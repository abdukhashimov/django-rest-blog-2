# Generated by Django 3.0.3 on 2020-02-10 12:28

from django.db import migrations, models
import post.validators.validate_name
import post.validators.validate_title


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200209_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, validators=[post.validators.validate_name.validate_name]),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, validators=[post.validators.validate_title.validate_title]),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, validators=[post.validators.validate_name.validate_name]),
        ),
    ]
