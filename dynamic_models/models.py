import os
from django.contrib import admin
import yaml
from django.db import models
from django.db.models import get_app, get_models, get_model
from django.conf import settings
import test_dm.settings as st
from django.forms.models import modelform_factory
from django.forms import ModelForm

FIELD_TYPES = {
    'char': models.CharField,
    'date': models.DateField,
    'int': models.IntegerField,
    }

def create_model(name, fields=None, app_label='', module='', options=None, admin_opts=None):

    class Meta:
        pass

    if app_label:
        setattr(Meta, 'app_label', app_label)

    if options is not None:
        for key, value in options.iteritems():
            setattr(Meta, key, value)

    attrs = {'__module__': module, 'Meta': Meta}

    if fields:
        attrs.update(fields)

    model = type(name, (models.Model,), attrs)

    if admin_opts is not None:
        class Admin(admin.ModelAdmin):
            pass
        for key, value in admin_opts:
            setattr(Admin, key, value)
        admin.site.register(model, Admin)

    return model

dict = yaml.load(open(st.rel('data.yml'), "r").read())
for model in dict:
    fields = {}
    for field in dict[model]['fields']:
        fields[field['id']] = FIELD_TYPES[field['type']](verbose_name = field['title'], max_length = '255')

    create_model(model,fields=fields,app_label= 'dynamic_models',admin_opts = {},
        options ={'verbose_name_plural': dict[model]['title'],},
    )
    #modelform_factory('Users')
