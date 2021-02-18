# Generated by Django 3.1.5 on 2021-02-11 04:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Order', '0003_auto_20210211_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderItem', related_query_name='orderItem', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
