# _*_ coding: utf-8 _*_ 

__author__ = 'astra'
__date__ = '2019/8/3 23:30'

import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):

    # 在xadmin后台的列表功能
    list_display = ['name', 'desc', 'add_time']
    # 在xadmin后台的搜索功能
    search_fields = ['name', 'desc']
    # 在xadmin后台的过滤器功能
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):

    # 在xadmin后台的列表功能
    list_display = ['name', 'desc','click_nums','fav_nums','image','address','city', 'add_time']
    # 在xadmin后台的搜索功能
    search_fields = ['name', 'desc','click_nums','fav_nums','image','address','city']
    # 在xadmin后台的过滤器功能
    list_filter = ['name', 'desc','click_nums','fav_nums','image','address','city', 'add_time']


class TeacherAdmin(object):

    # 在xadmin后台的列表功能
    list_display = ['org', 'name','work_years','work_company','work_position','points','fav_nums', 'click_nums', 'add_time']
    # 在xadmin后台的搜索功能
    search_fields = ['org', 'name','work_years','work_company','work_position','points','fav_nums', 'click_nums']
    # 在xadmin后台的过滤器功能
    list_filter = ['org', 'name','work_years','work_company','work_position','points','fav_nums', 'click_nums', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)