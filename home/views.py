from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Product
from subscription.models import Subscribers
from subscription.forms import SubscribeForm



def index(request):
    """Main index page render and handles News Letter Subscribers"""
    products = Product.objects.filter(category__name='honey')
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Thank you for subscribing to our News')
            return redirect('home')
        else:
            form = SubscribeForm()

    context = {
        'products': products,
        'form': form,
    }

    return render(request, 'home/index.html', context)

 