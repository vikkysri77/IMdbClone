# Generated by Django 4.0.3 on 2022-04-12 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoldenTicket', '0003_movie_delete_movies'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_poster',
            field=models.ImageField(blank=True, default='../static/default_avatar.png', upload_to='images'),
        ),
    ]
