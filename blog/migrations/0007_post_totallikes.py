# Generated by Django 3.1.5 on 2021-04-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='totallikes',
            field=models.IntegerField(default=0),
        ),
    ]
