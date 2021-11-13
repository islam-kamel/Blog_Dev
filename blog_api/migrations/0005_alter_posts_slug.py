# Generated by Django 3.2.9 on 2021-11-11 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0004_alter_posts_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=models.SlugField(blank=True, default=models.CharField(max_length=250), editable=False, max_length=150, unique_for_date='created_data'),
        ),
    ]
