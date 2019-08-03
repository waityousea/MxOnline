# _*_ coding: utf-8 _*_

__author__ = 'astra'
__date__ = '$DATE $TIME'
import xadmin
from xadmin import views
from .models import EmailVerifyRecord,Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    #把后台的Django改成"慕学后台管理系统"
    site_title = "慕学后台管理系统"
    # 把后台的"我的公司"改成"慕学在线网"
    site_footer = "慕学在线网"
    #xadmin后台的菜单收起功能
    menu_style = "accordion"



class EmailVerifyRecordAdmin(object):
   #在xadmin后台的列表功能
   list_display = ['code','email','send_type','send_time']
   #在xadmin后台的搜索功能
   search_fields = ['code','email','send_type']
   #在xadmin后台的过滤器功能
   list_filter = ['code','email','send_type','send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time']
    # 在xadmin后台的搜索功能
    search_fields = ['title', 'image', 'url', 'index']
    # 在xadmin后台的过滤器功能
    list_filter = ['title', 'image', 'url', 'index','add_time']


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
