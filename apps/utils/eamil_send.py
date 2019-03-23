# _*_ coding: utf-8
__author__ = 'hb'
__date__ = '2019/3/20 15:00'
from users.models import EmailVerifyRecord
from random import Random
from django.core.mail import send_mail
from MxOnline.settings import EMAIL_FORM
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()
    if send_type == "register":
        email_title = "在线网注册激活链接"
        email_body = "请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title,email_body,EMAIL_FORM, [email])
        if send_status:
            print("发送成功")
        else:
            print("发送失败")
    elif send_type=="forget":
        email_title = "在线网注册密码重置链接"
        email_body = "请点击下面的链接重置你的密码: http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title,email_body,EMAIL_FORM, [email])