from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description - Textfield() does not have max_lenght
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(null=False, max_length=500)

    def __str__(self):
        return self.name + " " + self.description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUW = 'SUW'
    WAGON = 'Station Wagon'
    COUPE = 'Coupe'
    CONVERTIBLE = 'Convertible'
    MINIVAN = 'Minivan'
    CAR_TYPE_CHOICE = [
        (SEDAN, 'Sedan'),
        (SUW, 'SUW'),
        (WAGON, 'Station Wagon'),
        (COUPE, 'Coupe'),
        (CONVERTIBLE, 'Convertible'),
        (MINIVAN, 'Minivan'),
    ]
    name = models.CharField(null=False, max_length=30)
    dealer_id = models.IntegerField()
    type = models.CharField(
        null=False,
        max_length=20,
        choices=CAR_TYPE_CHOICE,
        default=SEDAN
    )
    year = models.DateField(null=True)
    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.type + " " + str(self.year)

        


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    POSITIVE = 'positive'
    NEGATIVE = 'negative'
    NEUTRAL = 'neutral'
    SENTIMENT_CHOICE = [(POSITIVE, 'positive'), (NEGATIVE, 'negative'), (NEUTRAL, 'neutral')]
    address = models.CharField(max_length=256)
    sentiment = models.CharField(null=False, max_length=20, choices=SENTIMENT_CHOICE, default=NEUTRAL)

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data

class CarReview:

    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.id = id
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment

    def __str__(self):
        return "Review : " + self.id + " " + self.purchase