# Generated by Django 2.2.7 on 2019-12-03 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_auto_20191203_1505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sectionrecord',
            old_name='question',
            new_name='section_question',
        ),
    ]