# Generated by Django 2.1.5 on 2022-06-09 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0007_remove_song_genre_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='genre')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audio.Song')),
            ],
        ),
    ]
