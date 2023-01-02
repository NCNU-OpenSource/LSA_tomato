# LSA期末報告
## 概念
- 鄰近考試時間卻沒有辦法專心唸書？會一直想要玩手機？
- 我們希望透過開發「一天一番茄，考試100分」，來監督讀書時的狀況，提升讀書效率（減少干擾與分心）。

## 功能
- 使用者可以透過手勢來制定想要專注的模式，並且利用相機偵測使用者是否在使用手機
    - 如果在專注模式下使用者突然離開，系統會開始計時，如果超過一分鐘，系統會自動停止計時，直到使用者回到畫面
    - 如果使用者在專注模式下使用手機，系統會發出警告
    - 當使用者有急事離開時可以暫停專注模式
    - 回到鏡頭後可以利用手勢再繼續計時
    - (mail回傳使用狀態)

## 使用設備
- 軟體:
    - raspberry pi OS
    - 
- 硬體：

| 序號 | 設備名稱       | 數量 | 來源 |
| ---- | -------------- | ---- | ---- |
|  1   | raspberry pi 3 | 1    | MOLi |
|  2   |pi camera       |  1   | MOLI |
|  3   | 海螺揚聲器（任何揚聲器都可以）          | 1    | 助教  |
|  4   | 螢幕（顯示器）   |  1   |      |
|  5   | 膠帶           | 1     |      |
|      |                |      |      |

## 建構過程

### Raspberry pi + pi camera + 揚聲器 模組
- pi cermera

![](https://i.imgur.com/QXr32hz.png)
- raspberry pi 3![](https://i.imgur.com/WaL7LBG.png)
- 將pi camera 連接 raspberry pi 3 
![](https://i.imgur.com/nI3ubhD.png)

    
- 揚聲器 ![](https://i.imgur.com/3nGeAop.png)
- 將轉接頭插入揚聲器 ![](https://i.imgur.com/D3aNLnT.png)



## 使用步驟
1. 
## demo 影片
## 工作分配
- 王詠平:
- 李亞軒:
- 林千榆:
- 張可葭:
- 黃郁庭：
## 參考資料
- https://www.techbang.com/posts/98379-little-brother-self-created-ai-anti-procrastination-system-as?fbclid=IwAR2PgQqElHSfI_3qW6eX_MqQHOO5SmE8TiVfZ5AM1osQ4MiB0iV8enTHW9M
- https://github.com/sjf0213/rpi/tree/master/opencv-gesture
- https://blog.cavedu.com/2020/11/11/microsoft-lobe-ai/
- https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2
- https://stackoverflow.com/questions/55028280/no-module-named-picamera
### 其他
- 帳號:pi
- 密碼 raspberry

## 下載OPEN CV
- [如何下載open CV](https://medium.com/@lin7lic/%E5%9C%A8raspberry-pi-3-%E5%AE%89%E8%A3%9Dpython-3-opencv-34c9740d78e4)
- 可能會出現的問題(內存不夠)
    - ![](https://i.imgur.com/7UcHbVu.png)
    - [解決辦法](https://medium.com/@lin7lic/%E5%9C%A8raspberry-pi-3-%E5%AE%89%E8%A3%9Dpython-3-opencv-34c9740d78e4)
    - https://blog.everlearn.tw/%E7%95%B6-python-%E9%81%87%E4%B8%8A-raspberry-pi/%E5%9C%A8-raspberry-pi-3-model-b-%E5%BB%BA%E7%AB%8B-python-3-6-%E7%92%B0%E5%A2%83
- [各種pi camera](https://picamera.readthedocs.io/en/latest/index.html)
