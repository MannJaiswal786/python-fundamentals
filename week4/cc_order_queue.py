class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        return None

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
         if flavor not in self.flavors:
             print("Sorry, we do not have that flavor")
             return
         if scoops < 1 or scoops > 3:
             print("Scoops must be between 1 and 3")
             return
        
         order = {"customer": customer, "flavor": flavor, "scoops": scoops }
         self.orders.enqueue(order)
         print("Order Created")

    def show_all_orders(self):
             if self.orders.is_empty():
                 print("No orders in the queue")
             else:
                 for order in self.orders.items:
                     print(order)

    def next_order(self):
        order = self.orders.dequeue()
        if order:
            print("Next Order:", order)
        else:
            print("No more orders in the queue")

shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()