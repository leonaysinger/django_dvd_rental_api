from rest_framework import serializers
from .models import Actor, Address, Category, City, Country, Customer, Film, FilmActor,\
    FilmCategory, Inventory, Language, Payment, Rental, Staff, Store


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = City
        fields = ['city_id', 'city', 'last_update', 'country']


class AddressSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)

    class Meta:
        model = Address
        fields = ['address_id', 'address', 'address2', 'district',
                  'city', 'postal_code', 'phone', 'last_update']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class FilmActorSerializer(serializers.ModelSerializer):
    actor = ActorSerializer(read_only=True)
    film = FilmSerializer(read_only=True)

    class Meta:
        model = FilmActor
        fields = '__all__'


class FilmCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    film = FilmSerializer(read_only=True)

    class Meta:
        model = FilmCategory
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Staff
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    rental = RentalSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'
