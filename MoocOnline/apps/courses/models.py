# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField
from organization.models import CourseOrg, Teacher

# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)
    teacher = models.ForeignKey(Teacher, verbose_name=u"讲师", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"课程名称")
    category = models.CharField(max_length=20, default=u"", verbose_name=u"课程类别")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = UEditorField(u'内容	', width=600, height=300, imagePath="courses/ueditor/", filePath="courses/ueditor/",
                          default="")
    is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")
    degree = models.CharField(verbose_name='难度',  choices=(("cj", u"初级"), ("zj", u"中级"), ("gj", u"高级")), max_length=2)
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击量")
    tag = models.CharField(default=u"", verbose_name=u"课程标签", max_length=10)
    youneed_know = models.CharField(max_length=300, verbose_name=u"课程须知", default=u"")
    teacher_tell = models.CharField(max_length=300, verbose_name=u"课程能学到什么", default=u"")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        """
         获取章节数
        """
        return self.lesson_set.all().count()
    get_zj_nums.short_description = "章节数"

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='http://www.baidu.com'>跳转</a>")
    go_to.short_description = "跳转"

    def get_learn_users(self):
        """
        获取该课程的学习用户，这里取了5个
        """
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        """
        获取课程所有章节
        """
        return self.lesson_set.all()

    def __str__(self):
        return self.name


class BannerCourse(Course):
    class Meta:
        verbose_name = "轮播课程"
        verbose_name_plural = verbose_name
        # 设置proxy = True，不会再生成一张表，方便一个Course注册两个管理器
        proxy = True


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def get_lesson_video(self):
        """
        获取章节视频
        """
        return self.video_set.all()

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    url = models.CharField(max_length=200, default=u"", verbose_name=u"访问地址")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
