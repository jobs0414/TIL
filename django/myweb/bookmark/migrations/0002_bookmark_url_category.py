# Generated by Django 2.1.2 on 2018-10-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='url_category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]