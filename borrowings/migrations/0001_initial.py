# Generated by Django 4.0.6 on 2024-04-01 08:29

from django.db import migrations, models
import django.db.models.deletion
import shortuuid.main


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=256, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=256, null=True)),
                ('deleted_by', models.CharField(blank=True, max_length=256, null=True)),
                ('id', models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=20, primary_key=True, serialize=False)),
                ('deleted', models.BooleanField(default=False)),
                ('borrow_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
