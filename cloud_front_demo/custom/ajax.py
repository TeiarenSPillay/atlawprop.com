from django.conf import settings
from eos.settings.models import Settings
from django.http import HttpResponse, Http404
from django.db.models import Q
from eos.listings.models import Commercial, Residential, NewDevelopment, Holiday, Estate, Location
import json


# Advanced search
def search_locations(request, property_type, listing_type):

    if request.method != "POST":
        raise Http404

    keyword = request.POST.get('q')
    locations = []

    # -- get a list of province slugs
    locations = Location.objects.filter(
        country__in=settings.SUPPORTED_COUNTRIES
    ).exclude(
        suburb_slug='all'
    )

    locations = locations.exclude(
        residential__isnull=True
    )

    if keyword:
        locations = locations.filter(
            Q(suburb__icontains=keyword) |
            Q(region__icontains=keyword)
        )

        # -- Grab location ids for listings that are active and website display
        if listing_type == "buy":
            valid_location_ids = []
            if property_type == "residential":
                valid_location_ids += list(Residential.objects.filter(
                    status='Active', website_display=True, listing_type='Residential For Sale'
                ).values_list('location', flat=True))
            else:
                valid_location_ids += list(Commercial.objects.filter(
                    status='Active', website_display=True, listing_type='Commercial For Sale'
                ).values_list('location', flat=True))
        elif listing_type == "rent":
            valid_location_ids = []
            if property_type == "residential":
                valid_location_ids += list(Residential.objects.filter(
                    status='Active', website_display=True, listing_type='Residential To Let'
                ).values_list('location', flat=True))
            else:
                valid_location_ids += list(Commercial.objects.filter(
                    status='Active', website_display=True, listing_type='Commercial To Let'
                ).values_list('location', flat=True))

        locations = locations.filter(id__in=valid_location_ids).values(
            'id', 'suburb', 'region').distinct()

    response = HttpResponse(content_type="application/json")
    response.write(json.dumps(list(locations)))
    return response
