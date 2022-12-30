#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 00:25:51 2022

@author: wangyongping
"""

# webcam鏡頭
import cv2
import numpy as np
import time
import os
def decode_fourcc(v):
    v = int(v)
    return "".join([chr((v>>8 *i) & 0xFF) for i in range(4)])    

def main():
    cap = cv2.VideoCapture(1)
    print(type(cap))
    
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print("圖片長寬",width,height)
    # get fourcc
    fourcc = cap.get(cv2.CAP_PROP_FOURCC)
    codec = decode_fourcc(fourcc)
    print("Codec:",codec)
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,960)
    
    
    face_cascade = cv2.CascadeClassifier("face.xml")

    # 開鏡頭
    while True:
        ret,frame = cap.read()
        #cv2.imshow('ugly face',frame)
        nowtime = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
        cv2.putText(frame, nowtime, (300, 150), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 255, 255), 5, cv2.LINE_AA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # 將鏡頭影像轉換成灰階
        faces = face_cascade.detectMultiScale(gray)      # 偵測人臉
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)   # 標記人臉
        cv2.imshow('hahahahahah', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'): # 按q關閉
            break
    cap.release()
    cv2.destroyAllWindows()
    
    #cap = cv2.VideoCapture("video.mp4")
    # 播影片
    while (cap.isOpened()):
        ret,frame = cap.read()
        cv2.imshow('my video',frame)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

    # 輸出影片
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,360)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter("Output.avi",fourcc,20.0,(640,360))
    while (cap.isOpened()):
        ret,frame = cap.read()
        if ret == True:
            out.write(frame)
            cv2.imshow('ugly face',frame)
            # 使用各種字體
            if cv2.waitKey(1) & 0xFF == ord('q'): # 按q關閉
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

main()