# _*_ coding: utf-8
from django.urls import path

__author__ = 'hb'
__date__ = '2019/3/23 14:33'
from django.conf.urls import url, include

from .views import OrgView
# AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView
# from .views import TeacherListView, TeacherDetailView
app_name='org'
urlpatterns = [
    #课程机构列表页
    path('list/', OrgView.as_view(), name="org_list"),
    path('ask/', OrgView.as_view(), name="add_ask"),
    path('home/', OrgView.as_view(), name="org_home"),
    ]