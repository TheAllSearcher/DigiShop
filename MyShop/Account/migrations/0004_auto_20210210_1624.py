# Generated by Django 3.1.5 on 2021-02-10 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_auto_20210113_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user/image/', verbose_name='Image'),
        ),
    ]
