import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header


smtpserver = 'smtp.163.com'
username = 'test_report_send@163.com'
password='qq3161490'
sender='test_report_send@163.com'
#receiver='XXX@126.com'
#收件人为多个收件人
receiver=['test_report_send@163.com','649809620@qq.com']

subject = '测试报告 '

msg = MIMEMultipart('mixed')
msg['Subject'] = "自动化测试报告3"
msg['From'] = 'test_report_send@163.com'
msg['To'] = ";".join(receiver)
msg['Date'] = Header(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'utf-8')


#构造文字内容
text = ''''

木木木么么么么么么么么么么么么么么

'''
text_plain = MIMEText(text,'plain', 'utf-8')
msg.attach(text_plain)
#构造附件
sendfile=open(r'E:\shhfw\reports\2019-10-11 15_48_33 test_report.html','rb').read()
text_att = MIMEText(sendfile, 'base64', 'utf-8')
text_att["Content-Type"] = 'application/octet-stream'
#以下附件可以重命名成aaa.txt
####不能直接发送测试报告，因为网易或者QQ邮箱会认为是垃圾邮件拒收，所有必须更改测试报告的后缀
#接收邮件后，再手动更改后缀
text_att.add_header('Content-Disposition', 'attachment', filename='report.txt')
msg.attach(text_att)
#发送邮件
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()