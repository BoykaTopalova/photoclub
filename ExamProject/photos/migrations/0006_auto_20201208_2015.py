# Generated by Django 3.1.4 on 2020-12-08 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_auto_20201208_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='image',
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(default='', upload_to='photos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]