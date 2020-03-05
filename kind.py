import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sender = "xxx@xxx.xxx"  # 自己填上
password = "************"   # 自己填上
receivers = "xxx@xxx.xxx"   # 自己填上

subject = 'python发带附件的邮件测试'

msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receivers


msg.attach(MIMEText('使用python smtplib模块和email模块自动发送邮件测试', 'plain', 'utf-8'))


att1 = MIMEText(open("screenshot.bmp", "rb").read(), 'base64', 'utf-8')

att1["Content-Disposition"] = 'attachment; filename = "screenshot.bmp" '
msg.attach(att1)
try:
    s = smtplib.SMTP_SSL('smtp.163.com', 465)
    s.set_debuglevel(1)
    s.login(sender, password)
    s.sendmail(sender, receivers, msg.as_string())
    print('发送成功')

except:
    print('发送失败')