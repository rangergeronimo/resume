# Generated by Django 2.2.5 on 2019-11-01 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_auto_20191020_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='employmenthistory',
            name='achievements',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employmenthistory',
            name='main_role',
            field=models.TextField(blank=True, null=True),
        ),
    ]
