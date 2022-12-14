# Generated by Django 4.0.4 on 2022-10-11 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_account_datetime_create_account_friends_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('wallet_id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='wallet')),
                ('link_account', models.TextField(default='[]')),
                ('balance', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('volume', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('datetime_create', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_wallet', to='account.account')),
            ],
        ),
    ]
