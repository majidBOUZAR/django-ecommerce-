# Generated by Django 4.0.3 on 2022-05-29 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateField(auto_created=True, auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='app/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateField(auto_created=True, auto_now=True)),
                ('comment_name', models.CharField(max_length=30, null=True)),
                ('comment_mail', models.CharField(max_length=30, null=True)),
                ('image', models.ImageField(null=True, upload_to='app/images/')),
                ('comment', models.TextField(max_length=5000)),
                ('status', models.CharField(blank=True, choices=[('Live', 'Live'), ('Stop', 'Stop')], max_length=50, null=True)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog')),
            ],
        ),
    ]