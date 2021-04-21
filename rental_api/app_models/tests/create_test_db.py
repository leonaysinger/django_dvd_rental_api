from datetime import datetime
from django.db import connection

from ..models import Actor, Address, Category, City, Country, Customer, Language, Staff, Store


class CreateTestDb:

    def __init__(self):
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @classmethod
    def create_category(cls):
        connection.cursor().execute("CREATE SEQUENCE category_category_id_seq "
                                    "START WITH 1 "
                                    "INCREMENT BY 1 "
                                    "NO MINVALUE "
                                    "NO MAXVALUE CACHE 1;"
                                    "CREATE TABLE category ("
                                    "category_id integer DEFAULT "
                                    "nextval('category_category_id_seq'::regclass) NOT NULL,"
                                    "name character varying(25) NOT NULL,"
                                    "last_update timestamp without time zone DEFAULT now() NOT NULL);")

    def populate_category(self, name):
        Category.objects.create(name=name, last_update=self.now)

    @staticmethod
    def drop_table(table):
        connection.cursor().execute("DROP TABLE {};".format(table))

    @classmethod
    def create_actor(cls):
        connection.cursor().execute("CREATE SEQUENCE actor_actor_id_seq START WITH 1 "
                                    "INCREMENT BY 1 "
                                    "NO MINVALUE "
                                    "NO MAXVALUE "
                                    "CACHE 1;"
                                    "CREATE TABLE actor ( "
                                    "actor_id integer DEFAULT nextval('actor_actor_id_seq'::regclass) NOT NULL,"
                                    "first_name character varying(45) NOT NULL, "
                                    "last_name character varying(45) NOT NULL, "
                                    "last_update timestamp without time zone DEFAULT now() NOT NULL);")

    def populate_actor(self, first_name, last_name):
        Actor.objects.create(first_name=first_name, last_name=last_name, last_update=self.now)

    @classmethod
    def create_country(cls):
        connection.cursor().execute("CREATE SEQUENCE country_country_id_seq "
                                    "START WITH 1 "
                                    "INCREMENT BY 1 "
                                    "NO MINVALUE "
                                    "NO MAXVALUE "
                                    "CACHE 1;"
                                    "CREATE TABLE country ("
                                    "country_id integer DEFAULT nextval('country_country_id_seq'::regclass) NOT NULL, "
                                    "country character varying(50) NOT NULL, "
                                    "last_update timestamp without time zone DEFAULT now() NOT NULL);")

    def populate_country(self, country):
        Country.objects.create(country=country, last_update=self.now)

    @classmethod
    def create_city(cls):
        connection.cursor().execute("CREATE SEQUENCE city_city_id_seq "
                                    "START WITH 1 "
                                    "INCREMENT BY 1 "
                                    "NO MINVALUE "
                                    "NO MAXVALUE "
                                    "CACHE 1;"
                                    "CREATE TABLE city ("
                                    "city_id integer DEFAULT nextval('city_city_id_seq'::regclass) NOT NULL, "
                                    "city character varying(50) NOT NULL, "
                                    "country_id smallint NOT NULL, "
                                    "last_update timestamp without time zone DEFAULT now() NOT NULL);")

    def populate_city(self, city, country_id):
        City.objects.create(city=city, country_id=country_id, last_update=self.now)

    @classmethod
    def create_language(cls):
        connection.cursor().execute("CREATE SEQUENCE language_language_id_seq "
                                    "START WITH 1 "
                                    "INCREMENT BY 1 "
                                    "NO MINVALUE "
                                    "NO MAXVALUE "
                                    "CACHE 1;"
                                    "CREATE TABLE language ("
                                    "language_id integer DEFAULT nextval('"
                                    "language_language_id_seq'::regclass) NOT NULL, "
                                    "name character(20) NOT NULL, "
                                    "last_update timestamp without time zone DEFAULT now() NOT NULL);")

    def populate_language(self, name):
        Language.objects.create(name=name, last_update=self.now)

    @classmethod
    def create_address(cls):
        connection.cursor().execute("CREATE SEQUENCE address_address_id_seq "
                                    "START WITH 1 "
                                    "INCREMENT BY 1 "
                                    "NO MINVALUE "
                                    "NO MAXVALUE "
                                    "CACHE 1;"
                                    "CREATE TABLE address ("
                                    "address_id integer DEFAULT nextval('address_address_id_seq'::regclass) NOT NULL,"
                                    "address character varying(50) NOT NULL, "
                                    "address2 character varying(50), "
                                    "district character varying(20) NOT NULL, "
                                    "city_id smallint NOT NULL, "
                                    "postal_code character varying(10), "
                                    "phone character varying(20) NOT NULL, "
                                    "last_update timestamp without time zone DEFAULT now() NOT NULL);")

    def populate_address(self, address, address2, district, city_id, postal_code, phone):
        Address.objects.create(address=address, address2=address2, district=district,
                               city_id=city_id, postal_code=postal_code, phone=phone, last_update=self.now)

    @classmethod
    def create_staff(cls):
        connection.cursor().execute("CREATE SEQUENCE staff_staff_id_seq "
                                    "START WITH 1 "
                                    "INCREMENT BY 1 "
                                    "NO MINVALUE "
                                    "NO MAXVALUE "
                                    "CACHE 1;"
                                    "CREATE TABLE staff ("
                                    "staff_id integer DEFAULT nextval('staff_staff_id_seq'::regclass) NOT NULL, "
                                    "first_name character varying(45) NOT NULL, "
                                    "last_name character varying(45) NOT NULL, "
                                    "address_id smallint NOT NULL, "
                                    "email character varying(50), "
                                    "salary smallint, "
                                    "store_id smallint NOT NULL, "
                                    "active boolean DEFAULT true NOT NULL, "
                                    "username character varying(16) NOT NULL, "
                                    "password character varying(40), "
                                    "last_update timestamp without time zone DEFAULT now() NOT NULL, "
                                    "picture bytea);")

    def populate_staff(self, first_name, last_name, address_id, email, store_id, active, username, password):
        Staff.objects.create(first_name=first_name, last_name=last_name, address_id=address_id,
                             email=email, store_id=store_id, active=active, username=username,
                             password=password, last_update=self.now)

    @classmethod
    def create_store(cls):
        connection.cursor().execute("CREATE SEQUENCE store_store_id_seq "
                                    "START WITH 1 "
                                    "INCREMENT BY 1 "
                                    "NO MINVALUE "
                                    "NO MAXVALUE "
                                    "CACHE 1;"
                                    "CREATE TABLE store ("
                                    "store_id integer DEFAULT nextval('store_store_id_seq'::regclass) NOT NULL, "
                                    "manager_staff_id smallint NOT NULL, "
                                    "address_id smallint NOT NULL, "
                                    "last_update timestamp without time zone DEFAULT now() NOT NULL);")

    def populate_store(self, manager_staff_id, address_id):
        Store.objects.create(manager_staff_id=manager_staff_id, address_id=address_id, last_update=self.now)

    @classmethod
    def create_customer(cls):
        connection.cursor().execute("CREATE SEQUENCE customer_customer_id_seq "
                                    "START WITH 1 "
                                    "INCREMENT BY 1 "
                                    "NO MINVALUE "
                                    "NO MAXVALUE "
                                    "CACHE 1;"
                                    "CREATE TABLE customer ("
                                    "customer_id integer DEFAULT nextval('"
                                    "customer_customer_id_seq'::regclass) NOT NULL, "
                                    "store_id smallint NOT NULL, "
                                    "first_name character varying(45) NOT NULL, "
                                    "last_name character varying(45) NOT NULL, "
                                    "email character varying(50), "
                                    "address_id smallint NOT NULL, "
                                    "activebool boolean DEFAULT true NOT NULL, "
                                    "create_date date DEFAULT ('now'::text)::date NOT NULL, "
                                    "last_update timestamp without time zone DEFAULT now(), "
                                    "active integer);")

    def populate_customer(self, store_id, first_name, last_name, email, address_id, activebool, create_date, active):
        Customer.objects.create(store_id=store_id, first_name=first_name, last_name=last_name, email=email,
                                address_id=address_id, activebool=activebool, create_date=create_date,
                                last_update=self.now, active=active)
