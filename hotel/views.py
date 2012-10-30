from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson
from hotel.models import Hotel
from geographic_info.models import City, Region


def home(request):
    hotels = Hotel.objects.all()
    cities = City.objects.all()
    regions = Region.objects.all().values_list('region_name', 'city')
    return render_to_response('index.html', {'hotels': hotels, 'cities': cities, 'regions': simplejson.dumps(list(regions))},
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


def search(request, city):
    results = []
    if city:
        model_results = Hotel.objects.filter(city=city).values_list('id', 'name')
        print model_results
        for (ids, result) in model_results:
            results.append({'id': ids, 'name': result})

    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype="application/json")
