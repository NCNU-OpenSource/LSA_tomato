#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import time
import math
import mediapipe as mp
import pygame
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

pygame.mixer.init()
warning1 = pygame.mixer.Sound("phonealert.wav")
warning2 = pygame.mixer.Sound("personalert.wav")
music = pygame.mixer.Sound("relax.wav")
shot = pygame.mixer.Sound("shot.wav")
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

photo = 0
save_path = r'/home/yaxuan/LSA_project/'    # 照片的儲存路徑
file_name = 'photo'                         # 照片檔名

thres = 0.45 # Threshold to detect object

cap = cv2.VideoCapture(2)
cap.set(3,1280)
cap.set(4,720)
cap.set(10,70)

classNames = []
classFile = r'Object-Detector-main/coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = r'Object-Detector-main/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = r'Object-Detector-main/frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
print(net)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


def mail(count, working_time, break_time):
    today = datetime.date.today()
    content = 'working time = ' + str(working_time) + ' minutes' + '<br>'
    content += 'break_time = ' + str(break_time) + ' minutes' + '<br>'
    content += '完成：' + str(count) + '個循環'
    msg = MIMEMultipart()                          # 使用多種格式所組成的內容
    msg.attach(MIMEText(content, 'html', 'utf-8')) # 加入 HTML 內容
    # 使用 python 內建的 open 方法開啟指定目錄下的檔案
    with open('photo_0.jpg', 'rb') as file:
        img = file.read()
    attach_file = MIMEApplication(img, Name = 'photo_0.jpg') # 設定附加檔案圖片
    msg.attach(attach_file)                                  # 加入附加檔案圖片

    msg['Subject'] = "%s 番茄鐘使用時間" % today
    msg['From'] = "tomato"
    msg['To'] = 's109213068@mail1.ncnu.edu.tw'

    # smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp = smtplib.SMTP('smtp.gmail.com', 25)
    smtp.ehlo()
    smtp.starttls()
    # smtp.login() 的第二個參數 : 開啟應用程式密碼
    # https://support.google.com/accounts/answer/185833
    smtp.login('kieililiyihiaihiai@gmail.com', 'noumdhcaiewnwsii')
    status = smtp.send_message(msg)
    print(status)
    smtp.quit()

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

def hand(finger_angle,frame):
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,960)

    # 根據手指角度的串列內容，返回對應的手勢名稱
    f1 = finger_angle[0] # 大拇指角度
    f2 = finger_angle[1] # 食指角度
    f3 = finger_angle[2] # 中指角度
    f4 = finger_angle[3] # 無名指角度
    f5 = finger_angle[4] # 小拇指角度

    # 小於 50 表示手指伸直，大於等於 50 表示手指捲縮
    # if f1<50 and f2>=50 and f3>=50 and f4>=50 and f5>=50:
    #     return 'START' #good
    # elif f1>=50 and f2>=50 and f3>=50 and f4>=50 and f5>=50:
    #     return 'CLOSE' #0
    if f1>=50 and f2<50 and f3>=50 and f4>=50 and f5>=50:
        return '1'
    elif f1>=50 and f2<50 and f3<50 and f4>=50 and f5>=50: # 2: 拍照
        shot.play()
        cv2.imwrite(save_path + file_name + '_' + str(0) + '.jpg',frame)
        return '2'
    elif f1>=50 and f2>=50 and f3<50 and f4<50 and f5<50: # ok: 音樂
        music.play()
        time.sleep(3)
        return 'ok'
    # elif f1<50 and f2>=50 and f3<50 and f4<50 and f5<50:
    #     music.play()
    #     return 'ok'
    # elif f1>=50 and f2<50 and f3<50 and f4<50 and f5>50:
    #     return '3'
    # elif f1>=50 and f2>=50 and f3<50 and f4>=50 and f5>=50:
    #     return 'no!!!'
    # elif f1<50 and f2<50 and f3>=50 and f4>=50 and f5<50:
    #     return 'ROCK!'
    elif f1<50 and f2<50 and f3<50 and f4<50 and f5<50:
        music.stop()
        return 'STOP' #5
    # else:
    #     return

def tomato(minutes, notify_msg):
    start_time = time.perf_counter()
    diff_seconds = int(round(time.perf_counter() - start_time))
    left_seconds = minutes * 60 - diff_seconds
    # print(int(left_seconds / 60), int(left_seconds % 60))
    return left_seconds

def main():
    cap = cv2.VideoCapture(0)            # 讀取攝影機
    fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 印出文字的字型
    lineType = cv2.LINE_AA               # 印出文字的邊框
    # mediapipe 啟用偵測手掌
    with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
        w, h = 800, 450                                  # 影像尺寸
        # starttime = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
        count = 0
        working_time = 0
        break_time = 0
        start = False
        send = False
        # 開鏡頭
        while True:
            ret,frame= cap.read()
            classIds, confs, bbox = net.detect(frame,confThreshold=thres)

            img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # 轉換成 RGB 色彩
            results = hands.process(img2)                 # 偵測手勢
            text = 'notyet'
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
                        # print(finger_angle)                    # 印出角度 ( 有需要就開啟註解 )
                        text = hand(finger_angle,frame)          # 取得手勢所回傳的內容
                        cv2.putText(frame, text,(10,30), fontFace, 1, (0, 0, 0), 3, lineType) # 印出文字

            # choose mode
            if start == False:
                if text == '1':
                    working_time = 0.1        # 5 minute
                    break_time = 0.1          # 1 minute
                    start = True
                    a = tomato(working_time, 'Go working')
                elif text == '2':
                    working_time = 10       # 10 minute
                    break_time = 5          # 5 minute
                    start = True
                    a = tomato(working_time, 'Go working')
                elif text == 'ok':
                    working_time = 25       # 25 minute
                    break_time = 5          # 5 minute
                    start = True
                    a = tomato(working_time, 'Go working')
            else:
                if 77 in classIds:
                    cv2.putText(frame, "Warning!!", (180,250), fontFace, 2, (0, 0, 255), 3, lineType    ) # 印出文字      
                    warning1.play()
                    time.sleep(1)
                elif 1 not in classIds:
                    cv2.putText(frame, "NOT FOUND!!!", (120,250), fontFace, 2, (0, 0, 255), 3, lineType    ) # 印出文字                  
                    warning2.play()
                    time.sleep(1)
                if len(classIds) != 0:
                    for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
                        if classId == 77:
                            cv2.rectangle(frame,box,color=(0,0,255),thickness=2)
                            cv2.putText(frame,classNames[classId-1].upper(),(box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                
                nowtime = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
                cv2.putText(frame, nowtime,(10,70), fontFace, 1, (0, 0, 0), 3, lineType) # 印出文字

                a = a - 0.09
                minute = str(int(a / 60)).zfill(2)
                sec = str(int(a % 60)).zfill(2)
                countdown = "remaining time = " + minute + ":" + sec
                cv2.putText(frame, countdown, (10,110), fontFace, 1, (0, 0, 0), 3, lineType) # 印出文字
                if int(minute) <= 0 and int(sec) <= 0:
                    count += 1
                    time.sleep(1)
                    # if count == 4:
                    #     break
                    if count%2 != 0:
                        a = tomato(break_time, 'Take a break')
                    elif count%2 == 0:
                        a = tomato(working_time, 'Go working')
            cv2.imshow('Tomato', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'): # 按q關閉
                mail(count/2, working_time, break_time)
                send = True
                break
        if (send == False):
            mail(count/2, working_time, break_time)
    cap.release()
    cv2.destroyAllWindows()

main()
