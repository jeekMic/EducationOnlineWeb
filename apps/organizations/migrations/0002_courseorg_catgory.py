# Generated by Django 2.1.7 on 2019-03-23 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='catgory',
            field=models.CharField(choices=[('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高笑')], default='pxjg', max_length=20, verbose_name='机构类别'),
        ),
    ]
