# Generated by Django 2.1 on 2018-10-04 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20181004_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='identificacion',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]