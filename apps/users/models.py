# _*_ coding:utf-8 _*_
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name="昵称",default="")
    birday = models .DateTimeField(verbose_name= "生日", null = True, blank=True)
    gender = models.CharField(choices =(("male","男"),("female","女")), default="female", max_length=7)
    address = models.CharField(max_length=100, default= "")
    mobile = models.CharField(max_length=11, null = True,blank=True)
    image = models.ImageField(upload_to="image/%Y/%m",default="image/default.png",max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(verbose_name= "验证码类型", choices=(("register","注册"),("forget","找回密码")),max_length=10)
    send_time = models.DateTimeField(verbose_name= "发送时间", default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    #def __unicode__(self):
    def __str__(self):
        return '{0}({1})'.format(self.code,self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name="标题")
    image = models.ImageField(upload_to="banner/%Y/%m", max_length=100,verbose_name="轮播图",)
    url = models.URLField(max_length=200,verbose_name="访问地址")
    index = models.IntegerField(default=100,verbose_name="顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name
