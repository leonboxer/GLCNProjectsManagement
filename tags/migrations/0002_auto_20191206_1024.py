# Generated by Django 3.0 on 2019-12-06 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]