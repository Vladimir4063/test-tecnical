# Generated by Django 2.0 on 2023-12-19 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_auto_20231219_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redirect',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
