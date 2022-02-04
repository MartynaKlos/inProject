# Generated by Django 4.0.2 on 2022-02-04 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('occupation', models.CharField(max_length=250)),
                ('photo', models.ImageField(null=True, upload_to='photos/', verbose_name='Photo')),
            ],
        ),
    ]
