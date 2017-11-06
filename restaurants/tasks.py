from background_task import background
from .models import RestaurantLocation

@background(schedule=60)
def adaugare():
    # lookup user by id and send them a message
    inregistrare = RestaurantLocation.objects.create(name="nou", vanzari=1000)
    inregistrare.save()

adaugare( repeat= 60)

@background(schedule=20)
def print_test():
    # lookup user by id and send them a message
    print "!!!TEST!!!"

print_test( repeat= 600)