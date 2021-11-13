# Generated by Django 3.2.9 on 2021-11-11 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='post_tags', to='blog_api.tags'),
        ),
    ]
