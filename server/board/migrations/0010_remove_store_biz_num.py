# Generated by Django 3.2.6 on 2021-10-20 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_alter_tag_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='biz_num',
        ),
    ]
