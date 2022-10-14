# Generated by Django 4.0.3 on 2022-06-14 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('FL', 'Farine_Semoul'), ('P', 'Pates'), ('G', 'Gateaux'), ('S', 'Sucrerie'), ('OF', 'Graines'), ('L', 'Laitiers'), ('B', 'Boisson'), ('PFM', 'Produit_Fait_Maison'), ('CM', 'Compliment Alimentaire')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity1',
            field=models.CharField(choices=[('sold', 'sold'), ('available', 'available')], default='available', max_length=10),
        ),
    ]