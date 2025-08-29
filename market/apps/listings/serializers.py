from rest_framework import serializers
class Meta:
model = ListingImage
fields = ('id','url','is_cover','sort')


class ListingOut(serializers.ModelSerializer):
images = ListingImageOut(many=True)
class Meta:
model = Listing
fields = ('id','slug','title','description','price_cents','currency','condition','city','images','created_at')


class ListingDetailOut(serializers.ModelSerializer):
images = ListingImageOut(many=True)
class Meta:
model = Listing
fields = ('id','slug','title','description','price_cents','currency','condition','city','images','status','created_at','updated_at')


class ListingCreate(serializers.Serializer):
title = serializers.CharField(min_length=3)
description = serializers.CharField(min_length=10)
priceCents = serializers.IntegerField(min_value=0)
currency = serializers.CharField()
condition = serializers.ChoiceField(choices=[c for c,_ in Listing.Condition.choices])
city = serializers.CharField()
categoryId = serializers.IntegerField()
featured = serializers.BooleanField(required=False)
images = ListingImageIn(many=True, required=False)


def create(self, validated):
user = self.context['request'].user
listing = Listing.objects.create(
user=user,
category_id=validated['categoryId'],
title=validated['title'],
description=validated['description'],
price_cents=validated['priceCents'],
currency=validated['currency'],
condition=validated['condition'],
city=validated['city'],
featured=validated.get('featured', False),
)
for i, img in enumerate(validated.get('images', [])):
ListingImage.objects.create(
listing=listing,
url=img['url'],
is_cover=img.get('isCover', False) or img.get('is_cover', False),
sort=img.get('sort', i)
)
return listing


class ListingUpdate(serializers.Serializer):
title = serializers.CharField(required=False)
description = serializers.CharField(required=False)
priceCents = serializers.IntegerField(required=False, min_value=0)
currency = serializers.CharField(required=False)
condition = serializers.ChoiceField(required=False, choices=[c for c,_ in Listing.Condition.choices])
city = serializers.CharField(required=False)
categoryId = serializers.IntegerField(required=False)
featured = serializers.BooleanField(required=False)