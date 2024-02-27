class Item:
    def __init__(self, itemName: str, itemCount: int, itemPrice: float):
        self.itemName = itemName
        self.itemCount = itemCount
        self.itemPrice = itemPrice

class Details:
    def __init__(self):
        self.items = []

    def getName(name: str, self):
        self.name = name

    def getAddr(addr: str, self):
        self.addr = addr

    def addItem(itemName: str, itemCount: int, itemPrice: float, self):
        item = Item(itemName, itemCount, itemPrice)
        self.items.append(item)

    def getItems(self):
        return self.items

class Total:
    def __init__(self, taxRate: float):
        self.taxRate = taxRate

    def findTotal(cart, validator, inventory, self):
        validator.validate(inventory, cart.items)
        if validator.valid == True:
                subtotal = sum(item.itemPrice for item in cart.items)
                tax = subtotal * self.taxRate
                return subtotal + tax

class Validation:
    def __init__(self):
        self.valid == True

    def validate(inventory, items, self):
        for item in inventory:
            for item2 in items:
                if item.itemName == item2.itemName:
                    if item.itemCount < item2.itemCount:
                        self.valid == False

class Confirmation:
    def __init__(self, email_service: str):
        self.email_service = email_service

    def sendEmail(validator, email, self):
        if validator.valid == True:
            self.email_service.send_email(email, "Order Confirmed")

class Inventory:
    def __init__(self):
        self.inventory = []

    def addStock(itemName: str, itemCount: int, itemPrice: float, self):
        item = Item(itemName, itemCount, itemPrice)
        self.inventory.append(item)

    def remStock(itemName: str, itemCount: int, self):
        for item in self.inventory:
            if item.itemName == itemName:
                item.itemCount -= itemCount
                if item.itemCount == 0:
                    self.inventory.pop(item)


def main():
    inv = Inventory()
    conf = Confirmation("gmail")
    validator = Validation
    total = Total(0.05)
    cart = Details()

    inv.addStock("Socks", 5, 3.50)
    print("Test Succeed")

if __name__ == "__main__":
    main()