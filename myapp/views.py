from django.shortcuts import render
from .resources import PersonResource
from django.db.models import Q
from django import forms
from tablib import Dataset
from .models import *
# Create your views here.



class UploadFileForm(forms.Form):
    file = forms.FileField()
#diaplay view
def index(request):
  title = "Bienvenue"
  liste_electeurs = ListeElecteur.objects.all()
  queryset_list = ListeElecteur.objects.all()
  mes_electeurs = MonElecteur.objects.all()
  #queryset_list = Listing.objects.order_by('-list_date')

  #q
  if 'q' in request.GET:
      q = request.GET['q']
      print("q == ", q)
      queryset_list = queryset_list.filter(numero_electeur__iexact=q)
  context = {
    'title': title,
    'liste_electeurs':liste_electeurs,
    'mes_electeurs': mes_electeurs,
    'queryset_list':queryset_list,
  }
  return render(request, "myapp/index.html", context)

# search view 
def search(request):
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:            
            results = ListeElecteur.objects.filter(  
            	Q( numero_electeur__iexact = q ) |
                Q( nom__contains = q ) )          
            return render(request, 'myapp/results.html', {'results': results})


def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'import.html')