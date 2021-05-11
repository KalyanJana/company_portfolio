from django.shortcuts import render,get_object_or_404
from .models import Product
from aboutus.models import AboutUs
from career.models import Career
from Environment.models import EnvironmentsAndHealthSafety
from contactus.models import ContactUs

def home(request):
    products=Product.objects.all()
    aboutuses=AboutUs.objects.all()
    careers=Career.objects.all()
    environments=EnvironmentsAndHealthSafety.objects.all()
    contactuses=ContactUs.objects.all()
    return render(request, 'ourproduct/home.html', {'products':products,'aboutuses':aboutuses,'careers':careers,'environments':environments,'contactuses':contactuses})
def all_ourproducts(request):
    products=Product.objects.all()
    return render(request, 'ourproduct/home.html', {'products':products})
def product_details(request,product_id):
    product= get_object_or_404(Product, pk=product_id)
    return render(request, 'ourproduct/product_details.html', {'product':product})
