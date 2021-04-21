from django.test import TestCase

from ..models import Actor, Address, Category, City, Country, Language, Staff, Store
from .create_test_db import CreateTestDb


class TestModels(TestCase):

    def setUp(self):
        self.db_populator = CreateTestDb()

    def createCountry(self):
        self.db_populator.create_country()
        self.db_populator.populate_country(country='Germany')
        self.db_populator.populate_country(country='Brazil')
        self.db_populator.populate_country(country='Spain')

    def create_language(self):
        self.db_populator.create_language()
        self.db_populator.populate_language(name='en')
        self.db_populator.populate_language(name='pt')
        self.db_populator.populate_language(name='en')

    def create_city(self):
        self.createCountry()
        self.db_populator.create_city()
        self.db_populator.populate_city(city='SM', country_id=2)
        self.db_populator.populate_city(city='SA', country_id=2)
        self.db_populator.populate_city(city='ST', country_id=1)
        self.db_populator.populate_city(city='SR', country_id=1)

    def create_address(self):
        self.create_city()
        self.db_populator.create_address()
        self.db_populator.populate_address(address='teste1',
                                           address2='teste1b',
                                           district='testedist',
                                           city_id=3,
                                           postal_code='0215454',
                                           phone='998874545'
                                           )
        self.db_populator.populate_address(address='teste2',
                                           address2='teste2b',
                                           district='testedist2',
                                           city_id=2,
                                           postal_code='021545224',
                                           phone='998822245'
                                           )

    def create_staff(self):
        self.create_address()
        self.db_populator.create_staff()

    def create_store(self):
        self.create_staff()
        self.db_populator.create_store()
        self.db_populator.populate_store(1, 1)

    def test_category(self):
        self.db_populator.create_category()
        self.db_populator.populate_category('test1')
        categories = Category.objects.all()
        assert len(categories) == 1

    def test_actor(self):
        self.db_populator.create_actor()
        self.db_populator.populate_actor(first_name='Robert', last_name='De Niro')
        actors = Actor.objects.all()
        assert len(actors) == 1

    def test_language(self):
        self.create_language()
        languages = Language.objects.all()
        assert len(languages) == 3

    def test_country_(self):
        self.createCountry()
        actors = Country.objects.all()
        assert len(actors) == 3

    def test_city(self):
        self.create_city()
        actors = City.objects.all()
        assert len(actors) == 4

    def test_address(self):
        self.create_address()
        addresses = Address.objects.all()
        assert len(addresses) == 2

    def test_staff(self):
        self.create_staff()
        self.db_populator.populate_staff(first_name='teste1', last_name='last', address_id=1, email='a@bol.com',
                                         store_id=1, active=True, username='teste', password='123')
        staffs = Staff.objects.all()
        assert len(staffs) == 1

    def test_store(self):
        self.create_store()
        stores = Store.objects.all()
        assert len(stores) == 1

    def test_customer(self):
        self.create_store()
        self.db_populator.create_customer()
        self.db_populator.populate_customer(1, 't1', 't2', 'a@bol.com', '1', True, '2006-02-14', True)
