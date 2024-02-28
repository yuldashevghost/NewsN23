from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, New, Advertise


# Create your views here.
def home_page(request):
    news = New.objects.all()
    return render(request, 'news/index.html', {"news": news})


def contact_page(request):
    return render(request, 'news/contact.html')

def t_page(request):
    return render(request, 'news/404.html')

def single_page(request, new_id):
    new = get_object_or_404(New, pk=new_id)
    return render(request, 'news/single_page.html', {"new": new})

def contact_create(request):
    contacts = Contact.objects.all().reverse()[:10]
    context={
        "contacts": contacts
    }

    if request.method == 'POST':
        # request.POST['email'] = request.POST['email']
        name = request.POST["name"]
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(name=name, email=email, message=message)

        print(request.POST)
        return redirect('news:contact_page')

        # return render(request, 'news/contact_create.html', context=context)
    else:
        return render(request, 'news/contact_create.html', context=context)

def advertise_page(request):
    advertises = Advertise.objects.all()
    return render(request, 'news/advretertise.html', {"advertises": advertises})