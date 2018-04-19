# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-04 11:33
from __future__ import unicode_literals

from django.db import migrations

SWITCH = 'use_company_name_as_utm_source_value'


def create_switch(apps, schema_editor):
    """Create the use_company_name_as_utm_source_value switch."""
    Switch = apps.get_model('waffle', 'Switch')
    Switch.objects.get_or_create(name=SWITCH, defaults={'active': False})


def delete_switch(apps, schema_editor):
    """Delete the use_company_name_as_utm_source_value switch."""
    Switch = apps.get_model('waffle', 'Switch')
    Switch.objects.filter(name=SWITCH).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_partner_lms_url'),
        ('waffle', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_switch, reverse_code=delete_switch),
    ]
