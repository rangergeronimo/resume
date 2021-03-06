# Generated by Django 2.2.5 on 2019-10-19 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20191019_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employmenthistory',
            name='skill1',
        ),
        migrations.RemoveField(
            model_name='employmenthistory',
            name='skill2',
        ),
        migrations.RemoveField(
            model_name='employmenthistory',
            name='skill3',
        ),
        migrations.RemoveField(
            model_name='employmenthistory',
            name='skill4',
        ),
        migrations.RemoveField(
            model_name='employmenthistory',
            name='skill5',
        ),
        migrations.RemoveField(
            model_name='employmenthistory',
            name='skill6',
        ),
        migrations.RemoveField(
            model_name='employmenthistory',
            name='skill7',
        ),
        migrations.RemoveField(
            model_name='employmenthistory',
            name='skill8',
        ),
        migrations.RemoveField(
            model_name='employmenthistory',
            name='skill9',
        ),
        migrations.AddField(
            model_name='employmenthistory',
            name='github',
            field=models.URLField(default='https://github.com/KonicalRG'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employmenthistory',
            name='linkedin',
            field=models.URLField(default='www.linkedin.com/in/rangergeronimo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employmenthistory',
            name='skype',
            field=models.CharField(default='rangergeronimo', max_length=50),
            preserve_default=False,
        ),
    ]
