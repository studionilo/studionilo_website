# Generated by Django 3.0.3 on 2020-02-24 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200224_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='id',
            field=models.AutoField(auto_created=True, default=999999, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='paymentIntent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.PaymentIntent'),
        ),
    ]
