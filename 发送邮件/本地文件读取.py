import os
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def moveFile(sourceFile , targetFile):
    os.system("cp " + sourceFile + " " + targetFile)

def getTaskLog(logPath):
    f = open(logPath , mode='r' , encoding='utf-8')
    return f.read

def sendMessage(context):
    msg_from="1532867899@qq.com" #发送方地址
    pwd="ahrjmcfkdhziifja" #授权密码
    to="826245622@qq.com" #接收方地址
    now_time = datetime.datetime.now().strftime("%Y-%m-%d")
    subject = now_time + "任务记录" #邮件主题
    
    #构造邮件
    msg=MIMEText(context,'plain' , 'utf-8') #msg为邮件内容对象
    msg["Subject"]=Header(subject , "utf-8")
    msg["Form"]=Header(msg_from , "utf-8")
    msg["To"]=Header(to , "utf-8")
    
    #发送邮件
    try:
        ss=smtplib.SMTP("SMTP.qq.com",25) #465为网易邮箱的端口号  ss是邮件对象
        ss.login(msg_from,pwd)
        ss.sendmail(msg_from,to,msg.as_string()) #发送邮件
        print("邮件发送成功!")
    except Exception as e:
        print("邮件发送失败!错误信息:",e)

def main():
    logPath = "home/yefan/Desktop/任务记录.txt"
    sourceFile = logPath
    now_time = datetime.datetime.now().strftime("%Y-%m-%d")
    targetFile = "/home/yefan/Desktop/任务记录/"+now_time+".txt"
    sendMessage(getTaskLog(logPath))
    moveFile(sourceFile , targetFile)

if __name__ == "__main__":
    main()