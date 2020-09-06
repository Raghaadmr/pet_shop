from django.shortcuts import render, redirect
from .models import Pets
from .forms import PetsForm

def list(request):
    pets = Pets.objects.all()
    context = {
        "pets": pets,
    }
    return render(request, 'list.html', context)


def detail(request, pets_id):
    pets = Pets.objects.get(id=pets_id)
    context = {
        "pets": pets,
    }
    return render(request, 'detail.html', context)


def create(request):
    form = PetsForm()
    if request.method == "POST":
        form = PetsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pets-list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)


def update(request, pets_id):
    pet_obj = Pets.objects.get(id=pet_id)
    form = PetsForm(instance=pet_obj)
    if request.method == "POST":
        form = PetsForm(request.POST, request.FILES, instance=pet_obj)
        if form.is_valid():
            form.save()
            return redirect('pets-list')
    context = {
        "pet_obj": pet_obj,
        "form":form,
    }
    return render(request, 'update.html', context)


def delete(request, pets_id):
    pet_obj = Pets.objects.get(id=pet_id)
    pet_obj.delete()
    return redirect('pets-list')
