#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 21:36:12 2023

@author: wangyongping
"""


# webcam鏡頭
import cv2
import numpy as np
import time
import os
import mediapipe as mp
import math
import sys

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# 根據兩點的座標，計算角度
def vector_2d_angle(v1, v2):
    v1_x = v1[0]
    v1_y = v1[1]
    v2_x = v2[0]
    v2_y = v2[1]
    try:
        angle_= math.degrees(math.acos((v1_x*v2_x+v1_y*v2_y)/(((v1_x**2+v1_y**2)**0.5)*((v2_x**2+v2_y**2)**0.5))))
    except:
        angle_ = 180
    return angle_

# 根據傳入的 21 個節點座標，得到該手指的角度
def hand_angle(hand_):
    angle_list = []
    # thumb 大拇指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[2][0])),(int(hand_[0][1])-int(hand_[2][1]))),
        ((int(hand_[3][0])- int(hand_[4][0])),(int(hand_[3][1])- int(hand_[4][1])))
        )
    angle_list.append(angle_)
    # index 食指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])-int(hand_[6][0])),(int(hand_[0][1])- int(hand_[6][1]))),
        ((int(hand_[7][0])- int(hand_[8][0])),(int(hand_[7][1])- int(hand_[8][1])))
        )
    angle_list.append(angle_)
    # middle 中指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[10][0])),(int(hand_[0][1])- int(hand_[10][1]))),
        ((int(hand_[11][0])- int(hand_[12][0])),(int(hand_[11][1])- int(hand_[12][1])))
        )
    angle_list.append(angle_)
    # ring 無名指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[14][0])),(int(hand_[0][1])- int(hand_[14][1]))),
        ((int(hand_[15][0])- int(hand_[16][0])),(int(hand_[15][1])- int(hand_[16][1])))
        )
    angle_list.append(angle_)
    # pink 小拇指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[18][0])),(int(hand_[0][1])- int(hand_[18][1]))),
        ((int(hand_[19][0])- int(hand_[20][0])),(int(hand_[19][1])- int(hand_[20][1])))
        )
    angle_list.append(angle_)
    return angle_list


def decode_fourcc(v):
    v = int(v)
    return "".join([chr((v>>8 *i) & 0xFF) for i in range(4)])    

def hand(finger_angle):
    cap = cv2.VideoCapture(1)
    #print(type(cap))
    
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    #print("圖片長寬",width,height)
    # get fourcc
    fourcc = cap.get(cv2.CAP_PROP_FOURCC)
    codec = decode_fourcc(fourcc)
    #print("Codec:",codec)
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,960)
    
    
# 根據手指角度的串列內容，返回對應的手勢名稱
    f1 = finger_angle[0]   # 大拇指角度
    f2 = finger_angle[1]   # 食指角度
    f3 = finger_angle[2]   # 中指角度
    f4 = finger_angle[3]   # 無名指角度
    f5 = finger_angle[4]   # 小拇指角度

    # 小於 50 表示手指伸直，大於等於 50 表示手指捲縮
    if f1<50 and f2>=50 and f3>=50 and f4>=50 and f5>=50:
        return 'START' #good
    elif f1>=50 and f2>=50 and f3>=50 and f4>=50 and f5>=50:
        return 'CLOSE' #0
    elif f1>=50 and f2<50 and f3>=50 and f4>=50 and f5>=50:
        return '1'
    elif f1>=50 and f2<50 and f3<50 and f4>=50 and f5>=50:
        return '2'
    elif f1>=50 and f2>=50 and f3<50 and f4<50 and f5<50:
        return 'ok'
    elif f1<50 and f2>=50 and f3<50 and f4<50 and f5<50:
        return 'ok'
    elif f1>=50 and f2<50 and f3<50 and f4<50 and f5>50:
        return '3'
    elif f1>=50 and f2>=50 and f3<50 and f4>=50 and f5>=50:
        return 'no!!!'
    elif f1<50 and f2<50 and f3>=50 and f4>=50 and f5<50:
        return 'ROCK!'
    elif f1<50 and f2<50 and f3<50 and f4<50 and f5<50:
        return 'STOP' #5

    else:
        return ''
    '''    elif f1>=50 and f2>=50 and f3<50 and f4>=50 and f5>=50:
            return 'no!!!'
        elif f1<50 and f2<50 and f3>=50 and f4>=50 and f5<50:
            return 'ROCK!'
    '''
    
def tomato(minutes, notify_msg):
    start_time = time.perf_counter()
    diff_seconds = int(round(time.perf_counter() - start_time))
    left_seconds = minutes * 60 - diff_seconds
    #print(int(left_seconds / 60), int(left_seconds % 60))
    return left_seconds


def progressbar(curr, total, duration=10, extra=''):
    frac = curr / total
    filled = round(frac * duration)
    print('\r', '🍅' * filled + '--' * (duration - filled), '[{:.0%}]'.format(frac), extra, end='')



'''def countdown():

    a = tomato(1, 'It is time to take a break')
    #print(a)
    for i in range(a,0,-1):
        print(int(i / 60), int(i % 60))
        return int(i / 60), int(i % 60)
'''

    
def main():
    face_cascade = cv2.CascadeClassifier("face.xml")
    cap = cv2.VideoCapture(1)            # 讀取攝影機
    fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 印出文字的字型
    lineType = cv2.LINE_AA               # 印出文字的邊框

    # mediapipe 啟用偵測手掌
    with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
        w, h = 800, 450                                  # 影像尺寸
        #starttime = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
        a = tomato(0.25, 'It is times to take a break')
        count = 0
        # 開鏡頭
        while True:
            ret,frame= cap.read()
            #img = cv2.resize(img, (w,h))                 # 縮小尺寸，加快處理效率
            #cv2.imshow('ugly face',frame)
            nowtime = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
            cv2.putText(frame, nowtime, (300, 150), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 255, 255), 5, cv2.LINE_AA)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # 將鏡頭影像轉換成灰階
            faces = face_cascade.detectMultiScale(gray)      # 偵測人臉
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)   # 標記人臉
            img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 轉換成 RGB 色彩
            results = hands.process(img2)                # 偵測手勢
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    finger_points = []                   # 記錄手指節點座標的串列
                    for i in hand_landmarks.landmark:
                        # 將 21 個節點換算成座標，記錄到 finger_points
                        x = i.x*w
                        y = i.y*h
                        finger_points.append((x,y))
                    if finger_points:
                        finger_angle = hand_angle(finger_points) # 計算手指角度，回傳長度為 5 的串列
                        #print(finger_angle)                     # 印出角度 ( 有需要就開啟註解 )
                        text = hand(finger_angle)            # 取得手勢所回傳的內容
                        cv2.putText(frame, text,(30,120), fontFace, 3, (255, 255, 255), 10, lineType) # 印出文字
            #a = tomato(1, 'It is times to take a break')
            #print(a)
            a = a - 0.3
            minute = str(int(a / 60))
            sec = str(int(a % 60))
            countdown = "remaining time=" + minute + ":" + sec
            cv2.putText(frame, countdown, (160,220), fontFace, 2, (0,0,0), 3, lineType) # 印出文字
                #cv2.putText(frame, text, (30,120), fontFace, 5, (255, 255, 255), 10, lineType) # 印出文字
            if int(minute) <= 0 and int(sec) <= 0:
                count+=1
                #print(count)
                time.sleep(1)
                #cv2.putText(frame, "relax time", (160,220), fontFace, 2, (0,0,0), 3, lineType)
                if count == 2:
                    break
                elif count%2 != 0:
                    a += 10
                elif count%2 == 0:
                    a += 15
          
            cv2.imshow('Tomato', frame)
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