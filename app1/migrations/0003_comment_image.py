# Generated by Django 4.0.6 on 2023-05-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
