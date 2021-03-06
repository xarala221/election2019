from django.shortcuts import render, redirect
from .resources import PersonResource
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.utils.http import is_safe_url
from .models import *
from .forms import LoginForm

User = get_user_model()
def sign_in(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['profile'] = User.objects.count()
            print('sesssion begin')
            # print(request.session['profile'])
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect('/')
    else:
        print("Error 3")
    return render(request, "auth/login.html", context)

def log_out(request):
    if 'profil' in request.session:
        del request.session['profil']

    logout(request)
    return redirect('/sign_in/')
# def home(request):
#     form = LoginForm(request.POST or None)
#     context = {
#         'form': form
#     }
#     next_ = request.GET.get('next')
#     next_post = request.POST.get('next')
#     redirect_path = next_ or next_post
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             request.session['profile'] = User.objects.count()
#             print('sesssion begin')
#             # print(request.session['profile'])
#         if is_safe_url(redirect_path, request.get_host()):
#             return redirect(redirect_path)
#         else:
#             return redirect('/homepage/')
#     else:
#         print("Error 3")

#     # try:
#     #     if request.user.is_authenticated:
#     #         return HttpResponseRedirect("/home/")
#     # except Exception as e:
#     #     print("Exception {}".format(e))
#     return render(request, 'auth/login.html', context)


@login_required(login_url='/sign_in/')
def homepage(request):
    total = MonElecteur.objects.all().count()
    print("Total ", total)
    dakar = MonElecteur.objects.filter(region="Dakar").count()
    print("dakar ", dakar)
    diourbel = MonElecteur.objects.filter(region="Diourbel").count()
    print("Diourbel ", diourbel)
    fatick = MonElecteur.objects.filter(region="Fatick").count()
    print("Fatick ", fatick)
    kaffrine = MonElecteur.objects.filter(region="Kaffrine").count()
    print("Kaffrine ", kaffrine)
    kaolack = MonElecteur.objects.filter(region="Kaolack").count()
    print("kaolack ", kaolack)
    kedougou = MonElecteur.objects.filter(region="Kédougou").count()
    print("kedougou ", kedougou)
    matam = MonElecteur.objects.filter(region="Matam").count()
    print("Matam ", matam)
    saint_louis = MonElecteur.objects.filter(region="Saint-Louis").count()
    print("saint_louis ", saint_louis)
    sedhiou = MonElecteur.objects.filter(region="Sédhiou").count()
    print("Sédhiou ", sedhiou)
    tambacounda = MonElecteur.objects.filter(region="Tambacounda").count()
    print("Tambacounda ", tambacounda)
    thies = MonElecteur.objects.filter(region="Thiès").count()
    print("thies ", thies)
    ziguinchor = MonElecteur.objects.filter(region="Ziguinchor").count()
    print("Ziguinchor ", ziguinchor)
    kolda = MonElecteur.objects.filter(region="Kolda").count()
    print("Kolda ", kolda)
    louga = MonElecteur.objects.filter(region="Louga").count()
    print("Louga ", louga)
    context = {
        'dakar':dakar,
        'diourbel':diourbel,
        'fatick':fatick,
        'kaffrine':kaffrine,
        'kaolack':kaolack,
        'kedougou':kedougou,
        'matam':matam,
        'saint_louis':saint_louis,
        'sedhiou':sedhiou,
        'tambacounda':tambacounda,
        'thies':thies,
        'ziguinchor':ziguinchor,
        'kolda':kolda,
        'louga':louga,
        'total':total


    }
    return render(request, "dashboard/index.html", context)

#diaplay view
def index(request):
    title = "Bienvenue"
    total = MonElecteur.objects.all().count()
    print("Total ", total)
    dakar = MonElecteur.objects.filter(region="Dakar").count()
    print("dakar ", dakar)
    diourbel = MonElecteur.objects.filter(region="Diourbel").count()
    print("Diourbel ", diourbel)
    fatick = MonElecteur.objects.filter(region="Fatick").count()
    print("Fatick ", fatick)
    kaffrine = MonElecteur.objects.filter(region="Kaffrine").count()
    print("Kaffrine ", kaffrine)
    kaolack = MonElecteur.objects.filter(region="Kaolack").count()
    print("kaolack ", kaolack)
    kedougou = MonElecteur.objects.filter(region="Kédougou").count()
    print("kedougou ", kedougou)
    matam = MonElecteur.objects.filter(region="Matam").count()
    print("Matam ", matam)
    saint_louis = MonElecteur.objects.filter(region="Saint-Louis").count()
    print("saint_louis ", saint_louis)
    sedhiou = MonElecteur.objects.filter(region="Sédhiou").count()
    print("Sédhiou ", sedhiou)
    tambacounda = MonElecteur.objects.filter(region="Tambacounda").count()
    print("Tambacounda ", tambacounda)
    thies = MonElecteur.objects.filter(region="Thiès").count()
    print("thies ", thies)
    ziguinchor = MonElecteur.objects.filter(region="Ziguinchor").count()
    print("Ziguinchor ", ziguinchor)
    kolda = MonElecteur.objects.filter(region="Kolda").count()
    print("Kolda ", kolda)
    louga = MonElecteur.objects.filter(region="Louga").count()
    print("Louga ", louga)
    liste_electeurs = ListeElecteur.objects.all()
    context = {
        'title': title,
        'liste_electeurs':liste_electeurs,
        'total':total,
         'dakar':dakar,
        'diourbel':diourbel,
        'fatick':fatick,
        'kaffrine':kaffrine,
        'kaolack':kaolack,
        'kedougou':kedougou,
        'matam':matam,
        'saint_louis':saint_louis,
        'sedhiou':sedhiou,
        'tambacounda':tambacounda,
        'thies':thies,
        'ziguinchor':ziguinchor,
        'kolda':kolda,
        'louga':louga
    }
    return render(request, "myapp/index.html", context)

# search view 
def search(request):
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:            
            results = ListeElecteur.objects.filter(  
            	Q( numero_electeur__iexact = q ) |
                Q( numero_identite__iexact = q ) )  
            print("q", q)
            print("resula", results)        
            return render(request, 'myapp/results.html', {'results': results})

def mon_electeur(request):
  
    keyword = request.POST.get('keyword')

    data = []
    try:
        electeur = ListeElecteur.objects.get(numero_electeur=keyword)
        electeurs = ListeElecteur.objects.filter(numero_electeur=electeur)
        print("electeur ", electeurs)
        data = serializers.serialize('json', [electeurs])

        print("data , data", data)

    except Exception as e:
        print(e)

    return JsonResponse(data,safe=False)

def get_person_info(request):
    person_id = request.GET.get('person_id')
    data = []
    try:
        electeur = ListeElecteur.objects.get(pk=person_id)
        data = serializers.serialize('json', [electeur])
        print("data", data)
    except Exception as e:
        print(e)

    return JsonResponse(data,safe=False)

def create_person(request):
    values = {'error':'','has_error':0,}
    values['numero_electeur'] = request.POST.get('numero_electeur')
    values['numero_identite'] = request.POST.get('numero_identite')
    values['nom'] = request.POST.get('nom')
    values['prenom'] = request.POST.get('prenom')
    values['region'] = request.POST.get('region')
    # values['sex'] = request.POST.get('sex')
    # values['type_client'] = request.POST.get('type_client')
    # values['address'] = request.POST.get('address')

    try:
            #if len(values['first_name']) > 0 and len(values['last_name']) > 0  and len(values['phone']) > 0 and len(values['email']) > 0 and len(values['address']) > 0:

            electeur = MonElecteur.objects.create(
                nom=values['nom'],
                prenom=values['prenom'],
                numero_electeur=values['numero_electeur'],
                numero_identite=values['numero_identite'],
                region=values['region'],
                )
            electeur.save()
            #return redirect('/all_clients/')
            #values['clientId'] = client.id
            return JsonResponse(values)
            #else:
            #    values['error'] =  "Veuillez remplir tous les champs"
            #    values['has_error'] =  -1

    except Exception as e:
        values['error'] =  e
        values['has_error'] =  -1

        print("erreur ", e)

    return JsonResponse(values)

