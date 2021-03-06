# Generated by Django 2.1.5 on 2022-06-09 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='songs')),
                ('description', models.TextField()),
                ('genre', models.CharField(choices=[('GOSPEL', 'GOSPEL'), ('AFROBEATS', 'AFROBEATS'), ('RAP&HIP-HOP', 'RAP&HIP-HOP'), ('COUNTRY', 'COUNTRY'), ('POP', 'POP'), ('REGGE', 'REGGE')], max_length=15)),
                ('year_release', models.IntegerField()),
                ('date_upload', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
