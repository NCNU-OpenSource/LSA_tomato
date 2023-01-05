# LSA Final Project
## Concept Development
- Do you have thers kinds of trouble? When the exam is coming, but still can not concentrate on your studies? Wasting your time on looking at your phone？
- We hope by develope「一天一番茄，考試100分」to supervise the status of studies and improve efficiency (reduce interference and distraction). 


##  Function
- 「一天一番茄，考試100分」monitors whether the user is using the mobile phone by identifying the mobile phone, and if so, system will alarm the user.
- The system will detect gesture or motion than respond accordingly.
    - If user leave the camera (camera cannot detect the user), a warning message will appear.
    - If the sysytem detects the gesture of 『ok』, it will play relax music.

    ![](https://i.imgur.com/gP07HMp.png =200x200)
    - If the sysytem detects the gesture of 『2』, it will take a foto.
    
    ![](https://i.imgur.com/jC8GrqS.png =200x200)
- When the system ends, it will send a mail to the mailbox showing the usage status
## Implementation Resources

- Software:
    - Unbutu
- Hardware：
    - Laptop * 1
    
    
## Implementation Process

1. Install Ubuntu：Please refer to the following website
    - [The website of install Ubuntu](https://hackmd.io/iRFQSqTaQgyOTa4reEtXag?view)

2. Setting the envirement：
    - install cmake: `sudo apt install cmake`
    - install git：`sudo apt install git`
    - install pip:`sudo apt install pip`
    - install mediapipe: Please refer to the following website
        - [The website of install mediapipe](https://google.github.io/mediapipe/getting_started/install.html)
    - install opencv：Please refer to the following website
        - [The website of install opencv](https://docs.opencv.org/3.4/d7/d9f/tutorial_linux_install.html)
    - install pygame：`sudo apt install python-pygame` 
    - install ubuntu package（for camera）：
        - Confirm Ubuntu version
        - install the same version of package：
            - [The website of install ubuntu package](https://download.virtualbox.org/virtualbox/6.1.38/)

3. Clone the python code on git-hub：`git clone https://github.com/wyping314/LSA_project.git`
4. 

## Usage
1. execute program`python mainproject.py`
2. 會開始倒數所設定的

## Demo vedio
## Job Assignment
- 王詠平：program（detect gestures, detect person, Pomodoro）、program integration
- 李亞軒：program(detect cell phone, other funtions)、program development
- 林千榆：setting environment、program（Sent back mail）、program development
- 張可葭：setting environment、raspi research、github content、ppt
- 黃郁庭：setting environment、program(detect cell phone, other funtions)、program development、Thoughts on the topic、raspi research
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


## 感謝
- 感謝在MOLi學長姐的無私幫忙
- 感謝提供設備的柏瑋助教及MOLi
## Other

### Using raspberry pi

#### Implementation Resources

- 軟體:
    - raspberry pi OS
- 硬體：



| 序號 | 設備名稱                      | 數量 | 來源 |
| ---- | ----------------------------- | ---- | ---- |
| 1    | raspberry pi 3                | 1    | MOLi |
| 2    | pi camera                     | 1    | MOLi |
| 3    | 海螺揚聲器（任何揚聲器都可以) | 1    | 助教 |
| 4    | 螢幕（顯示器)                 | 1    |      |
| 5    | 膠帶(固定用)                  | 1    |      |

#### Implementation Process

1. 將 SD 卡格式化，與 raspberry pi 連接

2. 架設 Raspberry pi + pi camera + 揚聲器 模組
    - pi cermera
    ![](https://i.imgur.com/QXr32hz.png)
    - raspberry pi 3![](https://i.imgur.com/WaL7LBG.png =400x400)
    - 將pi camera 連接 raspberry pi 3 
    ![](https://i.imgur.com/nI3ubhD.png)

    
    - 揚聲器 ![](https://i.imgur.com/3nGeAop.png =400x400)
    - 將轉接頭插入揚聲器 ![](https://i.imgur.com/D3aNLnT.png =400x400)

3. 建構環境：
    - 下載 mediapipe：請參考以下網址
        - [下載 mediapipe 網頁](https://pypi.org/project/mediapipe-rpi4/)
    - 下載 cv2：請參考以下網址
        - [下載 cv2 網頁](https://medium.com/@stepanfilonov/tracking-your-eyes-with-python-3952e66194a6)

## 下載OPEN CV
- [如何下載open CV](https://medium.com/@lin7lic/%E5%9C%A8raspberry-pi-3-%E5%AE%89%E8%A3%9Dpython-3-opencv-34c9740d78e4)
- 可能會出現的問題(內存不夠)
    - ![](https://i.imgur.com/7UcHbVu.png)
    - [解決辦法](https://medium.com/@lin7lic/%E5%9C%A8raspberry-pi-3-%E5%AE%89%E8%A3%9Dpython-3-opencv-34c9740d78e4)
    - https://blog.everlearn.tw/%E7%95%B6-python-%E9%81%87%E4%B8%8A-raspberry-pi/%E5%9C%A8-raspberry-pi-3-model-b-%E5%BB%BA%E7%AB%8B-python-3-6-%E7%92%B0%E5%A2%83
- [各種pi camera](https://picamera.readthedocs.io/en/latest/index.html)
