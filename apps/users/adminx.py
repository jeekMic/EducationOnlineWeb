# _*_ coding: utf-8
__author__ = 'hb'
__date__ = '2019/3/7 16:39'
from .models import EmailVerifyRecord, Banner
import xadmin
from xadmin import views
# 主题管理配置 需要像xadmin一样注册
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
# 标题和注脚的配置
class GlobalSetting(object):
    site_title = "老周学院后台管理系统"
    site_footer = "老周网络学院"
    # 配置菜单可折叠的状态
    menu_style = "accordion"

class EmailVerifyRecordAdmin(object):
    # 显示的字段后台
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 可搜索的字段
    search_fields = ['code', 'email', 'send_type']
    # 过滤字段 用户在后台选择过滤的标签就行了
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    # 显示的字段后台
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    # 可搜索的字段
    search_fields = ['title', 'image', 'url', 'index']
    # 过滤字段 用户在后台选择过滤的标签就行了
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)