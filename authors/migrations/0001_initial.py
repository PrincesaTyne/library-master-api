# Generated by Django 4.0.6 on 2024-04-01 08:29

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=256, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=256, null=True)),
                ('deleted_by', models.CharField(blank=True, max_length=256, null=True)),
                ('id', models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=20, primary_key=True, serialize=False)),
                ('deleted', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
