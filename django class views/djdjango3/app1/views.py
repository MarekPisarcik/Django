from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.

def pozdrav_meno(request):
    meno = request.GET.get('meno', 'nezname meno')

    return HttpResponse(f'Tvoje meno je {meno}')

def vyber_kategoriu(request):
    kategorie = ['Filmy', 'Knihy', 'Hry']
    vybrana = None

    if request.method == 'POST':
        vybrana = request.POST.get('kategoria')

    context = {
        'kategorie': kategorie,
        'vybrana': vybrana,
    }
    return render(request, 'kategoria.html', context)
