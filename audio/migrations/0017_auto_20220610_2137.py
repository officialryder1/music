# Generated by Django 2.1.5 on 2022-06-10 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0016_auto_20220610_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='song',
        ),
        migrations.RemoveField(
            model_name='like',
            name='value',
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='post', to='audio.Song'),
            preserve_default=False,
        ),
    ]
