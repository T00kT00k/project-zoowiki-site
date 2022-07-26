from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *


# Create your views here.

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'action_page'},
]

action_menu = [{'title': "Добавить новый класс", 'url_name': "create_classis"},
               {'title': "Добавить новый отряд", 'url_name': "create_ordo"},
               {'title': "Добавить новое семейство", 'url_name': "create_familia"},
               {'title': "Добавить новый род", 'url_name': "create_genus"},
               {'title': "Добавить новый вид", 'url_name': "create_species"},
]

backtomain = ["Вернуться на главную страницу"]

# Главная страница (показывает список постов о Классах животных)
def index(request):

    # Словарь
    context = {
        'menu': menu,
        'title': 'Главная страница',
        'classis_selected': 0,
    }
    return render(request, 'zoowikipedia/index.html', context=context)

# Страница с информацией о сайте
def about(request):
    # Словарь
    context = {
        'menu': menu,
        'title': 'О сайте',
    }
    return render(request, 'zoowikipedia/about.html', context=context)

# Страница выбора объекта для дальнейших действий
def actionPage(request):

    # Словарь
    context = {
        'menu': menu,
        'title': 'Выбор объекта',
        'action_menu': action_menu,
    }
    return render(request, 'zoowikipedia/action.html', context=context)

# Добавление информации о классе на сайт
def addClassis(request):
    if request.method == 'POST':
        form = AddClassisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddClassisForm()
    return render(request, 'zoowikipedia/create_classis.html', {'form': form, 'menu': menu, 'title': 'Добавление класса'})

# Добавление информации об отряде на сайт
def addOrdo(request):
    if request.method == 'POST':
        form = AddOrdoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddOrdoForm()
    return render(request, 'zoowikipedia/create_ordo.html', {'form': form, 'menu': menu, 'title': 'Добавление отряда'})

# Добавление информации о семействе на сайт
def addFamilia(request):
    if request.method == 'POST':
        form = AddFamiliaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddFamiliaForm()
    return render(request, 'zoowikipedia/create_familia.html', {'form': form, 'menu': menu, 'title': 'Добавление семейства'})

# Добавление информации о роде на сайт
def addGenus(request):
    if request.method == 'POST':
        form = AddGenusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddGenusForm()
    return render(request, 'zoowikipedia/create_genus.html', {'form': form, 'menu': menu, 'title': 'Добавление рода'})

# Добавление информации о виде на сайт
def addSpecies(request):
    if request.method == 'POST':
        form = AddSpeciesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddSpeciesForm()
    return render(request, 'zoowikipedia/create_species.html', {'form': form, 'menu': menu, 'title': 'Добавление вида'})


# Удаление поста о классе
def delClassis(request, id):
    try:
        form = Classis.objects.get(id=id)
        form.delete()
        return redirect('home')
    except Classis.DoesNotExist:
        return HttpResponseNotFound("<h2>Classis not found</h2>")

# Удаление поста об отряде
def delOrdo(request, id, classis_list_id):
    try:
        form = Ordo.objects.get(id=id)
        form.delete()
        return redirect('home')
    except Ordo.DoesNotExist:
        return HttpResponseNotFound("<h2>Ordo not found</h2>")

# Удаление поста о семействе
def delFamilia(request, id, ordo_list_id, classis_list_id):
    try:
        form = Familia.objects.get(id=id)
        form.delete()
        return redirect('home')
    except Familia.DoesNotExist:
        return HttpResponseNotFound("<h2>Familia not found</h2>")

# Удаление поста о роде
def delGenus(request, id, familia_list_id, ordo_list_id, classis_list_id):
    try:
        form = Genus.objects.get(id=id)
        form.delete()
        return redirect('home')
    except Genus.DoesNotExist:
        return HttpResponseNotFound("<h2>Genus not found</h2>")

# Удаление поста о виде
def delSpecies(request, id, genus_list_id, familia_list_id, ordo_list_id, classis_list_id):
    try:
        form = Species.objects.get(id=id)
        form.delete()
        return redirect('home')
    except Species.DoesNotExist:
        return HttpResponseNotFound("<h2>Species not found</h2>")

# Редактирование поста о классе
def editClassis(request, id):
    try:
        form = Classis.objects.get(id=id)
        if request.method == "POST":
            form = AddClassisForm(request.POST, instance=form)
            form.name = request.POST.get("name")
            form.info = request.POST.get("info")
            form.save()
            return redirect('home')
        else:
            form = AddClassisForm(instance=form)
            return render(request, "classis_edit.html", {'form': form})
    except Classis.DoesNotExist:
        return HttpResponseNotFound("<h2>Classis not found</h2>")

# Редактирование поста об отряде
def editOrdo(request, id, classis_list_id):
    try:
        form = Ordo.objects.get(id=id)
        if request.method == "POST":
            form = AddOrdoForm(request.POST, instance=form)
            form.name = request.POST.get("name")
            form.info = request.POST.get("info")
            form.classis = request.POST.get("classis")
            form.save()
            return redirect('home')
        else:
            form = AddOrdoForm(instance=form)
            return render(request, "ordo_edit.html", {'form': form})
    except Ordo.DoesNotExist:
        return HttpResponseNotFound("<h2>Ordo not found</h2>")

# Редактирование поста о семействе
def editFamilia(request, id, ordo_list_id, classis_list_id):
    try:
        form = Familia.objects.get(id=id)
        if request.method == "POST":
            form = AddFamiliaForm(request.POST, instance=form)
            form.name = request.POST.get("name")
            form.info = request.POST.get("info")
            form.ordo = request.POST.get("ordo")
            form.save()
            return redirect('home')
        else:
            form = AddFamiliaForm(instance=form)
            return render(request, "familia_edit.html", {'form': form})
    except Familia.DoesNotExist:
        return HttpResponseNotFound("<h2>Familia not found</h2>")

# Редактирование поста о роде
def editGenus(request, id, familia_list_id, ordo_list_id, classis_list_id):
    try:
        form = Genus.objects.get(id=id)
        if request.method == "POST":
            form = AddGenusForm(request.POST, instance=form)
            form.name = request.POST.get("name")
            form.info = request.POST.get("info")
            form.familia = request.POST.get("familia")
            form.save()
            return redirect('home')
        else:
            form = AddGenusForm(instance=form)
            return render(request, "genus_edit.html", {'form': form})
    except Genus.DoesNotExist:
        return HttpResponseNotFound("<h2>Genus not found</h2>")

# Редактирование поста о роде
def editSpecies(request, id, genus_list_id, familia_list_id, ordo_list_id, classis_list_id):
    try:
        form = Species.objects.get(id=id)
        if request.method == "POST":
            form = AddSpeciesForm(request.POST, instance=form)
            form.name = request.POST.get("name")
            form.info = request.POST.get("info")
            form.genus = request.POST.get("genus")
            form.save()
            return redirect('home')
        else:
            form = AddSpeciesForm(instance=form)
            return render(request, "species_edit.html", {'form': form})
    except Species.DoesNotExist:
        return HttpResponseNotFound("<h2>Species not found</h2>")

# Информационная страница "Страница не найдена"
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# Показывает пост о классе животных
def show_classis(request, classis_post_id):
    post = get_object_or_404(Classis, pk=classis_post_id)

    # Словарь
    context = {
        'post': post,
        'menu': menu,
        'title': post.name,
        'classis_selected': post.pk,
    }
    return render(request, 'zoowikipedia/classis_post.html', context=context)

# Список отрядов животных на главном экране
def list_ordo(request, classis_list_id):
    ordo = Ordo.objects.filter(classis_id=classis_list_id)

    context = {
        'ordo': ordo,
        'menu': menu,
        'title': 'Отображение по классам',
    }
    return render(request, 'zoowikipedia/list_ordo.html', context=context)

# Показывает пост об отряде животных
def show_ordo(request, ordo_post_id, classis_id):
    post = get_object_or_404(Ordo, pk=ordo_post_id)

    # Словарь
    context = {
        'post': post,
        'menu': menu,
        'title': post.name,
        'ordo_selected': post.pk,
    }
    return render(request, 'zoowikipedia/ordo_post.html', context=context)

# Список семейств животных на главном экране
def list_familia(request, ordo_list_id, classis_id):
    familia = Familia.objects.filter(ordo_id=ordo_list_id)

    context = {
        'familia': familia,
        'menu': menu,
        'title': 'Отображение по классам',
        'ordo_selected': ordo_list_id
    }
    return render(request, 'zoowikipedia/list_familia.html', context=context)

# Показывает пост о семействе животных
def show_familia(request, familia_post_id, ordo_id, classis_id):
    post = get_object_or_404(Familia, pk=familia_post_id)

    # Словарь
    context = {
        'post': post,
        'menu': menu,
        'title': post.name,
        'familia_selected': post.pk,
    }
    return render(request, 'zoowikipedia/familia_post.html', context=context)

# Список родов животных на главном экране
def list_genus(request, familia_list_id, ordo_id, classis_id):
    genus = Genus.objects.filter(familia_id=familia_list_id)

    context = {
        'genus': genus,
        'menu': menu,
        'title': 'Отображение по классам',
        'familia_selected': familia_list_id
    }
    return render(request, 'zoowikipedia/list_genus.html', context=context)

# Показывает пост о роде животных
def show_genus(request, genus_post_id, familia_id, ordo_id, classis_id):
    post = get_object_or_404(Genus, pk=genus_post_id)

    # Словарь
    context = {
        'post': post,
        'menu': menu,
        'title': post.name,
        'genus_selected': post.pk,
    }
    return render(request, 'zoowikipedia/genus_post.html', context=context)

# Список видов животных на главном экране
def list_species(request, genus_list_id, familia_id, ordo_id, classis_id):
    species = Species.objects.filter(genus_id=genus_list_id)

    context = {
        'species': species,
        'menu': menu,
        'title': 'Отображение по классам',
        'genus_selected': genus_list_id
    }
    return render(request, 'zoowikipedia/list_species.html', context=context)

# Показывает пост о виде животных
def show_species(request, species_post_id, genus_id, familia_id, ordo_id, classis_id):
    post = get_object_or_404(Species, pk=species_post_id)

    # Словарь
    context = {
        'post': post,
        'menu': menu,
        'title': post.name,
        'species_selected': post.pk,
    }
    return render(request, 'zoowikipedia/species_post.html', context=context)
