# Generated by Django 2.2.7 on 2020-01-26 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cciApp', '0003_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='heading',
            field=models.CharField(default='asdasd', max_length=100),
            preserve_default=False,
        ),
    ]
