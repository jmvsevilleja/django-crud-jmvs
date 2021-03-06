# Generated by Django 2.1.8 on 2020-01-21 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('suburb', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
    ]
