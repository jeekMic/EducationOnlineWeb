# _*_ coding: utf-8
__author__ = 'hb'
__date__ = '2019/3/9 11:03'
import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityAdmin(object):
    # 需要展示出来的字段
    list_display = ["name", "desc", "add_time"]
    # 搜索的字段，搜索的字段一般不涉及时间
    search_fields = ["name", "desc"]
    # 过滤的字段
    list_filter = ["name", "desc", "add_time"]

class CourseOrgAdmin(object):
    # 需要展示出来的字段
    list_display = ["name", "desc", "click_nums", "fav_name", "image", "address", "city"]
    #搜索的字段
    search_fields = ["name", "desc", "click_nums", "fav_name", "image", "address", "city"]
    # 过滤的字段
    list_filter = ["name", "desc", "click_nums", "fav_name", "image", "address", "city"]


class TeacherAdmin(object):
    # 需要展示出来的字段
    list_display = ["org", "name", "work_year", "work_company", "work_position", "points", "points", "click_nums", "add_time"]
    #搜索的字段
    search_fields = ["org", "name", "work_year", "work_company", "work_position", "points", "points", "click_nums"]
    # 过滤的字段
    list_filter = ["org", "name", "work_year", "work_company", "work_position", "points", "points", "click_nums", "add_time"]

xadmin.site.register(CityDict, CityAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
