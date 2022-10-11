# Generated by Django 4.0.4 on 2022-10-11 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
        ('historical_data', '0002_pricehistory_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricehistory',
            name='wallet',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='wallet_user', to='wallet.wallet'),
            preserve_default=False,
        ),
    ]