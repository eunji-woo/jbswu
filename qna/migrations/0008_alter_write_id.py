# Generated by Django 3.2.6 on 2021-08-27 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0007_auto_20210827_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='write',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
