from SeedStoryDBConnection import create_connection, create_database, create_table, insert_sample_data

class SeedDetails:
    def __init__(self, SeedID, SeedName, Weeks, SeedBreeder, NetWt, Sales, Price, InStock):
        self.SeedID = SeedID
        self.SeedName = SeedName
        self.Weeks = Weeks
        self.SeedBreeder = SeedBreeder
        self.NetWt = NetWt
        self.Sales = Sales
        self.Price = Price
        self.InStock = InStock

    def display_info(self):
        print(f"{self.SeedName:<15} {self.Weeks:<15} {self.SeedBreeder:<20} {self.NetWt:<15} {self.Sales:<15} {self.Price:<15,.2f} {self.InStock:<5}")


class Inventory:
    def __init__(self):
        self.stocks = []
        self.load_inventory()

    def load_inventory(self):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Seeds")
            seeds = cursor.fetchall()

            for seed in seeds:
                SeedID, SeedName, Weeks, SeedBreeder, NetWt, Price, Sales, InStock = seed
                self.stocks.append(SeedDetails(SeedID, SeedName, Weeks, SeedBreeder, NetWt, Price, Sales, InStock))

            cursor.close()
            connection.close()

    def display_item_header(self):
        print("-" * 120)
        print(f"{'SEED NAME':<15} {'WEEKS(Growth)':<15} {'SEED BREEDER':<20} {'NET WT(g)':<15} {'SALES(pw)':<15} {'PRICE(PHP)':<15} {'STOCK':<5}")
        print("-" * 120)

    def display_by_SeedName(self):
        self.display_item_header()
        for seed in sorted(self.stocks, key=lambda x: x.SeedName):
            seed.display_info()
        self.display_item_header()
            
    def display_by_Weeks(self):
        self.display_item_header()
        for seed in sorted(self.stocks, key=lambda x: x.Weeks):
            seed.display_info()
        self.display_item_header()

    def display_by_Sales(self):
        self.display_item_header()
        for seed in sorted(self.stocks, key=lambda x: x.Sales, reverse = True):
            seed.display_info()
        self.display_item_header()

    def SeedName_finder(self, SeedName):
        for seed in self.stocks:
            if seed.SeedName.lower() == SeedName.lower():
                return seed
        return None
    
    def update_stock_in_db(self):
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                for seed in self.stocks:
                    sql = "UPDATE Seeds SET InStock = %s WHERE SeedID = %s"
                    cursor.execute(sql, (seed.InStock, seed.SeedID))
                connection.commit()
                print("Stock updated.")

            except mysql.connector.Error as err:
                print(f"Error updating stock in database: {err}")
                connection.rollback()
                
            finally:
                cursor.close()
                connection.close()


class ShoppingCart:
    def __init__(self, inventory):
        self.cart = []
        self.subtotal = 0
        self.inventory = inventory

    def add_to_cart(self, SeedName, Sales_added):
        if Sales_added <= 0:
            print("Invalid quantity.")
            return

        seed = self.inventory.SeedName_finder(SeedName)
        if seed:
            if seed.InStock < Sales_added:
                print(f"Only {seed.Sales} available.")
            else:
                self.cart.append((seed, Sales_added))
                seed.InStock -= Sales_added
                self.subtotal += seed.Price * Sales_added
                print(f"\n{Sales_added} {seed.SeedName}(s) added.")
                self.inventory.update_stock_in_db()
        else:
            print("Seed not found.")

    def display_cart_details(self, discount, total):
        print("-" * 120)
        print(f"{'SEED NAME':<15} {'SEED BREEDER':<20} {'PRICE(PHP)':<15} {'QUANTITY':<15} {'TOTAL(PHP)':<10}")
        print("-" * 120)
        for seed, qty in self.cart:
            print(f"{seed.SeedName:<15} {seed.SeedBreeder:<20} {seed.Price:<15,.2f} {qty:<15} {seed.Price * qty:<10,.2f}")
        print("-" * 120)
        print(f"Subtotal: PHP {self.subtotal:,.2f}")
        print(f"Discount: -PHP {discount:,.2f} (5% off for 5 or more items)")
        print(f"Total: PHP {total:,.2f}")

    def shopping_cart_list(self, discount, total):
        print("\n" + "-" * 120)
        print("CART - SEEDSTORY")
        self.display_cart_details(discount, total)
        print("-" * 120)

    def process_payment(self):
        discount = self.subtotal / 20 if len(self.cart) >= 5 else 0
        total = self.subtotal - discount

        while True:
            try:
                print("-" * 120)
                payment = float(input(f"Enter payment (Total: PHP {total:,.2f}): "))
                if payment < total:
                    print("Insufficient amount. Please try again.\n")
                    continue

                change = payment - total

                print("\nPayment successful.")

                print("\nRECEIPT - SEEDSTORY")
                print("-" * 120)
                self.display_cart_details(discount, total)
                print(f"Cash: PHP {payment:,.2f}")
                print(f"Change: PHP {change:,.2f}")
                print("-" * 120)

                self.clear_cart()
                break

            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def checkout(self):
        if len(self.cart) == 0: 
            print("\nCart is empty.")
            return

        discount = self.subtotal / 20 if len(self.cart) >= 5 else 0
        total = self.subtotal - discount

        print("\nCART SUMMARY - SEEDSTORY")
        self.display_cart_details(discount, total)

        while True:
            proceed_payment = input("\nProceed to payment? (yes/no): ").strip().lower()
            if proceed_payment == 'yes':
                self.process_payment()
                break
            elif proceed_payment == 'no':
                print("Returning to the main menu.")
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

    def clear_cart(self):
        self.cart.clear()
        self.subtotal = 0

class Sorting:
    @staticmethod
    def sorting_options(inventory, cart):
        while True:
            print("\n--------Sort Products By:--------")
            print("(1) Name (A-Z)")
            print("(2) Growth Duration (Weeks)")
            print("(3) Weekly Sales")
            print("\n(4) BACK")
            print("---------------------------------")

            try:
                choice = int(input("Your choice (1-4): "))
                if choice not in [1, 2, 3, 4]:
                    print("Select from (1-4).")
                    continue

            except ValueError:
                print("Select from (1-4).")
                continue

            print("")

            if choice == 1:
                Sorting.sort_by_SeedName(inventory, cart)
            elif choice == 2:
                Sorting.sort_by_Weeks(inventory, cart)
            elif choice == 3:
                Sorting.sort_by_Sales(inventory, cart)
            elif choice == 4:
                break

    @staticmethod
    def sort_by_Sales(inventory, cart):
        inventory.display_by_Sales()
        Sorting.prompt_to_add_to_cart(inventory, cart)

    @staticmethod
    def sort_by_SeedName(inventory, cart):
        inventory.display_by_SeedName()
        Sorting.prompt_to_add_to_cart(inventory, cart)

    @staticmethod
    def sort_by_Weeks(inventory, cart):
        inventory.display_by_Weeks()
        Sorting.prompt_to_add_to_cart(inventory, cart)

    @staticmethod
    def prompt_to_add_to_cart(inventory, cart):
        while True:
            add_to_cart = input("\nAdd an item to cart? (yes/no): ").strip().lower()
            if add_to_cart == "yes":
                SeedName = input("Enter seed name to add to cart: ").strip()
                Sales_added = int(input(f"Enter quantity to add: "))
                cart.add_to_cart(SeedName, Sales_added)
                break
            elif add_to_cart == "no":
                break
            else:
                print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    connection = create_connection()
    if connection:
        create_database(connection)
        create_table(connection)
        insert_sample_data(connection)
    
    inventory = Inventory()
    cart = ShoppingCart(inventory)

    while True:
        print("\n-----------MAIN MENU-------------")
        print("(1) Browse Products")
        print("(2) View Cart and Checkout")
        print("\n(3) Exit")
        print("---------------------------------")

        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                Sorting.sorting_options(inventory, cart)
            elif choice == 2:
                cart.checkout()
            elif choice == 3:
                print("Exited SeedStory.")
                break
            else:
                print("Select from (1-3).")

        except ValueError:
            print("Select from (1-3).")
