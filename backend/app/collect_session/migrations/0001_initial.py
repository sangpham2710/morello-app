# Generated by Django 4.1 on 2023-12-16 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollectSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('due', models.DateTimeField()),
                ('description', models.CharField(max_length=255)),
                ('is_open', models.BooleanField(default=True)),
            ],
        ),
    ]