# Generated by Django 2.2.7 on 2020-01-26 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cciApp', '0004_blog_heading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
