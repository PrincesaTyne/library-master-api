# Generated by Django 4.0.6 on 2024-04-01 10:36

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=22, primary_key=True, serialize=False),
        ),
    ]
