# Generated by Django 3.1.5 on 2021-02-11 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_auto_20210210_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='count',
            field=models.IntegerField(default=1, verbose_name='count'),
        ),
    ]
