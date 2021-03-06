# Generated by Django 2.1.5 on 2022-06-10 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0009_auto_20220609_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='download',
            field=models.FileField(default='', upload_to='Music_download'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(upload_to='image'),
        ),
    ]
