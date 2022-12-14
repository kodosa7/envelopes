# Generated by Django 3.0.2 on 2020-01-24 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senderTitle', models.CharField(max_length=10, verbose_name='Sender Title')),
                ('senderName', models.CharField(max_length=40, verbose_name='Sender Name')),
                ('senderAddress', models.CharField(max_length=40, verbose_name='Sender Address')),
                ('senderCity', models.CharField(max_length=40, verbose_name='Sender City')),
                ('senderProvince', models.CharField(max_length=40, verbose_name='Sender Province')),
                ('senderCountry', models.CharField(max_length=40, verbose_name='Sender Country')),
                ('senderZip', models.CharField(max_length=40, verbose_name='Sender ZIP/postal code')),
                ('receiverTitle', models.CharField(max_length=10, verbose_name='Sender Title')),
                ('receiverName', models.CharField(max_length=40, verbose_name='Sender Name')),
                ('receiverAddress', models.CharField(max_length=40, verbose_name='Sender Address')),
                ('receiverCity', models.CharField(max_length=40, verbose_name='Sender City')),
                ('receiverProvince', models.CharField(max_length=40, verbose_name='Sender Province')),
                ('receiverrCountry', models.CharField(max_length=40, verbose_name='Sender Country')),
                ('receiverZip', models.CharField(max_length=40, verbose_name='Sender ZIP/postal code')),
            ],
        ),
    ]
