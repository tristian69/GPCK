# Generated by Django 5.0.6 on 2024-09-26 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iils', '0003_answer_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
