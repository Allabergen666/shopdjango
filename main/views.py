from django.shortcuts import render, redirect
from .models import Category, Product
from main.forms import ProductForm, CategoryForm
from django.contrib import messages

# Create your views here.




def IndexViev(request):
    return render(request, 'main/index.html')


def AddProductViev(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Add product succes")
        else:
            messages.error(request, form.errors)
            # messages.debug
            # messages.success
            # messages.error
            # messages.warning
            # messages.info     
    else:
        form = ProductForm()
    context = {
        "form": form
        }
    return render(request, 'main/addproduct.html', context=context)


def ProductViev(request):
    products = Product.objects.all()
    context = {
        "products": products
        }
    return render(request, 'main/product.html', context=context)


def CategoryViev(request):
    return render(request, 'main/category.html')

   