# Generated by Django 2.2.4 on 2019-08-12 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connexion', '0008_competence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competence',
            name='competence',
            field=models.CharField(max_length=128),
        ),
    ]
