# Generated by Django 3.2.14 on 2022-08-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20220817_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='certificates',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='guide',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='guide',
            name='nationality',
            field=models.CharField(max_length=254),
        ),
    ]
