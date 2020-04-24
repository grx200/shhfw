import os
import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

""" 该函数功能是获最新的HTML测试报告"""


def get_report(file):
    # dir指报告所在目录，listdir()方法是获取dir目录下所有文件和文件夹的列表
    lists = os.listdir(file)
    # 对列表进行排序，以创建时间顺序排序
    lists.sort(key=lambda fn: os.path.getatime(file + "\\" + fn))
    # 获取列表最后一个元素，即最新的HTML测试报告，再和目录dir拼接得到测试报告文件的路径
    file_name = os.path.join(file, lists[-1])
    # 返回获取到的测试报告文件的路径
    return file_name


""" 该函数功能是通过邮件发送测试报告"""


def send_email(file_name):
    # 定义发送邮件的服务器主机
    mail_host = 'smtp.163.com'
    # 定义发送邮件账号和授权码
    mail_user = 'test_report_send@163.com'
    mail_pass = 'qq3161490'
    # 定义接收邮件的账号,可以添加多个邮箱
    recivers = ['649809620@qq.com']
    # 定义发送邮件的类型，'related'类型是可以携带附件
    message = MIMEMultipart('related')
    # 打开报告文件并读取文件内容作为邮件的内容
    f = open(file_name, 'rb')
    mail_body = f.read()
    # 定义发送邮件附件的格式
    att = MIMEText(mail_body, 'base64', 'utf-8', )
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment;filename="report.html"'  # 定义附件名称
    # 为邮件加载附件
    message.attach(att)
    f.close()  # 关闭文件读取流
    # 定义发送邮件内容的格式
    msg = MIMEText(mail_body, 'html', 'utf-8')
    # 为邮件加载邮件内容
    message.attach(msg)
    # 指定发送邮件的账号
    message['Form'] = mail_user
    # 指定接收邮件的账号
    message['To'] = ','.join(recivers)
    # 定义邮件的标题
    message['Subject'] = Header('自动化测试报告', 'utf-8')
    # 邮件传输协议
    smtp = smtplib.SMTP()
    # 连接服务器主机
    smtp.connect(mail_host)
    # 登录发送邮件的账号
    smtp.login(mail_user, mail_pass)
    # 发送邮件
    smtp.sendmail(mail_user, recivers, message.as_string())
    smtp.quit()


if __name__ == '__main__':

    rep = get_report('../reports')
    send_email(rep) # 通过邮件发送测试报告的
