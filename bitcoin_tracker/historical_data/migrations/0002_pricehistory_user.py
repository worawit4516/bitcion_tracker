# Generated by Django 4.0.4 on 2022-10-05 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('historical_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricehistory',
            name='user',
            field=models.ForeignKey(default=20, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='account.account'),
            preserve_default=False,
        ),
    ]
