from datetime import datetime
from django.db import models

# Create your models here.

class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name="城市")
    desc = models.CharField(max_length=200, verbose_name="描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name="机构名称")
    desc = models.TextField(verbose_name="机构描述")
    catgory = models.CharField(default="pxjg", verbose_name ="机构类别",max_length=20,choices=(("pxjg", "培训机构"), ("gr", "个人"), ("gx", "高笑")))
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_name= models.IntegerField(default=0, verbose_name="收藏数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="封面图")
    address = models.CharField(max_length=100, verbose_name="机构地址")
    city = models.ForeignKey(CityDict,verbose_name="所在城市",on_delete= models.CASCADE)

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,verbose_name="所属机构",on_delete= models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="教师名称")
    work_year= models.IntegerField(default=0,verbose_name="教学年限")
    work_company = models.CharField(max_length=50, verbose_name="就职公司")
    work_position = models.CharField(max_length=50,verbose_name="公司职位")
    points = models.CharField(max_length=50, verbose_name="教学特点")
    click_nums = models.IntegerField(default=0, verbose_name="收藏数")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name