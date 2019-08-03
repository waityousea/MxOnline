# _*_ coding: utf-8 _*_ 

__author__ = 'astra'
__date__ = '2019/8/3 23:43'

import xadmin
from .models import UserAsk, UserComments, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    # 在xadmin后台的列表功能
    list_display = ['name', 'mobile', 'course_name','add_time']
    # 在xadmin后台的搜索功能
    search_fields = ['name', 'mobile', 'course_name']
    # 在xadmin后台的过滤器功能
    list_filter =['name', 'mobile', 'course_name','add_time']


class UserCommentsAdmin(object):
    # 在xadmin后台的列表功能
    list_display = ['user', 'course', 'comments','add_time']
    # 在xadmin后台的搜索功能
    search_fields = ['user', 'course', 'comments']
    # 在xadmin后台的过滤器功能
    list_filter =['user', 'course', 'comments','add_time']


class UserFavoriteAdmin(object):
    # 在xadmin后台的列表功能
    list_display = ['user', 'course', 'fav_id', 'fav_type','add_time']
    # 在xadmin后台的搜索功能
    search_fields = ['user', 'course', 'fav_id', 'fav_type']
    # 在xadmin后台的过滤器功能
    list_filter =['user', 'course', 'fav_id', 'fav_type','add_time']


class UserMessageAdmin(object):
    # 在xadmin后台的列表功能
    list_display = ['user', 'message', 'has_read','add_time']
    # 在xadmin后台的搜索功能
    search_fields = ['user', 'message', 'has_read']
    # 在xadmin后台的过滤器功能
    list_filter =['user', 'message', 'has_read','add_time']


class UserCourseAdmin(object):
    # 在xadmin后台的列表功能
    list_display = ['user', 'course', 'add_time']
    # 在xadmin后台的搜索功能
    search_fields = ['user', 'course']
    # 在xadmin后台的过滤器功能
    list_filter =['user', 'course','add_time']


xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserComments, UserCommentsAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)