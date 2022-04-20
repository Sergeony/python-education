"""Restaurant chain

-This module is designed to simulate a restaurant business with OOP paradigm.
-It provides many actions on components of its.
-There are many classes which have different relations with each other,
so you can create your own employees and hire them or fire out.
-The user interface provides you to manipulate customers when the program
is running. Employees manipulation is automated, but you're always able to
config it for yourself.
"""
from abc import ABC, abstractmethod
from random import choice


class Employee(ABC):
    """An abstract restaurant employee."""

    @abstractmethod
    def __init__(self, name) -> None:
        """Set options common to all positions."""
        self.__name = name
        self.place_of_work = None

    @property
    def name(self):
        return self.__name


class Cooker(Employee):
    """A person responsible for cooking."""

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def cook(self, order_id: int) -> str:
        """Prepare the order that the chef instructed you
        and return dishes(in string form) him.
        """
        p_o_w = self.place_of_work

        # Change actor in print depending on who is cooking:
        if isinstance(self, Chef):
            print(f"Chef {self.name} is cooking for you...")
        else:
            print(f"Cooker {self.name} is cooking for you...")

        cooked_dishes = ""
        for item_id in p_o_w.storage.get('order')[order_id].items:
            cooked_dishes += f"{p_o_w.menu.items[item_id].title}, "

        return cooked_dishes


class Chef(Cooker):
    """A person responsible for cookers and menu planning."""

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def cook(self, order_id: int) -> str:
        """Do the same as just a cooker but with an addition dish."""
        return super(Chef, self).cook(order_id) + "compliment from the chef"

    def appoint_cooker(self, order_id: int) -> str:
        """Randomly choose a cooker or do it by yourself
         if the customer has made orders for times_to_get_compliment
         and return to the waiter.
        """
        p_o_w = self.place_of_work

        print(f"Chef {self.name} is deciding who'll cook...")

        if p_o_w.storage.get('order')[order_id].owner.orders_count == p_o_w.times_to_get_compliment:
            # Reset counter
            p_o_w.storage.get('order')[order_id].owner.orders_count = 0

            cooked_order = self.cook(order_id)
        else:
            randomly_chosen_cooker_id = choice(list(p_o_w.storage['cooker'].keys()))
            cooked_order = p_o_w.storage.get('cooker')[randomly_chosen_cooker_id].cook(order_id)

        print(f"Chef {self.name} returns cooked order to waiter...")
        return cooked_order

    def modify_menu(self,
                    action: int,
                    item_title: str = None,
                    item_id: int = None,
                    item_price: int = None) -> None:
        """Do one of 3 actions:
            0 - add item: requires item_title and item_price
            1 - del item: requires item_id
            2 - update item: requires item_id and item_price
        """
        p_o_w = self.place_of_work

        if action == 0:
            p_o_w.menu.add_item(item_title, item_price)

        elif action == 1:
            p_o_w.menu.del_item(item_id)

        elif action == 2:
            p_o_w.menu.update_item(item_id, item_price)

        else:
            print("Entered action isn't correct!")


class Waiter(Employee):
    """A person responsible for taking an order."""

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def take_order(self, order_id: int) -> str:
        """Take the order and give it to the chef, and when it's ready,
        bring it to the customer or send a randomly chosen courier.
        """
        p_o_w = self.place_of_work

        print(f"Waiter {self.name} is giving order to the chef...")

        cooked_order = p_o_w.chef.appoint_cooker(order_id)

        order_address = p_o_w.storage.get("order")[order_id].address
        if order_address is None:
            print(f"Waiter {self.name} is bringing order to you...")
            return cooked_order

        print(f"Waiter {self.name} is sending courier to you...")
        couriers = p_o_w.storage.get('courier')
        randomly_chosen_courier = couriers[choice(list(couriers.keys()))]
        return randomly_chosen_courier.deliver_order(cooked_order, order_address)


class Courier(Employee):
    """A person responsible for the delivery of an order."""

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def deliver_order(self, delivery: str, address: str) -> str:
        """Deliver the order to the specified address."""
        print(f"Courier {self.name} is delivering your order to {address}...")
        return delivery


class Restaurant:
    """A master class, responsible for making and storage employees
    and everything related to the establishment.
    """

    def __init__(self, chef: Chef, cooker: Cooker, waiter: Waiter, courier: Courier) -> None:
        """Build a new restaurant,
        including hiring working staff
        and creating of necessary things.
        """

        # restaurant characteristics
        self.times_to_get_compliment = 2
        self.__money = 0

        # restaurant components that exist in one instance:
        self.chef = chef
        self.menu = Menu()

        # restaurant components that exist in many instances'
        # cooker, waiter, courier - at least one, because they are necessary for work:
        self.storage = {
            "cooker": {1: cooker},
            "waiter": {1: waiter},
            "courier": {1: courier},
            "order": {},
            "customer": {},
        }

        # counters for components that exist in many instance:
        self.counter = {
            "cooker": 1,
            "waiter": 1,
            "courier": 1,
            "order": 0,
            "customer": 0,
        }

        # set place of work for starter working stuff
        for employee in (chef, cooker, waiter, courier):
            self.set_place_of_work(employee)

    def generate_id(self, object_type_name) -> int:
        """Take the current object counter and
        increase it by 1 to return the new object id.
        """
        self.counter[object_type_name] += 1
        return self.counter[object_type_name]

    def append(self, object_to_storage) -> int:
        """Get string name of object class(to access by dict key in storage),
        create id for it and push it to the storage. Return the object id, after all.
        """
        object_type_name = type(object_to_storage).__name__.lower()

        new_id = self.generate_id(object_type_name)

        self.storage.get(object_type_name)[new_id] = object_to_storage

        # Special case for order appending - using recursion
        # Add an order customer to storage too, if he's not already in it:
        values = self.storage.get("customer").values()
        if object_type_name == "order" and object_to_storage.owner not in values:
            self.append(object_to_storage.owner)

        return new_id

    def delete(self, object_to_delete) -> None:
        """Get an object and remove it from a storage,
        exactly the opposite to append, but return None.
        """
        object_type_name = type(object_to_delete).__name__.lower()
        objects = self.storage.get(object_type_name)

        for obj_id, obj_value in objects.items():
            if obj_value == object_to_delete:
                objects.pop(obj_id)
                break

    def take_payment(self, order_id: int) -> None:
        """Take payment from a customer for an order
        and remove the order from a storage.
        """
        order = self.storage.get("order")[order_id]
        self.__money += order.cost
        self.delete(order)

    def set_place_of_work(self, employee: Employee) -> None:
        """Give link to my class for each employee who works for me."""
        employee.place_of_work = self


class Customer:
    """A person who visits restaurants."""

    def __init__(self):
        """Initiate necessary attributes to be able to make an order."""
        self.__my_dishes = ""
        self.__restaurant = None
        self.__address = None
        self.orders_count = 0

    @property
    def restaurant(self) -> Restaurant:
        return self.__restaurant

    @property
    def address(self) -> str:
        return self.__address

    def visit_restaurant(self, restaurant: Restaurant, address: str = None) -> None:
        """Choose the restaurant and type of visiting.
        It's None by default which means to visit inplace."""
        self.__restaurant = restaurant
        self.__address = address

    def change_restaurant(self, restaurant: Restaurant, address: str = None) -> None:
        """Leave current restaurant and visit other one."""
        self.__restaurant.delete(self)
        self.orders_count = 0
        self.__address = address
        self.__restaurant = restaurant

    def eat(self) -> str:
        """Eat my_dishes and return it(in string form)."""
        self.__my_dishes = ""
        return "I'm eating..."

    def see_menu(self) -> None:
        """See available dishes."""
        self.__restaurant.menu.show_items()

    def make_order(self, order_items: list) -> None:
        """Create the order, then randomly choose a waiter,
        also pay after receiving and add received order to your dishes.
        """
        self.orders_count += 1

        order_id = self.__restaurant.append(Order(self, order_items))

        waiters = self.__restaurant.storage.get("waiter")
        randomly_chosen_waiter = waiters[choice(list(waiters.keys()))]
        received_order = randomly_chosen_waiter.take_order(order_id)

        self.pay_for_order(order_id)

        self.__my_dishes += received_order

    def pay_for_order(self, order_id) -> None:
        """Just paying for the order."""
        self.__restaurant.take_payment(order_id)


class Order:
    """A customer's request to a restaurant."""

    def __init__(self, owner: Customer, items: list):
        """Initiate necessary attributes."""
        self.__owner = owner
        self.__items = items
        self.__address = owner.address

        self.__cost = 0
        for item in self.items:
            self.__cost += self.owner.restaurant.menu.items[item].price

    @property
    def items(self) -> list:
        return self.__items

    @property
    def owner(self) -> Customer:
        return self.__owner

    @property
    def address(self) -> str:
        return self.__address

    @property
    def cost(self) -> int:
        return self.__cost


class Menu:
    """A composite class that implements actions on dishes."""

    def __init__(self) -> None:
        """Initiate a storage to keep items in it, like a restaurant keeps its."""
        self.__item_counter = 0
        self.items = {}

    def add_item(self, title: str, price: int) -> None:
        """Create a new dish, storage it and increase counter by 1."""
        self.items[self.__item_counter] = MenuItem(title, price)
        self.__item_counter += 1

    def show_items(self) -> None:
        """Read dishes"""
        for item_id, item_value in self.items.items():
            print(f"{item_id}) {item_value}")

    def update_item(self, item_id: int, new_price: int) -> None:
        """Update the dish price"""
        self.items[item_id].set_price(new_price)

    def del_item(self, item_id: int) -> None:
        """Delete the dish"""
        del self.items[item_id]


class MenuItem:
    """A dish on menu"""

    def __init__(self, title: str, price: int) -> None:
        """Initiate necessary attributes."""
        self.__title = title
        self.__price = price

    @property
    def price(self) -> int:
        """Get a price, used to calculate an order cost."""
        return self.__price

    @price.setter
    def price(self, new_price: int) -> None:
        """Set a new price, used when a chef is modifying a menu."""
        self.__price = new_price

    @property
    def title(self) -> str:
        """Get the dish, used when a cooker is preparing an order."""
        return self.__title

    def __str__(self) -> str:
        """Represent dish in string form, used to be show in a menu."""
        return f"{self.__title} : {self.__price} UAH"


# Open the first restaurant
chef_1 = Chef("Rick")
cooker_1 = Cooker("Marry")
waiter_1 = Waiter("John")
courier_1 = Courier("Morty")
claude_monet = Restaurant(chef_1, cooker_1, waiter_1, courier_1)

# Make menu
claude_monet.menu.add_item("soup", 50)
claude_monet.menu.add_item("foie gras", 150)
claude_monet.menu.add_item("ice cream", 30)

# Create one customer
customer_1 = Customer()

# Visit our restaurant
customer_1.visit_restaurant(claude_monet, "baker street")

# Chef modifies menu
chef_1.modify_menu(0, item_title="cheese cake", item_price=60)
chef_1.modify_menu(1, item_id=1)

# Start action
while True:

    print(f"for each {claude_monet.times_to_get_compliment} "
          f"order you will receive the compliment from chef.")

    if int(input("Would you like to see the menu?(1 - yes, 0 - no): ")):
        customer_1.see_menu()

    items_to_order = list(map(int, input("Enter menu item IDs( 0 2 ...):").split()))

    customer_1.make_order(items_to_order)

    if int(input("Enter 1 to continue and 0 to finish:")):
        print("#"*70)
    else:
        break

# It's also possible to open yet one restaurant
chef_2 = Chef("Kate")
cooker_2 = Cooker("Jack")
waiter_2 = Waiter("Margo")
courier_2 = Courier("Lisa")
rest_2 = Restaurant(chef_2, cooker_2, waiter_2, courier_2)
