# Generated by Django 2.1.5 on 2019-01-28 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoTBL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accion', models.CharField(max_length=40)),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]