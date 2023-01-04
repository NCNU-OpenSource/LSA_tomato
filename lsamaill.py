import smtplib
from email.mime.text import MIMEText
import time
import datetime

def message():
    today=datetime.date.today()
    content='今日讀書時間:\n 今日手機使用次數 \n 暫停次數\n'
    mime=MIMEText(content, "html", "utf-8")
    mime['Subject']="%s 番茄鐘使用時間"%today
    mime["From"]="番茄紀錄"
    #subject='Subject:%s study time'%today
    #studytime='今日讀書時間:\n'
    #usePhone='今日'
    return mime.as_string()


def main():
    smtp=smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()#tls 加密
    smtp.login('dryfish828@gmail.com','ccwgwsrgdxqvcgtc')#要去google 帳戶>安全性>app 生成
    from_addr='dryfish828@gmail.com'
    to_addr="una910828@gmail.com"
    msg=message()
    smtp.sendmail(from_addr, to_addr, msg)
main()