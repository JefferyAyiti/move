# Generated by Django 3.2 on 2021-08-23 21:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20210808_1908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ('act_name', 'status'), 'verbose_name': 'Activity', 'verbose_name_plural': 'Activities'},
        ),
        migrations.AlterModelOptions(
            name='domain',
            options={'ordering': ('region', 'constituency'), 'verbose_name': 'Domain', 'verbose_name_plural': 'Domains'},
        ),
        migrations.AlterModelOptions(
            name='minister',
            options={'ordering': ('rank', 'last_name', 'first_name'), 'verbose_name': 'Minister', 'verbose_name_plural': 'Ministers'},
        ),
        migrations.AlterModelOptions(
            name='ministry',
            options={'ordering': ('name', 'est'), 'verbose_name': 'Ministry', 'verbose_name_plural': 'Ministries'},
        ),
        migrations.AlterModelOptions(
            name='parlmember',
            options={'ordering': ('last_name', 'first_name', 'elected_to'), 'verbose_name': 'MP', 'verbose_name_plural': 'MPs'},
        ),
        migrations.AlterModelOptions(
            name='party',
            options={'ordering': ('est',), 'verbose_name': 'Party', 'verbose_name_plural': 'Parties'},
        ),
        migrations.AddField(
            model_name='parlmember',
            name='party',
            field=models.ForeignKey(default='NPP', on_delete=django.db.models.deletion.PROTECT, to='records.party'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='constituency',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='domain',
            name='district',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='domain',
            name='region',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='minister',
            name='appoint_year',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='YearOfAppointment'),
        ),
        migrations.AlterField(
            model_name='ministry',
            name='est',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='ministry',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='parlmember',
            name='no_terms',
            field=models.PositiveIntegerField(),
        ),
    ]
