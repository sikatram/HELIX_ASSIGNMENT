# Generated by Django 4.1.6 on 2023-02-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_rename_text_question_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(max_length=1000),
        ),
    ]
