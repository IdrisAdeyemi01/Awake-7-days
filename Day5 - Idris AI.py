nights= int(input(' How many nights were spent: '))
city = input('What city is it?. (Ajah, Lagos Island, Victoria Island or Lekki: ')
days= int(input('Cars were rented for how many days: '))


def hotel_cost(nights):
    return nights*1000
def plane_ride_cost(city):
    if city.lower()== 'ajah':
        return 5000
    elif city.lower() == 'lagos island':
        return 2000
    elif city.lower() == 'victoria island':
        return 2500
    elif city.lower() == 'lekki':
        return 4500
def rental_car_cost(days):
    if days>= 7:
        cost= 1000*days - 2000
    elif days >= 3:
        cost= 1000*days -500
    else:
        cost = 1000*days
    return cost
def trip_cost(city, days):
    return hotel_cost(nights)+plane_ride_cost(city)+rental_car_cost(days)

def trip_cost_mod(city, days, spending_money):
    return hotel_cost(nights)+plane_ride_cost(city)+rental_car_cost(days)+ spending_money

