from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.db.models import Q
def home(request):
    galleries=HomeImage.objects.all()
    partners=Partner.objects.all()
    services=Service.objects.filter(is_main=True)[:3]
    products=Product.objects.filter(is_main=True)[:3]
    about_info=About.objects.first()
    form=HomeApplyForm()
    if request.method=='POST':
        form=HomeApplyForm(request.POST)
        if form.is_valid():
            form.save()
            form=HomeApplyForm()
    return render(request, 'home.html', {'about_info':about_info, 'services':services,
        'products':products, 'partners':partners, 'galleries':galleries, 'form':form })

def about(request):
    partners=Partner.objects.all()
    about_info=About.objects.last()
    return render(request, 'about.html', {'about_info':about_info, 'partners':partners})

def service(request, category_name=None):
    category_name=None
    all_services=Service.objects.order_by('name')
    paginator = Paginator(all_services, 12)
    page_number = request.GET.get('page', 1)
    services = paginator.page(page_number)
    if request.method == 'GET':
        service_name=request.GET.get('search-field')
        name=request.GET.get('search_query')
        if service_name is not None:
            services=Service.objects.filter(Q(name__icontains=service_name))
    
    if category_name:
        category=get_object_or_404(Service, name=category_name)
        services=Service.objects.filter(category=category)

    return render(request, 'service.html', {'services':services })

def service_detail(request, slug):
    service=get_object_or_404(Service, slug=slug)
    service_categories=ServiceCategory.objects.all()
  
    return render(request, 'service_detail.html', {'service':service, 'service_categories':service_categories})
def products(request, category_name=None):
    category_name=None
    all_products = Product.objects.order_by('name')
    paginator = Paginator(all_products, 2)
    page_number = request.GET.get('page', 1)
    products = paginator.page(page_number)
    if request.method=='GET':
        name=request.GET.get('search_query')
        if name is not None:
            products=Product.objects.filter(Q(name__icontains=name))
    if category_name:
        category=get_object_or_404(Product, name=category_name)
        products=Product.objects.filter(category=category)

    return render(request, 'products.html', {'products':products})

def product_detail(request, slug):
    form=ProductApplyForm()
    product=get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductApplyForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.instance.product = product
            form.save()

    else:
        form = ProductApplyForm()
       
    return render(request, 'product_detail.html', {'product':product, 'form':form})

def contact(request):
    main_contact=Main.objects.last()
    form=ContactForm()
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form=ContactForm()
    return render(request, 'contact.html', {'form':form, 'main_contact':main_contact})