# Generated by Django 4.1 on 2022-08-24 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_topic_alter_article_secondary_descriptor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(max_length=500, upload_to=''),
        ),
    ]
