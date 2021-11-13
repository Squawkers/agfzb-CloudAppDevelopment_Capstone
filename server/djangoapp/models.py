from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description - Textfield() does not have max_lenght
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_lenght=1000)
    description = models.Textfield()
    def __str__(self):
        return "Name" + self.name + ", " + \
                "Description: " + self.description


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
    SUV = 'SUV'
    WAGON = 'Wagon'
    HATSCHBACK = 'Hatchback'

    CAR_CHOICES = [
        (SEDAN = 'Sedan'),
        (SUV = 'SUV'),
        (WAGON = 'Wagon'),
        (HATSCHBACK = 'Hatchback'),
        (SEDAN, 'Sedan'),
    ]
    
    carmake = model.ForeignKey(CarMake, on_delete=model.CASCADE)
    name = model.CharField(null=False,max_lenght=1000)
    dealer_id = models.InteggerField()
    car_type = model.CharField(max_lenght=1, choices=CAR_CHOICES, default=SEDAN)
    year = models.DataField()
    def __str__(self):
        return "Name: " + self.name + ", " + "Car Type: " +  self.car_type ", " + "Year: " + str(self.year)


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    def __init__(self, id, full_name, short_name, city, state, st, address, zip, lat, long):
        self.id = id
        self.full_name = full_name
        self.short_name = short_name
        self.city = city
        self.state = state
        self.address = address
        self.zip =zip
        self.lat = lat
        self.long = long
    def __str__(self):
        return "Dealer: name: " + self.full_name


# <HINT> Create a plain Python class `DealerReview` to hold review data

class DealerReview:
    def __init__(self, name, dealership, review, purchase, purchase_date, car_make, car_model, car_year)
        self.name = name
        self.dealership = dealership
        self.review = review
        self.purchase = puchase
        self.purchase_date = puchase_date
        self.car_make = review
        self.car_model = car_model
        self.car_year = car_year
    def __str__(self):
        return "Name:" + self.name