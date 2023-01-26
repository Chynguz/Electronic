from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.models import Product, Category


# Create your views here.
def main(request):
    product = Product.objects.all()
    category = Category.objects.all()
    return render(request, 'index.html', {'product': product, 'category': category})


def more(request, id):
    more = Product.objects.get(id=id)
    return render(request, 'more.html', {'more': more})


def add_to_cart(request, id):
    car_session = request.session.get('car_session', [])
    car_session.append(id)
    request.session['car_session'] = car_session
    print(f'{car_session} dobavleno')
    return HttpResponseRedirect('/')


def cart(request):
    car_session = request.session.get('car_session', [])
    print(f'{car_session} pokazyvaet 1')
    ln_cart = len(car_session)
    product = Product.objects.all()
    price = 0
    for i in range(len(car_session)):
        for j in product:
            if i == j.id:
                price += j.price
                print(f'{j.price} oshibka')

    product_cart = []
    for i in set(car_session):
        cart_count = []
        pro_count = list(car_session).count(i)
        cart_count.append(pro_count)
        for j in product:
            if i == j.id:
                cart_count.append(j)
        product_cart.append(cart_count)

    return render(request, 'cart.html', {'price': price, 'product_cart': product_cart, 'ln_cart': ln_cart})


def remove_product(request, id):
    car_session = request.session.get('car_session', [])
    remove_cart = []
    remove_cart = car_session
    remove_cart.pop()
    request.session['car_session'] = remove_cart
    return HttpResponseRedirect('/cart')


# def cart(request):
#     cart_session = request.seesion.get('cart_session', [])
#     amount = len(cart_session)
#     products = Product.objects.filter(id_in = cart_session)
#     total_prise = 0
#     for i in products:
#         i.count = cart_session.count(i.id)
#         i.sum = i.count * i.price
#         total_prise += i.sum
#     context = {'products': products, 'amount': amount, 'total_price': total_prise}
#     return render(request, 'cart.html', context)
