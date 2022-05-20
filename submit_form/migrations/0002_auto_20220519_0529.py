# Generated by Django 3.1.6 on 2022-05-19 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submit_form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Form',
        ),
    ]