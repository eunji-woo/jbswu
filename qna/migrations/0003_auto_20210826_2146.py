# Generated by Django 2.2.4 on 2021-08-26 12:46

from django.db import migrations, models
import qna.models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0002_delete_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='write',
            name='filename',
            field=models.CharField(max_length=64, null=True, verbose_name='첨부파일명'),
        ),
        migrations.AddField(
            model_name='write',
            name='upload_files',
            field=models.FileField(blank=True, null=True, upload_to=qna.models.get_file_path, verbose_name='파일'),
        ),
    ]
