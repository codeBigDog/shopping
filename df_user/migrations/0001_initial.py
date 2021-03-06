# Generated by Django 2.1.1 on 2018-09-25 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=32)),
                ('harvestName', models.CharField(default='', max_length=32)),
                ('address', models.CharField(default='', max_length=255)),
                ('phone', models.CharField(default='', max_length=32)),
            ],
        ),
    ]
