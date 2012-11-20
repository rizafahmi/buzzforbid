from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson
from hotel.models import Hotel
from hotel.forms import SearchForm
from geographic_info.models import Region


def search_hotels(request, priority):
    if priority == 1:  # Raise the price
        raise_price = request.POST['price'] + (request.POST['price'] * 0.25)
        return Hotel.objects.filter(city=request.POST['city'],
                room_type_1__default_publish_price__lte=raise_price,
                room_type_1__allotment__gte=request.POST['number_of_rooms'],
                rating__gte=request.POST['stars'])
    elif priority == 2:  # Skip the price
        return Hotel.objects.filter(city=request.POST['city'],
                room_type_1__allotment__gte=request.POST['number_of_rooms'],
                rating__gte=request.POST['stars'])
    # Skip the price and rating
    return Hotel.objects.filter(city=request.POST['city'],
            room_type_1__allotment__gte=request.POST['number_of_rooms'])


def home(request):
    # hotels = Hotel.objects.all()
    # cities = City.objects.all()
    # regions = Region.objects.all().values_list('region_name', 'city')
    # return render_to_response('index.html', {'hotels': hotels, 'cities': cities, 'regions': simplejson.dumps(list(regions))},
    #         context_instance=RequestContext(request))

    if request.POST:
        # print request.POST, request.POST.getlist('region')

        # search for hotels
        # Check apakah date masuk ke salah satu season
            # Kalo masuk, cari harganya

            # Kalo ngga masuk harganya default
        hotels = Hotel.objects.filter(city=request.POST['city'],
                rating__gte=request.POST['stars'],
                room_type_1__allotment__gte=request.POST['number_of_rooms'],
                room_type_1__default_publish_price__lte=request.POST['price'])

        # cek dulu, kalo result nya sedikit, dikurangin search parameter nya
        # while jumlah < 4 iterasi cari sampe hasil > 4
        iter = 1
        while hotels < 4:
            hotels += search_hotels(request, iter)
            iter = iter + 1

        # iterate hotels, save to request model

    return render_to_response('index.html',
            {'form': SearchForm()},
            context_instance=RequestContext(request))


def get_region(request, city):
    results = []
    if city:
        model_results = Region.objects.filter(city__id=city).values_list('id', 'region_name')
        # results = [region.region_name for region in model_results]
        for (ids, result) in model_results:
            results.append({'id': ids, 'region_name': result})

    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype="application/json")


def search(request, city, star, checkin, checkout, region, price, qty):
    results = []

    region_split = []
    # split the region
    if region != '0':
        region_split = [int(reg) for reg in region.split(',')]

    # print region_split

    # Example: Hotel.objects.filter(city=3, room_type_1__default_price__lte=1500000, room_type_1__default_price__gte=1000000)
        model_results = Hotel.objects.filter(city=city, rating__gte=star,
            room_type_1__default_publish_price__gte=price,
            region__in=region_split).values_list('id', 'name')
    else:
        model_results = Hotel.objects.filter(city=city, rating__gte=star,
            room_type_1__default_publish_price__gte=price).values_list('id', 'name')

    for (ids, result) in model_results:
        results.append({'id': ids, 'name': result})

    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype="application/json")
