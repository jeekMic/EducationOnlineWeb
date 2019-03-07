# _*_ coding: utf-8
__author__ = 'hb'
__date__ = '2019/3/7 16:39'
from .models import EmailVerifyRecord
import xadmin
class EmailVerifyRecordAdmin(object):
    pass
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)