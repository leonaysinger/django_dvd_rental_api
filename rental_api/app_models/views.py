from rest_framework import generics
from .models import Actor, Address, Category, City, Country, Customer, Film, FilmActor,\
    FilmCategory, Inventory, Language, Payment, Rental, Staff, Store
from .serializers import \
    ActorSerializer, AddressSerializer, CategorySerializer, CitySerializer, CustomerSerializer, \
    CountrySerializer, FilmActorSerializer, FilmCategorySerializer, FilmSerializer, InventorySerializer, \
    LanguageSerializer, PaymentSerializer, RentalSerializer, StaffSerializer, StoreSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ActorList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class LanguageList(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmActorList(generics.ListCreateAPIView):
    queryset = FilmActor.objects.all()
    serializer_class = FilmActorSerializer


class FilmCategoryList(generics.ListCreateAPIView):
    queryset = FilmCategory.objects.all()
    serializer_class = FilmCategorySerializer


class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class RentalList(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer


class StaffList(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
