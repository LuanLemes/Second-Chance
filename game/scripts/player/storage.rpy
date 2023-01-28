init python:
    class Inventory():
        def __init__(self, items, no_of_items):
            self.items = items
            self.no_of_items = no_of_items

        def add_item(self, item):
            if item in self.items:
                self.no_of_items += 1
                item.add_quantity()
            else:
                self.items.append(item)
                item.add_quantity
                self.no_of_items += 1

        def remove_item(self, item):
            self.items.remove(item)
            # self.no_of_items -= 1

        def list_items(self):
            x = 1
            if len(self.items) < 1:
                return
            else:
                for item in self.items:
                    mc(item.name)
                    x = x+1

    player_inventory = Inventory([], 0)

    class InventoryItem():
        def __init__(self, id, name, type, is_active, buy_price, sell_price, quantity, rarity, description):
            self.name = name
            self.is_active = is_active
            self.buy_price = buy_price
            self.sell_price = sell_price
            quantity = quantity
            self.description = description
            self.add_to_player_inventory()

        def add_quantity(self):
            self.quantity += 1

        def remove_quantity(self, quantity):
            if item > 0:
                self.quantity -= 1
        def add_to_player_inventory(self):
            player_inventory.add_item(self)

    def start_inventory_items():
        # rarity 0 commom  1 uncomom 2 rare, 3 very rare epic
        #   Flowers
        lily = InventoryItem( 0, "Lily", "Flower", True, 10, 7, 0, 1,"Lilium. Tall, majestic and strikingly-shaped")
        rose = InventoryItem(1, "Rose", "Flower", True, 25 ,15,0 , 2, "Rosa. Perhaps the most famous flower on the list")
        tulip = InventoryItem(2, "Tulip", "Flower", True, 7, 3, 0, 0, "Tulipa. Closely related to the lily and with a long history of cultivation.")
        carnation = InventoryItem(3, "Carnation", "Flower", True, 5, 2, 0, 0, "Scientific Name: Dianthus.")
        freesia = InventoryItem(4, "Freesia", "Flower", True, 8, 4, 0, 0, "What we call freesias are actually cultivated hybrids.")
        sunflower = InventoryItem(6, "Sunflower", "Flower", True, 12, 8, 0, 1, "known for its bright and cheery bloom.")
        uncommon_orchid = InventoryItem(7, "Common Orchid", "Flower", True, 28, 20, 0, 2, "known for its bright and cheery bloom.")
        rare_orchid = InventoryItem(8, "Rare Orchid", "Flower", True, 50, 35, 0, 3,"known for its bright and cheery bloom.")
        blood_rose = InventoryItem(9, "blood_rose", "Flower", True, 150, 100, 0, 4,"A Very rare rose when the seed is \"watered\" by the blood of a magic creature")
    #   Herbs
        test_herb = InventoryItem(50, "blood_rose", "Herb", True, 150, 100, 0, 4,"")
        test_herb = InventoryItem(51, "um pirocão", "Herb", True, 150, 100, 0, 4,"")
