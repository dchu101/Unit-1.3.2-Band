class Bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

class BikeShops(object):        
    def __init__(self, shop, inventory, margin, profit):
        
        self.shop = shop
        self.inventory = {}
        self.margin = margin
        
        self.profit = 0

class Customers(object):
    def __init__(self,customer, funds, bikeowned):
        self.custname = custname
        self.funds = funds
        self.bikeowned = None
        
    # Can buy and own a new bicycle

