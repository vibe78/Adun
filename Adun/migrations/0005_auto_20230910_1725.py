# Generated by Django 2.2.6 on 2023-09-10 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adun', '0004_auto_20230910_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffregistration',
            name='comfirm_password',
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='staffregistration',
            name='password',
            field=models.CharField(max_length=900, null=True),
        ),
    ]
