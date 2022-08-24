# Generated by Django 4.1 on 2022-08-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_article_subtitle_alter_article_descriptor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='secondary_descriptor',
            field=models.CharField(blank=True, choices=[('world affairs', 'World Affairs')], max_length=20),
        ),
    ]