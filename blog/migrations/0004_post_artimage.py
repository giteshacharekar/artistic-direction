# Generated by Django 3.1.5 on 2021-04-17 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_artcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='artimage',
            field=models.TextField(default=''),
        ),
    ]