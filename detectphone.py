import cv2
import numpy as np
import time
import cv2
thres = 0.45 # Threshold to detect object
#呼叫電腦連接的攝像頭，後面的參數代表攝像頭的編號
cap = cv2.VideoCapture(0)
cap.set(3,1280)
classNames= []
classFile = r'C:\Users\User\Downloads\Object-Detector-main\Object-Detector-main\coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = r'C:\Users\User\Downloads\Object-Detector-main\Object-Detector-main\ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = r'C:\Users\User\Downloads\Object-Detector-main\Object-Detector-main\frozen_inference_graph.pb'


net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# confidenceScore = 0 # if value is above 0.7, active punishment

efficencyMetric = 0

while True:
    success,img = cap.read()
    classIds, confs, bbox = net.detect(img,confThreshold=thres)
    #加入時間
    nowtime = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
    cv2.putText(img, nowtime, (300, 150), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 255, 255), 5, cv2.LINE_AA)
    if 1 in classIds :
        # confidenceScore = 1
        if efficencyMetric == 1:
            field_updates = {"value": 1}
        # print("ALERT: Off Task! Cell Phone Detected with high confidence level")

        efficencyMetric = 0
    else:
        # confidenceScore = 0
        if efficencyMetric == 0:
            field_updates = {"value": 0}
        # print("On Task: No cell phone or distractions detected")
        efficencyMetric = 1
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            cv2.rectangle(img,box,color=(0,255,0),thickness=2)
            #加入偵測物體的名稱
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

