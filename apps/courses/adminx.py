# _*_ coding: utf-8
import xadmin

__author__ = 'hb'
__date__ = '2019/3/8 16:47'
from .models import Course,Lesson,Video,CourseResource
class CourseAdmin(object):

    # 显示的字段后台
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times','students', 'fav_nums', 'image','click_nums', 'add_time']
    # 可搜索的字段
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times','students', 'fav_nums', 'image','click_nums']
    # 过滤字段 用户在后台选择过滤的标签就行了
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times','students', 'fav_nums', 'image','click_nums', 'add_time']
class LessonAdmin(object):
    # 显示的字段后台
    list_display = ['course', 'name', 'add_time']
    # 可搜索的字段
    search_fields = ['course', 'name']
    # 过滤字段 用户在后台选择过滤的标签就行了
    list_filter = ['course__name', 'name', 'add_time']

class VideoAdmin(object):
    # 显示的字段后台
    list_display = ['lesson', 'name', 'add_time']
    # 可搜索的字段
    search_fields = ['course', 'name']
    # 过滤字段 用户在后台选择过滤的标签就行了
    list_filter = ['lesson__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    # 显示的字段后台
    list_display = ['course', 'name', 'add_time',"download"]
    # 可搜索的字段
    search_fields = ['course', 'name',"download"]
    # 过滤字段 用户在后台选择过滤的标签就行了
    list_filter = ['course', 'name', 'add_time',"download"]



xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)