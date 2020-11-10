from eos.listings.models import Commercial, Residential, NewDevelopment, Holiday, Estate
from django.template import resolve_variable
from django.template import Variable
from eos.lib.db import QuerySetChain
from django.db.models import Q
from django import template
import random


register = template.Library()


listing_models = {
    "Commercial": Commercial,
    "Residential": Residential,
    "NewDevelopment": NewDevelopment,
    "Holiday": Holiday,
    "Estate": Estate,
    "All": [Commercial, Residential, NewDevelopment, Holiday, Estate]
}
available_listing_types = [
    "Residential To Let",
    "Residential For Sale",
    "Commercial To Let",
    "Commercial For Sale",
    'Residential New Development',
    'Commercial New Development',
    'Holiday Letting',
    'Residential Estate',
    'Commercial Estate'
]
available_listing_statuses = ['Active', 'Archived', 'Sold', 'Rented', 'Pending']


class GetVirtualWalkThroughs(template.Node):

    def __init__(self, listing_modules, listing_types, listing_statuses, return_count, randomize):
        self.listing_modules = listing_modules
        self.listing_types = listing_types
        self.listing_statuses = listing_statuses
        self.return_count = return_count
        self.randomize = randomize

    def render(self, context):
        # Resolve the variables
        listing_modules = Variable(self.listing_modules).resolve(context)
        listing_types = Variable(self.listing_types).resolve(context)
        listing_statuses = Variable(self.listing_statuses).resolve(context)
        return_count = Variable(self.return_count).resolve(context)
        randomize = Variable(self.randomize).resolve(context)
        # Filter the variables into specific lists
        # models is a list of listing models. We will parse the parameters of listing_modules to get the required models.
        models = []
        listing_modules = listing_modules.split(",")
        listing_types = listing_types.split(",")
        listing_statuses = listing_statuses.split(",")

        # Assign models to what is defined on client side.
        for module in listing_modules:
            if module in listing_models and module != "All":
                models.append(listing_models[module])
            if module == "All":
                models = listing_models["All"]

        # Listing statuses. If all or "" then use all available status
        if listing_statuses[0] in ["", "All"]:
            listing_statuses = available_listing_statuses

        # Listing Types. If all or "" then use all available Types
        if listing_types[0] in ["", "All"]:
            listing_types = available_listing_types

        all_properties = models[0].objects.none()
        existing_properties = models[0].objects.none()
        featured_properties = models[0].objects.none()
        featured_max = int(return_count)
        for model in models:
            if all_properties:
                existing_properties = all_properties

            featured_properties = model.objects.filter(
                Q(eyespy360__isnull=False) |
                Q(matterport_id__isnull=False) |
                Q(virtual_tour__isnull=False),
                status__in=listing_statuses,
                listing_type__in=listing_types,
                featured=True,
                website_display=True,
                imagegallery__isnull=False).distinct().order_by("id")
            if all_properties:
                current_listing_count = all_properties.count() + featured_properties.count()
            else:
                current_listing_count = featured_properties.count()

            if existing_properties:
                all_properties = QuerySetChain(existing_properties, featured_properties)
            else:
                all_properties = featured_properties

        if current_listing_count < featured_max:
            needed = featured_max - current_listing_count
            for model in models:
                if not needed:
                    break
                additional_listings = model.objects.filter(
                    Q(eyespy360__isnull=False) |
                    Q(matterport_id__isnull=False) |
                    Q(virtual_tour__isnull=False),
                    status__in=listing_statuses,
                    listing_type__in=listing_types,
                    featured=False,
                    website_display=True,
                    imagegallery__isnull=False).distinct().order_by("id")[:needed]
                needed -= additional_listings.count()
                featured_properties = QuerySetChain(featured_properties, additional_listings)

                if existing_properties:
                    all_properties = QuerySetChain(existing_properties, featured_properties)
                else:
                    all_properties = featured_properties

        # Return the list.
        if all_properties.count():
            # Make a list to shuffle the listings.
            all_properties = list(all_properties)
            if randomize:
                random.shuffle(all_properties)
            context['featured'] = all_properties[:featured_max]
        else:
            context['featured'] = None

        return ''


@register.tag(name="get_virtual_walkthroughs")
def get_virtual_walkthroughs(parser, token):
    try:
        tag_name, listing_modules, listing_types, listing_statuses, return_count, randomize = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires 5 arguments: 'listing_modules, listing_types, listing statuses, return_count, randomize'" % token.contents[0]
    return GetVirtualWalkThroughs(listing_modules, listing_types, listing_statuses, return_count, randomize)