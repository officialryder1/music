# Generated by Django 2.1.5 on 2022-06-09 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0005_auto_20220609_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre_img',
            field=models.FileField(default='', upload_to='genre'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.FileField(upload_to='image'),
        ),
    ]
