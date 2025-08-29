from django.db.models import Q
from .models import Listing


def filter_listings(qs, params):
q = params.get('q')
category_id = params.get('categoryId')
city = params.get('city')
sort = params.get('sort')


if q:
qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))
if category_id:
qs = qs.filter(category_id=category_id)
if city:
qs = qs.filter(city__icontains=city)


if sort == 'priceAsc':
qs = qs.order_by('price_cents')
elif sort == 'priceDesc':
qs = qs.order_by('-price_cents')
else:
qs = qs.order_by('-created_at')
return qs