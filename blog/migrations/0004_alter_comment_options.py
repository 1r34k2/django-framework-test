# Generated by Django 4.1.3 on 2022-11-17 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_comment_blog_commen_created_0e6ed4_idx'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created']},
        ),
    ]
