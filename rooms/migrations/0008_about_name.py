# Generated by Django 2.2 on 2020-08-19 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_auto_20200815_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
