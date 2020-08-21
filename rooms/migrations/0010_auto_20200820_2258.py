# Generated by Django 2.2 on 2020-08-21 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0009_localguest'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToursitBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('image1', models.ImageField(upload_to='blog')),
                ('image2', models.ImageField(upload_to='blog')),
                ('image3', models.ImageField(upload_to='blog')),
            ],
        ),
        migrations.AlterField(
            model_name='localguest',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
