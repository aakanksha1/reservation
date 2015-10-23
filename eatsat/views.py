from eatsat.models import Restaurant, Account, Eatsat
from django.shortcuts import render
from django.http.response import HttpResponseRedirect

from django.core.urlresolvers import reverse
import datetime

def index(request):
    restaurant_List = Restaurant.objects.order_by('name')
    context = {'restaurant_List': restaurant_List}
    return render(request, 'index.html', context)

def restaurant(request, restaurant_name, restaurant_address):
    restaurant = Restaurant.objects.get(name=restaurant_name, address=restaurant_address)
    accounts_at_restaurant = Eatsat.objects.filter(restaurant__name=restaurant_name, restaurant__address=restaurant_address).values('account')
    eatsat_list = Eatsat.objects.filter(restaurant__name=restaurant_name, restaurant__address=restaurant_address);
    accounts = Account.objects.exclude(id__in=accounts_at_restaurant)
    context = {'restaurant': restaurant, 'accounts':accounts, 'eatsat_list':eatsat_list}
    return render(request, 'restaurant.html', context)

def update_wait_time(request, restaurant_name, restaurant_address):
    restaurant = Restaurant.objects.get(name=restaurant_name, address=restaurant_address)
    restaurant.estimated_wait_time = request.POST['new_wait_time']
    restaurant.save()
    return HttpResponseRedirect(reverse('eatsat:restaurant', args=(restaurant_name,restaurant_address)))

def new_eatsat(request, restaurant_name, restaurant_address):
    eatsat_party_size = request.POST['party_size']
    account_id = request.POST['account_id']
    eatsat_restaurant = Restaurant.objects.get(name=restaurant_name, address=restaurant_address)
    eatsat_account = Account.objects.get(account_id=account_id)
    eatsat_wait_time = None
    eatsat_meal_time = None
    if (request.POST['eatsat_type'] == "walkin"):
        eatsat_wait_time = eatsat_restaurant.estimated_wait_time     
    else:
        eatsat_meal_time_string = request.POST['reservation_time']
        eatsat_meal_time = datetime.datetime.strptime(eatsat_meal_time_string,
                                                     '%Y-%m-%dT%H:%M')
    new_eatsat = Eatsat(party_size=eatsat_party_size, account=eatsat_account, restaurant=eatsat_restaurant, wait_time=eatsat_wait_time, meal_time=eatsat_meal_time)
    new_eatsat.save()
    return HttpResponseRedirect(reverse('eatsat:restaurant', args=(restaurant_name, restaurant_address,)))

def cancel_eatsat(request, restaurant_name, restaurant_address, account_id):
    eatsat = Eatsat.objects.get(restaurant__name=restaurant_name, restaurant__address=restaurant_address, account__account_id=int(account_id))
    eatsat.delete()
    return HttpResponseRedirect(reverse('eatsat:restaurant', args=(restaurant_name, restaurant_address,)))
