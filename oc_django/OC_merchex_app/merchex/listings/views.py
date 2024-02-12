
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

from django.core.mail import send_mail

from listings.models import Band
from listings.models import Listing
from listings.forms import BandForm, ContactUsForm, ListsForm

# Create your views here.
def index(request):
    return render(request, 
                'listings/index.html')

def band_list(request):
	bands = Band.objects.all()
	return render(request, 
                'listings/band_list.html',
                {'bands':bands})

def band_detail(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})

def delete_band(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    if (request.method == 'POST'):
        band.delete()
        return redirect('band-list')
    return render(request,
                  'listings/band_delete.html',
                  {'band': band})

def band_create(request):
    if (request.method == 'POST'):
        form = BandForm(request.POST)
        if (form.is_valid()):
            band = form.save()
            return redirect('band_detail', band.id)
    else:
        form = BandForm()
    return render(request,
                  'listings/band_creation.html',
                  {'form':form})

def update_band(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    if(request.method == 'POST'):
        form = BandForm(request.POST, instance=band)
        if (form.is_valid()):
            form.save()
            return redirect ('band_detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request,
                  'listings/band_change.html',
                  {'form': form})

def listings_list(request):
	
	lists = Listing.objects.all()
	return render(request, 
                'listings/listings_list.html',
                {'lists':lists})

def listings_detail(request, list_id):
    list = get_object_or_404(Listing, id=list_id)
    return render(request,
                  'listings/listings_detail.html',
                  {'list': list})

def delete_lists(request, list_id):
    list = get_object_or_404(Listing, id=list_id)
    if (request.method == 'POST'):
        list.delete()
        return redirect('list-list')
    return render(request,
                  'listings/listings_delete.html',
                  {'list': list})

def lists_create(request):
    if (request.method == 'POST'):
        form = ListsForm(request.POST)
        if (form.is_valid()):
            lists = form.save()
            return redirect('lists_detail', lists.id)
    else:
        form = ListsForm()
    return render(request,
                  'listings/listings_creation.html',
                  {'form':form})

def update_lists(request, list_id):
    lists = get_object_or_404(Listing, id=list_id)
    if(request.method == 'POST'):
        form = ListsForm(request.POST, instance=lists)
        if (form.is_valid()):
            form.save()
            return redirect ('lists_detail', lists.id)
    else:
        form = ListsForm(instance=lists)
    return render(request,
                  'listings/listings_change.html',
                  {'form': form})
    

def about(request):
	return render(request,
               'listings/about.html')

def contact(request):
    if (request.method == 'POST'):
        form = ContactUsForm(request.POST)
        if (form.is_valid()):
            send_mail(
                subject=f'MESSAGE FROM {form.cleaned_data["name"] or "anonyme"} (merchex contact form)',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email_sent')
            
    else:
        form = ContactUsForm()
    return render(request,
               'listings/contact.html',
               {'form':form})

def email_success(request):
	return render(request,
               'listings/email_sent.html')