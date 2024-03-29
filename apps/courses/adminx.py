# _*_ coding: utf-8 _*_ 

__author__ = 'astra'
__date__ = '2019/8/3 23:04'
import xadmin
from .models import Course, Lesson,Video,CourseResource


class CourseAdmin(object):

    # 在xadmin后台的列表功能
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times',
                    'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    # 在xadmin后台的搜索功能
    search_fields = ['name', 'desc', 'detail', 'degree','students']
    # 在xadmin后台的过滤器功能
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times',
                    'students', 'fav_nums', 'click_nums', 'add_time']


class LessonAdmin(object):
    # 在xadmin后台的列表功能
    list_display = ['course', 'name', 'add_time']
    # 在xadmin后台的搜索功能
    search_fields = ['course', 'name']
    # 在xadmin后台的过滤器功能
    list_filter =['course__name', 'name', 'add_time']


class VideoAdmin(object):
    # 在xadmin后台的列表功能
    list_display = ['lesson', 'name', 'add_time']
    # 在xadmin后台的搜索功能
    search_fields = ['lesson', 'name']
    # 在xadmin后台的过滤器功能
    list_filter =['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    # 在xadmin后台的列表功能
    list_display = ['course', 'name', 'download','add_time']
    # 在xadmin后台的搜索功能
    search_fields = ['lesson', 'name', 'download']
    # 在xadmin后台的过滤器功能
    list_filter =['course__name', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)