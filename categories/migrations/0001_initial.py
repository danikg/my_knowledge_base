# Generated by Django 3.1 on 2020-08-21 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Category name')),
                ('description', models.TextField(blank=True, verbose_name='Category description')),
                ('slug', models.SlugField(editable=False, max_length=255)),
                ('icon', models.ImageField(blank=True, upload_to=utils.get_upload_path, verbose_name='Category icon')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'categories',
                'ordering': ['name'],
            },
        ),
    ]
