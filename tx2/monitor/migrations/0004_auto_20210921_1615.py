# Generated by Django 3.2.7 on 2021-09-21 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_alter_segmentationimage_seg_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detectionimage',
            name='det_img',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='originalimage',
            name='org_img',
            field=models.ImageField(upload_to='media/'),
        ),
    ]