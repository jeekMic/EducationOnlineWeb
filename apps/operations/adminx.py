# _*_ coding: utf-8
__author__ = 'hb'
__date__ = '2019/3/9 11:25'
import xadmin
from .models import CourseComments,UserProfile, UserAsk,UserCourse,UserFavorite, UserMessage
class UserAksAdmin(object):
    list_display = ["name", "mobile", "course_name", "add_time"]
    serarch_fields = ["name", "mobile", "course_name"]
    list_filter = ["name", "mobile", "course_name"]


class CourseCommentsAdmin(object):
    list_display = ["user", "course", "comments", "add_time"]
    serarch_fields = ["user", "course", "comments"]
    list_filter = ["user", "course", "comments", "add_time"]

class UserCourseAdmin(object):
    list_display = ["user", "course", "genders", "add_time"]
    serarch_fields = ["user", "course", "genders"]
    list_filter = ["user", "course", "genders", "add_time"]


class UserFavoriteAdmin(object):
    list_display = ["user", "fav_id", "fav_type", "add_time"]
    serarch_fields = ["user", "fav_id", "fav_type"]
    list_filter = ["user", "fav_id", "fav_type", "add_time"]

class UserMessageAdmin(object):
    list_display = ["user", "message",  "has_read","add_time"]
    serarch_fields = ["user", "message",  "has_read"]
    list_filter = ["user", "message",  "has_read","add_time"]


xadmin.site.register(UserAsk,UserAksAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)