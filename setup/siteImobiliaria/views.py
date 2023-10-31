from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from .models import Imovel, Message
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic import View
from .models import Imovel, Message
from .forms import ImovelForm

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def properties(request):
    return render(request, 'properties.html')

def property_details(request):
    return render(request, 'property-details.html')

class ImovelListView(View):
    def get(self, request):
        imoveis = Imovel.objects.all()
        return render(request, 'imovel_list.html', {'imoveis': imoveis})

class MessageCreateView(View):
    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message_text = request.POST['message']

        message = Message(name=name, email=email, subject=subject, message=message_text)
        message.save()

        return JsonResponse({'success': True})

class ImovelListView(View):
    def get(self, request):
        imoveis = Imovel.objects.all()
        return render(request, 'imovel_list.html', {'imoveis': imoveis})

class ImovelCreateView(View):
    def get(self, request):
        form = ImovelForm()
        return render(request, 'imovel_create.html', {'form': form})

    def post(self, request):
        form = ImovelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('imovel-list')
        return render(request, 'imovel_create.html', {'form': form})

class ImovelUpdateView(View):
    def get(self, request, id):
        imovel = get_object_or_404(Imovel, id=id)
        form = ImovelForm(instance=imovel)
        return render(request, 'imovel_update.html', {'form': form, 'imovel': imovel})

    def post(self, request, id):
        imovel = get_object_or_404(Imovel, id=id)
        form = ImovelForm(request.POST, instance=imovel)
        if form.is_valid():
            form.save()
            return redirect('imovel-list')
        return render(request, 'imovel_update.html', {'form': form, 'imovel': imovel})

class ImovelDeleteView(View):
    def post(self, request, id):
        imovel = get_object_or_404(Imovel, id=id)
        imovel.delete()
        return JsonResponse({'success': True})
