#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Offers, OffersProperties, Properties, OffersPhotos
from .filters import OfferFilter
from .forms import OfferSort, ContactForm, PublishForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def index(request):
    latest_offers = Offers.objects.order_by('-creation_date').select_related()[:5]
    promoted_offers = Offers.objects.filter(offersproperties__value="True").order_by('?')[:5]
    f = OfferFilter(request.GET, queryset=Offers.objects.all())

    
    context_dict = {
        'latest_offers': latest_offers,
        'promoted_offers': promoted_offers,
        'filter': f,
                    }
    
    return render(request, 'cardom/index.html', context_dict)

def flats(request):
    flat_offers = Offers.objects.filter(object='Mieszkanie').order_by('-creation_date')
    f = OfferFilter(request.GET, queryset=Offers.objects.all())
    if request.method=="GET":
        form = OfferSort(request.GET)
        sortby_choice = request.GET.get('sort_offer', '')
        if sortby_choice=='PDM':
            flat_offers = Offers.objects.filter(object='Mieszkanie').order_by('-creation_date')
        elif sortby_choice=='PDR':
            flat_offers = Offers.objects.filter(object='Mieszkanie').order_by('creation_date')
        elif sortby_choice=='PM':
            flat_offers = Offers.objects.filter(object='Mieszkanie').order_by('-price')
        elif sortby_choice=='PR':
            flat_offers = Offers.objects.filter(object='Mieszkanie').order_by('price')
        elif sortby_choice=='FLM':
            flat_offers = Offers.objects.filter(object='Mieszkanie').order_by('-area')
        elif sortby_choice=='FLR':
            flat_offers = Offers.objects.filter(object='Mieszkanie').order_by('area')
    context_dict = {
        'flat_offers': flat_offers,
        'filter': f,
        'form': form,
        }
    return render(request, 'cardom/flats.html', context_dict)

def houses(request):
    house_offers = Offers.objects.filter(object='Dom').order_by('-creation_date')
    f = OfferFilter(request.GET, queryset=Offers.objects.all())
    if request.method=="GET":
        form = OfferSort(request.GET)
        sortby_choice = request.GET.get('sort_offer', '')
        if sortby_choice=='PDM':
            house_offers = Offers.objects.filter(object='Dom').order_by('-creation_date')
        elif sortby_choice=='PDR':
            house_offers = Offers.objects.filter(object='Dom').order_by('creation_date')
        elif sortby_choice=='PM':
            house_offers = Offers.objects.filter(object='Dom').order_by('-price')
        elif sortby_choice=='PR':
            house_offers = Offers.objects.filter(object='Dom').order_by('price')
        elif sortby_choice=='FLM':
            house_offers = Offers.objects.filter(object='Dom').order_by('-area')
        elif sortby_choice=='FLR':
            house_offers = Offers.objects.filter(object='Dom').order_by('area')
    context_dict = {
        'house_offers': house_offers,
        'filter': f,
        'form': form,
        }
    return render(request, 'cardom/houses.html', context_dict)

def lots(request):
    lot_offers = Offers.objects.filter(object='Dzialka').order_by('-creation_date')
    f = OfferFilter(request.GET, queryset=Offers.objects.all())
    if request.method=="GET":
        form = OfferSort(request.GET)
        sortby_choice = request.GET.get('sort_offer', '')
        if sortby_choice=='PDM':
            lot_offers = Offers.objects.filter(object='Dzialka').order_by('-creation_date')
        elif sortby_choice=='PDR':
            lot_offers = Offers.objects.filter(object='Dzialka').order_by('creation_date')
        elif sortby_choice=='PM':
            lot_offers = Offers.objects.filter(object='Dzialka').order_by('-price')
        elif sortby_choice=='PR':
            lot_offers = Offers.objects.filter(object='Dzialka').order_by('price')
        elif sortby_choice=='FLM':
            lot_offers = Offers.objects.filter(object='Dzialka').order_by('-area')
        elif sortby_choice=='FLR':
            lot_offers = Offers.objects.filter(object='Dzialka').order_by('area')
    context_dict = {
        'lot_offers': lot_offers,
        'filter': f,
        'form': form,
        }
    return render(request, 'cardom/lots.html', context_dict)

def locals(request):
    local_offers = Offers.objects.filter(object='Lokal').order_by('-creation_date')
    f = OfferFilter(request.GET, queryset=Offers.objects.all())
    if request.method=="GET":
        form = OfferSort(request.GET)
        sortby_choice = request.GET.get('sort_offer', '')
        if sortby_choice=='PDM':
            local_offers = Offers.objects.filter(object='Lokal').order_by('-creation_date')
        elif sortby_choice=='PDR':
            local_offers = Offers.objects.filter(object='Lokal').order_by('creation_date')
        elif sortby_choice=='PM':
            local_offers = Offers.objects.filter(object='Lokal').order_by('-price')
        elif sortby_choice=='PR':
            local_offers = Offers.objects.filter(object='Lokal').order_by('price')
        elif sortby_choice=='FLM':
            local_offers = Offers.objects.filter(object='Lokal').order_by('-area')
        elif sortby_choice=='FLR':
            local_offers = Offers.objects.filter(object='Lokal').order_by('area')
    context_dict = {
        'local_offers': local_offers,
        'filter': f,
        'form': form,
        }
    return render(request, 'cardom/locals.html', context_dict)

def other_objects(request):
    other_object_offers = Offers.objects.filter(object='Biurowiec').order_by('-creation_date')
    f = OfferFilter(request.GET, queryset=Offers.objects.all())
    if request.method=="GET":
        form = OfferSort(request.GET)
        sortby_choice = request.GET.get('sort_offer', '')
        if sortby_choice=='PDM':
            other_object_offers = Offers.objects.filter(object='Biurowiec').order_by('-creation_date')
        elif sortby_choice=='PDR':
            other_object_offers = Offers.objects.filter(object='Biurowiec').order_by('creation_date')
        elif sortby_choice=='PM':
            other_object_offers = Offers.objects.filter(object='Biurowiec').order_by('-price')
        elif sortby_choice=='PR':
            other_object_offers = Offers.objects.filter(object='Biurowiec').order_by('price')
        elif sortby_choice=='FLM':
            other_object_offers = Offers.objects.filter(object='Biurowiec').order_by('-area')
        elif sortby_choice=='FLR':
            other_object_offers = Offers.objects.filter(object='Biurowiec').order_by('area')
    context_dict = {
        'other_object_offers': other_object_offers,
        'filter': f,
        'form': form
        }
    return render(request, 'cardom/other_objects.html', context_dict)

def about(request):
    f = OfferFilter(request.GET, queryset=Offers.objects.all())    
    return render(request, 'cardom/about.html', {'filter': f})

def contact(request):
    f = OfferFilter(request.GET, queryset=Offers.objects.all())
    return render(request, 'cardom/contact.html', {'filter': f})

def career(request):
    f = OfferFilter(request.GET, queryset=Offers.objects.all())
    return render(request, 'cardom/career.html', {'filter': f})

def publish_offer(request):
    f = OfferFilter(request.GET, queryset=Offers.objects.all())
    
    form = PublishForm()
    if request.method=="POST":
        form = PublishForm(request.POST)
        if form.is_valid():
            subject = "Zgłoszenie oferty"
            from_email = "E-mail" + form.cleaned_data['from_email']
            phone_nb = "Numer telefonu" + form.cleaned_data['phone_nb']
            category = "Rodzaj obiektu" + form.cleaned_data['category']
            location = "Lokalizacja" + form.cleaned_data['location']
            price = "Cena" + form.cleaned_data['price']
            description = "Dodatkowy opis" + form.cleaned_data['description']
            message = phone_nb + "\n" + category + "\n" + location + "\n" + price + "\n" + description
            try:
                send_mail(subject, from_email, message, ['dominik.broj@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Wprowadzono niepoprawne dane")
    context_dict = {
        'filter': f,
        'form': form
    }
    return render(request, 'cardom/publish_offer.html', context_dict)

def credits(request):
    f = OfferFilter(request.GET, queryset=Offers.objects.all())
    return render(request, 'cardom/credits.html', {'filter': f})

def prices(request):
    f = OfferFilter(request.GET, queryset=Offers.objects.all())
    return render(request, 'cardom/prices.html', {'filter': f})

def offer_list(request):
    f = OfferFilter(request.GET, queryset=Offers.objects.all())

    context_dict = {
        'filter': f,
        }
    return render(request, 'cardom/offer_list.html', context_dict)

def offer_details(request, pk):
    offer = get_object_or_404(Offers, pk=pk)
    f = OfferFilter(request.GET, queryset=Offers.objects.all())
    gallery = OffersPhotos.objects.filter(offers_id=offer.id)
    
    form = ContactForm()
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            subject = form.cleaned_data['subject']
            try:
                send_mail(subject, message, from_email, ['dominik.broj@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Wprowadzono niepoprawne dane")
    
    context_dict = {
        'offer': offer,
        'filter': f,
        'gallery': gallery,
        'form': form,
        }
    return render(request, 'cardom/offer_details.html', context_dict)


            