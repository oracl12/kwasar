from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product
from django.core.mail import send_mail


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    order_by = request.POST.get('bt')
    products = Product.objects.filter(available=True)
    if category_slug:
        if order_by:
            category = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.filter(available=True).filter(category=category).order_by(order_by)
        else:
            category = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.filter(available=True).filter(category=category).order_by("-price")
    else:
        if order_by:
            products = Product.objects.filter(available=True).order_by(order_by)
    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, 'shop/product/detail.html', context)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')

def back(request):
    return render(request, 'shop/back.html')

def delivery(request):
    return render(request, 'shop/delivery.html')

def question(request):
    try:
        email = request.POST.get('email')
        name=request.POST.get('name')
        msg = request.POST.get('msg')
        msg = name+" "+ msg+ " "+email
        #до адміна
        send_mail(
            "Дали запитання на kwasar.ua",
            msg,
            "KvazarUa.noreply@gmail.com",
            ["zhydachiv_zem@ukr.net"]
        )
        msg_person = f"Ви задали питання на сайті kwasar.ua" \
                     f"Очікуйте на відповідь від нашого оператора \n Вдалого дня! \n +3909750505050"
        # до користувача
        send_mail(
            "Ви задали питання на сайті kwasar.ua",
            msg_person,
            "KvazarUa.noreply@gmail.com",
            [email]
        )
        message = "Повідомлення відіслане"
    except:
        message=None
    return render(request, 'shop/question.html',{"message":message})