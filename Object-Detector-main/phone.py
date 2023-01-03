#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 18:16:34 2023

@author: wangyongping
"""

import cv2
# import firebase_admin
import time
# from firebase_admin import credentials
# from firebase_admin import firestore
#import winsound #發出聲音
import os
#拍照用的
cap = cv2.VideoCapture(1)
i=0
save_path = r'/Users/wangyongping/Desktop/LSA_project/Object-Detector-main'      # 儲存路徑
file_name = 'test'                          # 檔名


#發出聲音用的
frequency = 2000
duration = 1000

thres = 0.45 # Threshold to detect object

cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)
cap.set(10,70)

classNames= []
classFile = r'/Users/wangyongping/Desktop/LSA_project/Object-Detector-main/coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = r'/Users/wangyongping/Desktop/LSA_project/Object-Detector-main/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = r'/Users/wangyongping/Desktop/LSA_project/Object-Detector-main/frozen_inference_graph.pb'


# cred = credentials.Certificate(r"C:\Users\User\Downloads\Object-Detector-main\Object-Detector-main\disco-bedrock-296-firebase-adminsdk-suhzw-34a818d89e.json") # You would need to connect this to your own firebase server
# firebase_admin.initialize_app(cred)

# db = firestore.client()
# doc_ref = db.collection(u'123').document("EIniiP9ToMzE3inMbFkp") # add this document to your own firebase server



net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

confidenceScore = 0 # if value is above 0.7, active punishment

efficencyMetric = 0

while True:
    success,img = cap.read()
    classIds, confs, bbox = net.detect(img,confThreshold=thres)
    # print(classIds,bbox)

    if 77 in classIds or 73 in classIds or 61 in classIds:
        confidenceScore = 1
        if efficencyMetric == 1:
            field_updates = {"value": 1}
            # doc_ref.update(field_updates)
        print("ALERT: Off Task! Cell Phone Detected with high confidence level")

        # winsound.Beep(frequency, duration)#發出逼逼聲音
        #拍照
        # ret, frame = cap.read()                 # 讀取相機影像
        # cv2.imshow('cap', frame)                # 顯示影像
        # cv2.imwrite(save_path + file_name + '_' + str(i) + '.jpg',frame)
        # print('save:',file_name + '_' + str(i) + '.jpg')
        # i = i + 1
        # time.sleep(2)
        ###
        efficencyMetric = 0
    else:
        confidenceScore = 0
        if efficencyMetric == 0:
            field_updates = {"value": 0}
            # doc_ref.update(field_updates)#把值加到資料庫
        print("On Task: No cell phone or distractions detected")
        efficencyMetric = 1
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            cv2.rectangle(img,box,color=(0,255,0),thickness=2)
            cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                        cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                        cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    #在影像中加入文字
    text = '1244444'
    cv2.putText(img, text, (100, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow("Output",img)
    cv2.waitKey(1)
    ####

    #如果改成不專心的次數(每偵測到一次手機就更新資料庫讓他加1)
    #結合番茄鍾