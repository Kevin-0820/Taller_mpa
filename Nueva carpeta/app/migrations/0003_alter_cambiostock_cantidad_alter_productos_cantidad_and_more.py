# Generated by Django 5.0.4 on 2024-05-05 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_productos_id_cambiostock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cambiostock',
            name='cantidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='productos',
            name='Cantidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='productos',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
