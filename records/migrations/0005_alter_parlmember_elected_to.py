# Generated by Django 3.2 on 2021-09-05 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_auto_20210829_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parlmember',
            name='elected_to',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='records.domain'),
        ),
    ]
