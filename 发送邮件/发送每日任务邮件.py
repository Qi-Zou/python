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

def sendMessage(context , sender , password , recipient):
    now_time = datetime.datetime.now().strftime("%Y-%m-%d")
    subject = now_time + "任务记录" #邮件主题
    #构造邮件
    msg=MIMEText(context,'plain' , 'utf-8') #msg为邮件内容对象
    msg["Subject"]=Header(subject , "utf-8")
    msg["Form"]=Header(sender , "utf-8")
    msg["To"]=Header(recipient , "utf-8")
    
    #发送邮件
    try:
        ss=smtplib.SMTP("SMTP.qq.com",25) #465为网易邮箱的端口号  ss是邮件对象
        ss.login(sender,password)
        ss.sendmail(sender,recipient,msg.as_string()) #发送邮件
        print("邮件发送成功!")
    except Exception as e:
        print("邮件发送失败!错误信息:",e)

def main():
    sender = "1532867899@qq.com"
    password = "12345"
    recipient = "zouqi@powersi.com.cn"
    logPath = "/home/yefan/Desktop/任务记录.txt"
    sourceFile = logPath
    now_time = datetime.datetime.now().strftime("%Y-%m-%d")
    targetFile = "/home/yefan/Desktop/任务记录/"+now_time+".txt"
    # 获取内容
    context = getTaskLog(logPath)
    # 发送邮件
    sendMessage(str(context), sender , password , recipient)
    # 移动日志文件
    moveFile(sourceFile , targetFile)

if __name__ == "__main__":
    main()