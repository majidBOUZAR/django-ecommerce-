# Generated by Django 4.0.3 on 2022-05-31 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_rename_category_blog_categorie_remove_blog_slug_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='categorie',
            new_name='category',
        ),
    ]