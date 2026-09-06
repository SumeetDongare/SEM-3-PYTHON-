"""PART 3 — DESIGN PATTERNS
Comprehensive Practice Question 3

Create a Food Delivery Application that demonstrates all four design patterns taught in your PDF:

Singleton
Factory
Observer
Strategy
A. Singleton Pattern — Application Configuration

Create:

AppConfig

The application must have only one AppConfig object.

Example:

config1 = AppConfig()
config2 = AppConfig()

print(config1 is config2)

Expected:

True

Store something such as:

app_name
version

inside the singleton.

B. Factory Pattern — Create Food Items

Create different food classes:

Pizza
Burger
Biryani

Each should have:

prepare()

with different output.

Create:

FoodFactory

which decides which object to create.

For example:

food = FoodFactory.create_food("pizza")
food.prepare()

Output:

Preparing Pizza

The client should not need to directly create Pizza(), Burger(), etc.

C. Observer Pattern — Order Notification

Create:

Order

as the subject.

Create:

Customer

as the observer.

The order should allow:

subscribe()
unsubscribe()
notify()

When order status changes:

Order Placed
Preparing
Out for Delivery
Delivered

all subscribed customers should receive the notification.

Example:

order.subscribe(customer1)
order.subscribe(customer2)

order.update_status("Out for Delivery")

Expected idea:

Customer 1 received: Out for Delivery
Customer 2 received: Out for Delivery
D. Strategy Pattern — Payment

Create different payment strategies:

UPIPayment
CardPayment
CashPayment

Each should implement:

pay(amount)

Create a context:

Payment

which accepts a payment strategy.

Example:

payment = Payment(UPIPayment())
payment.pay(500)

Then change the strategy:

payment.set_strategy(CardPayment())
payment.pay(500)

The same Payment object should now use a different algorithm.

E. Final Integration

Now combine everything.

Your application should work approximately like this:

                 FOOD DELIVERY APP
                        |
        ┌───────────────┼───────────────┐
        ↓               ↓               ↓
    Singleton         Factory        Observer
    AppConfig       Food Creation    Notifications
                                        |
                                        ↓
                                   Customers
                                        
                        ↓
                    Strategy
                     Payment

Example flow:

config = AppConfig()

food = FoodFactory.create_food("pizza")

order = Order()

customer1 = Customer("Rahul")
customer2 = Customer("Priya")

order.subscribe(customer1)
order.subscribe(customer2)

order.update_status("Order Placed")

payment = Payment(UPIPayment())
payment.pay(500)

Then change payment strategy:

payment.set_strategy(CardPayment())
payment.pay(500)"""

# ============================================================
# 1. Singleton Design Pattern :- The Singleton Design Pattern ensures that a class can create only one object, and everyone uses that same object.
# ============================================================
class Application_config:
    _instance = None  #class variable
                                                 #self → refers to the object #cls → refers to the class
    def __new__(cls):                            #__new__() runs when an object is being created control object creation
        if cls._instance is None:
            cls._instance = super().__new__(cls) #Call the parent class's __new__() method to actually create a new object of the cls class.
        return cls._instance

    def __init__(self):
        self.app_config = "My_app"
        self.version = "v.1.0"

obj1 = Application_config()
obj2 = Application_config()

print(obj1 is obj2)
print(f"Application configuration is:{obj1.app_config}\nApplication version is:{obj2.version}")

# ============================================================
# 2.Factory Design Pattern :- Factory Pattern is a design pattern where a factory class decides and creates the required object, so the client does not need to directly create it.
# ============================================================

class pizza:
    def create(self):
        print("Baking pizza")

class burger:
    def create(self):
        print("Making burger")

class biryani:
    def create(self):
        print("surving biryani")

class Hotel:
    @staticmethod
    def order(item):
        match item.lower():
            case "pizza":
                return pizza()
            case "burger":
                return burger()
            case "biryani":
                return biryani()
            case _:
                print("Invalid item")
                return None

a =input("Enter item name:")
obj3 = Hotel.order(a)
if obj3:
    obj3.create()
            
# ============================================================
# 3.Observer Design Pattern :-  Observer Pattern allows all subscribed Customer objects to automatically receive updates when the Order object's state, such as status, changes from "Preparing" to "Out for Delivery".
# ============================================================
class Observer:
    def __init__(self,name):
        self.name = name

    def update(self,status):
        self.status = status
        print(f"{self.name} order status is {self.status}")

class subject:
    def __init__(self):
        self.customer = []
        self.status = None

    def add_customer(self,customer):
        self.customer.append(customer)

    def remove_customer(self,customer):
        self.customer.remove(customer)

    def notify(self):
        for customer in self.customer:
            customer.update(self.status)

    def update_status(self,status):
        self.status = status
        self.notify()

customer1 = Observer("Customer1")
customer2 = Observer("Customer2")

order = subject()

order.add_customer(customer1)
order.add_customer(customer2)

order.update_status("Baking")