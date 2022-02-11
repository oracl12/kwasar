from django.shortcuts import render
from cart.cart import Cart
from .models import OrderItem
from .forms import OrderCreateForm
from django.core.mail import send_mail


def order_create(request):
    data = {"product": [], "price": [], "quantity": []}
    msg_dev = str()
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'], quantity=item['quantity'])
                msg_dev += str(item['product']) + ' ' + str(item['price']) + '.грн ' + str(
                    item['quantity']) + "к." + "|"

            send_mail(
                "Замовлення на kwasar.ua",
                msg_dev,
                "KvazarUa.noreply@gmail.com",
                ["zhydachiv_zem@ukr.net"]
            )
            msg_person = f"Ви здійснили замовлення на сайті kwasar.ua, ваше замовлення: {msg_dev} \n " \
                         f"Очікуйте на звінок від нашого оператора \n Вдалого дня! \n +3909750505050"
            send_mail(
                "Ви здійснили замовлення на сайті kwasar.ua",
                msg_person,
                "KvazarUa.noreply@gmail.com",
                [order.email]
            )

            cart.clear()
            return render(request, 'order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'order/create.html', {'cart': cart, 'form': form})
