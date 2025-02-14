# Generated by Django 5.0.3 on 2024-04-03 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'blog',
            },
        ),
    ]
