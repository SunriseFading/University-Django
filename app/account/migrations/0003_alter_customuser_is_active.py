# Generated by Django 4.1.5 on 2023-01-20 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("account", "0002_alter_customuser_gender")]

    operations = [
        migrations.AlterField(model_name="customuser", name="is_active", field=models.BooleanField(default=True))
    ]
