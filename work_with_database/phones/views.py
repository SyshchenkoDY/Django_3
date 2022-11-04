from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')
    if sort == 'min_price':
        all_phones = Phone.objects.all().order_by('price')
        models = [{'name': phone.name, 'price': phone.price, 'image': phone.image, 'release_date': phone.release_date,
                   'lte_exist': phone.lte_exist, 'slug': phone.slug} for phone in all_phones]
        context = {
                'phones': models
            }
    elif sort == 'max_price':
        all_phones = Phone.objects.all().order_by('-price')
        models = [{'name': phone.name, 'price': phone.price, 'image': phone.image, 'release_date': phone.release_date,
                   'lte_exist': phone.lte_exist, 'slug': phone.slug} for phone in all_phones]
        context = {
                'phones': models
            }
    else:
        all_phones = Phone.objects.all().order_by('name')
        models = [{'name': phone.name, 'price': phone.price, 'image': phone.image, 'release_date': phone.release_date, 'lte_exist': phone.lte_exist, 'slug': phone.slug} for phone in all_phones]
        context = {
            'phones': models
        }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    current_model = Phone.objects.filter(slug=slug)
    model = [{'name': phone.name, 'price': phone.price, 'image': phone.image, 'release_date': phone.release_date,
               'lte_exists': phone.lte_exist, 'slug': phone.slug} for phone in current_model]
    context = {
        'phone': model[0]
    }
    return render(request, template, context)
