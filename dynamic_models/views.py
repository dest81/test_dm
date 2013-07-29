from django.views.generic.simple import direct_to_template
from django.db.models import get_app, get_models, get_model
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.forms import ModelForm
from django.forms.models import modelform_factory
modelforms = ModelForm.__subclasses__()


def get_modelform(model):
    return filter(lambda x:x.Meta.model == model, modelforms)[0]

def index(request,app):
    if request.is_ajax():
        model = get_model(app, request.GET.get('model'))
        data=[]
        data = model.objects.all().values_list()
        fields = [field.verbose_name for field in model._meta.fields]
        #fm=get_modelform(model)
        #form = fm()
        form=modelform_factory(model)
        htmlcode = render_to_string('table.html', {'data': data,'fields':fields,'form':form})#,'form':form
        return HttpResponse(htmlcode)
    else:
        list_models = []
        for model in get_models(get_app(app)):
            list_models.append([model.__name__, model._meta.verbose_name_plural])
        return direct_to_template(request, 'index.html', {
            'models': list_models,
            })