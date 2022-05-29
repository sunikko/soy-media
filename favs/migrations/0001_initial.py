# Generated by Django 2.2.5 on 2022-05-23 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('books', models.ManyToManyField(related_name='fav_lists', to='books.Book')),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fav_lists', to=settings.AUTH_USER_MODEL)),
                ('movies', models.ManyToManyField(related_name='fav_lists', to='movies.Movie')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]