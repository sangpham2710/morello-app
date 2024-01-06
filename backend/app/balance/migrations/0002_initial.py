# Generated by Django 4.1 on 2024-01-05 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('balance', '0001_initial'),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='balanceentry',
            name='group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balance_entries', to='group.group'),
        ),
    ]
