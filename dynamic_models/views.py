from django.views.generic.simple import direct_to_template
from django.db.models import get_app, get_models, get_model
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.forms import ModelForm
from django.forms.models import modelform_factory
from django.forms import ModelForm, Textarea, TextInput,HiddenInput

def index(request,app):
    if request.is_ajax():
        model = get_model(app, request.GET.get('model'))
        for field in model._meta.fields:
            if field.get_internal_type()=='DateField':
                wdg={field.get_attname(): TextInput(attrs={'class': 'datepicker1'})}
            else:
                wdg=None
        form=modelform_factory(model,widgets=wdg)#{'date_joined': TextInput(attrs={'class': 'datepicker1'})})
        id=None
        f = form(request.POST or None,request.FILES or None,instance=id and model.objects.get(id=id))
        if request.method == 'POST' and f.is_valid() :
            f.save()
        data=[]
        data = model.objects.all().values_list()
        fields = [field.verbose_name for field in model._meta.fields]
        html = render_to_string('table.html', {'data': data,'fields':fields,'form':form,'model':model,'modelnm':model.__name__})
        return HttpResponse(html)
    else:
        list_models = []
        for model in get_models(get_app(app)):
            list_models.append([model.__name__, model._meta.verbose_name_plural])
        return direct_to_template(request, 'index.html', {'models': list_models,})