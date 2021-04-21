from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^categories/$', views.CategoryList.as_view(), name='category-list'),
    url(r'^actors/$', views.ActorList.as_view(), name='actor-list'),
    url(r'^countries/$', views.CountryList.as_view(), name='country-list'),
    url(r'^cities/$', views.CityList.as_view(), name='city-list'),
    url(r'^languages/$', views.LanguageList.as_view(), name='language-list'),
    url(r'^addresses/$', views.AddressList.as_view(), name='address-list'),
    url(r'^films/$', views.FilmList.as_view(), name='film-list'),
    url(r'^film_actors/$', views.FilmActorList.as_view(), name='film-actor-list'),
    url(r'^customers/$', views.CustomerList.as_view(), name='customer-list'),
    url(r'^film_categories/$', views.FilmCategoryList.as_view(), name='film-category-list'),
    url(r'^inventory/$', views.InventoryList.as_view(), name='inventory-list'),
    url(r'^payments/$', views.PaymentList.as_view(), name='payment-list'),
    url(r'^rentals/$', views.RentalList.as_view(), name='rental-list'),
    url(r'^staffs/$', views.StaffList.as_view(), name='staff-list'),
    url(r'^stores/$', views.StoreList.as_view(), name='store-list'),
]
