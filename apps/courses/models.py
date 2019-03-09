from datetime import datetime

from django.db import models


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="课程名称")
    desc = models.CharField(max_length=300, verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情")
    degree = models.CharField(verbose_name="等级", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=6)
    learn_times = models.IntegerField(default=0, verbose_name="学习时长")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name="封面")
    click_nums = models.IntegerField(default=0, verbose_name="课程点击量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}".format(self.name)

class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="章节名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name
    def __str__(self):
        return "{0}".format(self.course)


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="章节", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="视频名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="视频名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name="资源文件", max_length=100)

    class Meta:
        verbose_name = "资源"
        verbose_name_plural = verbose_name
