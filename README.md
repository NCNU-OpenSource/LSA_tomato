# LSA Final Project － 「一天一番茄，考試100分」
## Concept Development
- Do you have these kinds of trouble? When the exam is coming, but still can not concentrate on your studies? Wasting your time on looking at your phone？
- We hope by develope「一天一番茄，考試100分」to supervise the status of studies and improve efficiency (reduce interference and distraction). 

##  Function
- 「一天一番茄，考試100分」monitors whether the user is using the mobile phone by identifying the mobile phone, and if so, system will alarm the user.
- The system will detect gesture or motion than respond accordingly.
    - At system start, the user can select one of three timekeeping modes. Use gestures 1, 2 or 3 to select. 
    - If user leave the camera (camera cannot detect the user), a warning message will appear.
    - If the sysytem detects the gesture of 『ok』, it will play relax music.

    ![](https://i.imgur.com/gP07HMp.png)
    - If you want to stop the music by detects the gesture of 『5』. 

     ![](https://i.imgur.com/l829TlY.png)



    - If the sysytem detects the gesture of 『2』, it will take a foto.
    
    ![](https://i.imgur.com/jC8GrqS.png)
- When the system ends, it will send a mail to the mailbox showing the usage status
- tab `q` to  ending the function
## Implementation Resources

- Software:
    - ~~raspberry pi OS~~
    - Unbutu
- Hardware：


| 序號 | 設備名稱                     | 數量 | 來源 |
| ---- | ---------------------------- | ---- | ------- |
| 1  | ~~raspberry pi 3~~                 | 1    | MOLi |
| 2    | ~~pi camera~~                      | 1    | MOLi    |
| 3    | ~~海螺揚聲器（任何揚聲器都可~~ | 1    | 助教    |
| 4    | ~~Screen（monitor）~~              | 1    |         |
| 5    | ~~adhesive tape~~            |1
| 6 | Laptop    | 1 |      |

    
## Implementation Process

### 樹莓派環境
1. ~~將 SD 卡格式化，與 raspberry pi 連接~~

2. ~~架設 Raspberry pi + pi camera + 揚聲器 模組~~
    - ~~pi cermera~~
    ![](https://i.imgur.com/QXr32hz.png)
    - ~~raspberry pi 3~~ ![](https://i.imgur.com/WaL7LBG.png)
    - ~~將pi camera 連接 raspberry pi 3~~ 
    ![](https://i.imgur.com/nI3ubhD.png)

    
    - ~~揚聲器~~ ![](https://i.imgur.com/qMFznTV.jpg)
    - ~~將轉接頭插入揚聲器~~ 
    ![](https://i.imgur.com/SSF3Jj5.png)


3. ~~建構環境~~：
- Problem：
    1.  一開始希望使用 Tensorflow 訓練偵測手機模型，但後來因能力不足，加上有找到可以替代的模組，改而使用模組
    2.   如果使用 pi camera 的話樹莓派只能使用 32 bits
    3.    一開始我們原本安裝 conda 以便快速安裝 opencv (只需 20 分鐘)，但後來發現環境無法通用且我們需要的模組（dnn.detection model）只有 4.1 以上的 opencv 才可以支援，但 conda 中的 opencv 只有 3.6.7
            - 嘗試升級 conda 中的 opencv 版本但以失敗告終。
    4. 官方下載 mediapipe 的封包無法支援 32 bits，後來經由非官方資源才成功裝載支援 32 bits 的 mediapipe
    5. 將SD卡格式化，重新下載環境，直接載完整的 opencv，但途中也遇到問題：樹莓派耗損跑不動（措施：換新的樹莓派），且最終也仍然無法成功安裝。
    6. 嘗試依照學長建議直接安裝 cv2，有安裝成功但發現裡面沒有我們所需的模組，因此也失敗。
    
4. 樹莓派
   - ~~下載 mediapipe：請參考以下網址~~
        - ~~因為我們需要使用pi camera，所以只能將raspberry pi 使用 32 bit，但目前大多數 mediapipe 都只能支援 64 bit，後來找到以下網頁內的資訊，才有辦法安裝 mediapipe。~~
        - [下載 mediapipe 網頁](https://pypi.org/project/mediapipe-rpi4/)
    - ~~下載 cv2：請參考以下網址~~
        - [下載 cv2 網頁](https://medium.com/@stepanfilonov/tracking-your-eyes-with-python-3952e66194a6)

#### 樹莓派最終結果：
- 因在樹莓派上無法下載 opencv 因此無法將環境建構完成，所以改用虛擬機建構及執行，方法請參考下方步驟

---
### Linux

1. Install Ubuntu：Please refer to the following website
    - [The website of install Ubuntu](https://hackmd.io/iRFQSqTaQgyOTa4reEtXag?view)

2. Setting the environment：
    - install cmake: `sudo apt install cmake`
    - install git：`sudo apt install git`
    - install pip:`sudo apt install pip`
    - install mediapipe: Please refer to the following website
        - `git clone https://github.com/google/mediapipe.git`
        - [reference : The website of install mediapipe](https://google.github.io/mediapipe/getting_started/install.html)
    - install opencv：Please refer to the following website
        - [The website of install opencv](https://docs.opencv.org/3.4/d7/d9f/tutorial_linux_install.html)
          :::info
          1. `git clone https://github.com/opencv/opencv.git`
          2. `git clone https://github.com/opencv/opencv_contrib.git`
          3. `cd ~/opencv`
          4. `mkdir build`
          5. `cd build`
          6. `cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..`
          7. `make -j3` # 看你開幾顆CPU
          8. `sudo make install`
          9. `git clone https://github.com/opencv/opencv_extra.git`
          :::
    - install pygame：`sudo apt install python-pygame` 
    - `pip install pygame`
    - `pip install opencv-python`
    - install ubuntu package（for camera）：
        - Confirm Ubuntu version
         ![](https://i.imgur.com/JNz1jHU.jpg)
        - install the same version of package：
            - [The website of install ubuntu package](https://download.virtualbox.org/virtualbox/6.1.38/)
    - check your camera
      ![](https://i.imgur.com/aU6q3vp.png)


## Usage
1. Clone the project on GitHub：`git clone https://github.com/wyping314/LSA_project.git`
2.  `cd LSA_project`
3. `vim tomato.py`
    1. Modify the path to store pictures:`save_path` 
    2. Modify the recipient `msg['To']` which in `def mail()` 
    3. Modify two parameters `smtp.login()` which in `def mail()`
        - [產生及使用應用程式密碼](https://support.google.com/accounts/answer/185833)
    4. Adjust the parameters of the lens `VideoCapture()` (total of three places) according to your equipment
4. execute program `python3 mainproject.py`
5. The system will pop up the camera window
6. Read how to use & Choose mode
7. Pomodoro Technique start
8. System start detecting the user

## Code
### 番茄鐘回傳剩餘時間
* 選擇模式
```python=
start = False
if start == False:
    if text == '1':
        # test mode
        working_time = 0.1
        break_time = 0.1
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
```
* 計算剩餘時間
```python=
def tomato(minutes):
    start_time = time.perf_counter()
    diff_seconds = int(round(time.perf_counter() - start_time))
    left_seconds = minutes * 60 - diff_seconds
    return left_seconds
```
* 在畫面上顯示讀書和休息的剩餘時間
```python=
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

```
### 辨識手勢
* 音效
```python=
pygame.mixer.init()
warning1 = pygame.mixer.Sound("phonealert.wav")
warning2= pygame.mixer.Sound("personalert.wav")
music= pygame.mixer.Sound("relax.wav")
shot= pygame.mixer.Sound("shot.wav")
```
* 根據角度判斷手勢
    * [參考來源](https://steam.oxxostudio.tw/category/python/ai/ai-mediapipe-gesture.html)
```python=
def hand(finger_angle,frame):
    
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
        shot.play()
        cv2.imwrite(save_path + file_name + '.jpg',frame)
        return '2'
    
    elif f1>=50 and f2>=50 and f3<50 and f4<50 and f5<50:
        music.play()
        time.sleep(1)
        return 'ok'

    elif f1<50 and f2<50 and f3<50 and f4<50 and f5<50:
        music.stop()
        return 'STOP' #5
    else:
        return
```
* 在每一幀畫面中辨識手勢
```python=
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
            text = hand(finger_angle,frame)            # 取得手勢所回傳的內容
```

### 偵測手機、人臉
* 匯入模型／設定參數
    * [參考來源](https://github.com/ayushpai/Object-Detector.git)
```python=
classNames= []
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
```
* 辨識每一幀畫面中是否有手機和人臉
```python=
classIds, confs, bbox = net.detect(frame,confThreshold=thres)
#偵測到手機
if 77 in classIds:
    cv2.putText(frame, "Warning!!",(30,400), fontFace, 5, (0,0,255), 10, lineType) # 印出文字
    warning1.play()
    time.sleep(1)
#偵測不到手機也偵測不到人
elif 1 not in classIds:
    cv2.putText(frame, "NOT FOUND!!!",(180,400), fontFace, 5, (0, 0, 255), 8, cv2.FONT_HERSHEY_COMPLEX) # 印出文字
    warning2.play()
    time.sleep(2.5)
    warning2.stop()
#偵測到手機後匡選
if len(classIds) != 0:
    for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
        if classId == 77:
            cv2.rectangle(frame,box,color=(0,0,255),thickness=2)
            cv2.putText(frame,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                        cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
```
### 寄信給使用者
```python=
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
    msg['To'] = 'account@mail1.ncnu.edu.tw'

    # smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp = smtplib.SMTP('smtp.gmail.com', 25)
    smtp.ehlo()
    smtp.starttls()
    # smtp.login() 的第二個參數 : 開啟應用程式密碼
    # https://support.google.com/accounts/answer/185833
    smtp.login('account@gmail.com', '金鑰')
    status = smtp.send_message(msg)
    print(status)
    smtp.quit()
```

## Demo Viedo
- https://youtu.be/cgwadJ77LnI
## Job Assignment
- 王詠平：program（detect gestures, detect person, Pomodoro）、program integration
- 李亞軒：program(detect cell phone, other funtions)、program development
- 林千榆：setting environment、program（Sent back mail）、program development
- 張可葭：setting environment、raspi research、github content、ppt、Demo veido
- 黃郁庭：setting environment、program(detect cell phone, other funtions)、program development、Thoughts on the topic、raspi research


## Thankful
- 感謝在MOLi學長姐的無私幫忙
- 感謝提供設備的柏瑋助教及MOLi
## References
- https://www.techbang.com/posts/98379-little-brother-self-created-ai-anti-procrastination-system-as?fbclid=IwAR2PgQqElHSfI_3qW6eX_MqQHOO5SmE8TiVfZ5AM1osQ4MiB0iV8enTHW9M
- https://github.com/sjf0213/rpi/tree/master/opencv-gesture
- https://github.com/ayushpai/Object-Detector
- https://blog.cavedu.com/2020/11/11/microsoft-lobe-ai/
- https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2
- https://stackoverflow.com/questions/55028280/no-module-named-picamera
- https://caffeinedev.medium.com/how-to-install-tensorflow-on-m1-mac-8e9b91d93706
- https://realpython.com/face-recognition-with-python/
- https://gogoprivateryan.blogspot.com/2015/09/opencv-3-opencv-python-face-recognition.html
- https://blog.csdn.net/lovelyaiq/article/details/26501983
- https://hackmd.io/@TienYi/HJf4gGnrF
- https://www.jeremymorgan.com/tutorials/raspberry-pi/how-to-install-opencv-raspberry-pi/
- https://www.youtube.com/watch?v=QzVYnG-WaM4
- https://www.circuspi.com/index.php/2022/07/29/ai-mediapipe-hand/

## Powerpoint
- [ppt連結](https://www.canva.com/design/DAFXVa3epzM/b-NLYZIazco1a-YTvCysxQ/view?utm_content=DAFXVa3epzM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
