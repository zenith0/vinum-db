# Generated by Django 2.1.3 on 2018-11-15 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('slug', models.SlugField(max_length=40)),
                ('grower', models.CharField(max_length=200)),
                ('year', models.IntegerField(blank=True, default=0, null=True)),
                ('color', models.CharField(choices=[('red', 'Rot'), ('white', 'Weiß'), ('rose', 'Rose')], max_length=5)),
                ('front_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('back_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=500, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('provine', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
