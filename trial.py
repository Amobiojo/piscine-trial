def item_cost(first, second):
    return first + second

def travel_cost(fair, trips):
    total = fair * trips
    return total
print(travel_cost(200, 3))

def budget_left(budget, food, transpot):
    remaining = budget - food - transpot
    return remaining
print(budget_left(10000, 6000, 3200))


def particapant_cost(attendees, food, transport):
    particapant_cost = attendees * (food + transport)
    return particapant_cost

print(particapant_cost(10, 2000, 500))


def welcome(name, days):
    return f"Welcome {name}, Trial length is {days} days."
message = welcome("Usman Amobiojo", 5)
print(message)


def budget_message(name, remaining):
    return f"{name} has {remaining} naira remaining"
message = budget_message("Usman", 500)
print(message)

def budget_message(name, remaining):
    return f"{name} has {remaining} naira remaining" 
message = budget_message("Ada", 500)
print(message)

def welcome_message(name):
    return f"Welcome {name}."
message = welcome_message('Ada')
print(message)

# Complete learner_status(name, tasks) to return exactly 
# "Ada completed 4 tasks." Use the supplied values and keep 
# the word tasks even when the value is 1.

def learner_status(name, tasks):
    return f"{name} completed {tasks} tasks"
output = learner_status('Ada', 4)

print(output)


def greetings():
    return "Hi"
response = greetings()

print(response)




def budget_cost(budget, cost):
    if budget >= cost: return "enough"
    else: return "not enough"
    

def items_list(*items):
    items = list(items)
    return items(0)

def items_list(*items):
    items = list(items)
    return items(0)

def check_budget(budget, cost):
    if budget >= cost:
        return "Enough money"
    else:
        return "Not enough money"


def can_afford(budget, cost):
    return budget >= cost
print(can_afford(10, 10))

def can_afford(budget, cost):
    return budget >= cost
print(can_afford(10, 20))

def matches_expected(actual, expected):
    return actual == expected
print(matches_expected(40, 20))

def matches_expected(actual, expected):
    return actual == expected
print(matches_expected(40, 40))

def funding_status(budget, cost):
    if budget >= cost:
        return "Enough"
    else: 
        return "Not enough"
    
print(funding_status(2000, 3000))

def funding_status(budget, cost):
    if budget >= cost:
        return "Enough"
    else: 
        return "Not enough"
    
print(funding_status(2000, 1230))

def funding_status(budget, cost):
    if budget == cost:
        return "Enough"
    else: 
        return "Not enough"
    
print(funding_status(1000, 1000))

def booking_status(capacity, booked):
     if booked <= capacity:
          return "Fits"
     else: 
          return "Too many"
print(booking_status(10, 7))

def booking_status(capacity, booked):
     if booked <= capacity:
          return "Fits"
     else: 
          return "Too many"
print(booking_status(7, 10))

def space_status(places):
   if places > 0:
      return "Available"
   else:
      return "Full"
print(space_status(10))

def space_status(places):
    if places >0:
        return "Available"
    else:
        return "Not Available"
print(space_status(0))


 
def budget_left(budget, food, transpot):
    remaining = budget - food - transpot
    return remaining
print(budget_left(10000, 12000, 3200))


# Event Budget Helper 

#Build a working Event Budget Helper that can: calculate participant-related costs;add 
#the venue cost to get the total event cost;
#decide whether the event is within budget; return a clear event summary.

#Fucntions to use 
#def participant_cost(attendees, food_per_person, transport_per_person):
#def event_total(attendees, food_per_person, transport_per_person, venue_cost):
#def budget_status(budget, total):
#def event_summary(event_name, total, status):
  
def participant_cost(attendees, food_per_person, transport_per_person):
    return attendees *(food_per_person + transport_per_person)

def event_total(attendees, food_per_person, transport_per_person, venue_cost):
    return attendees *(food_per_person + transport_per_person + venue_cost)

def budget_status(budget, event_total):
    return budget - event_total


print(particapant_cost(10, 2000, 1000))
print(event_total(10, 2000, 1000, 20000))
print(budget_status(200000, 230000))


# Event Budget Helper 

#Build a working Event Budget Helper that can: calculate participant-related costs;add 
#the venue cost to get the total event cost;
#decide whether the event is within budget; return a clear event summary.

#Fucntions to use 
#def participant_cost(attendees, food_per_person, transport_per_person):
#def event_total(attendees, food_per_person, transport_per_person, venue_cost):
#def budget_status(budget, total):
#def event_summary(event_name, total, status):


def participant_cost(attendees, food_per_person, transport_per_person):
    return attendees * (food_per_person + transport_per_person)

def event_total(attendees, food_per_person, transport_per_person, venue_cost):
    people = participant_cost(attendees, food_per_person, transport_per_person)
    return people + venue_cost

def budget_status(budget, total):
    if total <= budget:
        return "Within budget"
    elif total < budget:
        return "Below budget"
    elif total == budget:
        return "Exact budget"
    else:
        return "Over budget"

def event_summary(event_name, total, status):
    return f"{event_name}: total {total} - {status}"

total = event_total(20, 2000, 500, 30000)
status = budget_status(100000, total)

print(event_summary("Learn2earn trial", total, status))

#Write a function called first_item that accepts any number of items and returns the first item.

def first_item(*items):
    items = list(items)
    return items[0]
print(first_item("bread", "millo", "sugar"))

def first_item(*items):
    items = list(items)
    return items[1]
print(first_item("bread", "millo", "sugar"))



def first_item(*items):
    items = list(items)
    return items[-1]
print(first_item("bread", "millo", "sugar"))



def first_item(*items):
    items = list(items)
    return items[-2]
print(first_item("bread", "millo", "sugar", "candle", "tin"))

