import mysql.connector

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",      
            password="",      
            database="SeedStory"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None


def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS SeedStory")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")


def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Seeds (
                SeedID INT AUTO_INCREMENT PRIMARY KEY,
                SeedName VARCHAR(50) NOT NULL,
                Weeks INT,
                SeedBreeder VARCHAR(50) NOT NULL,
                NetWt INT,
                Sales INT,
                Price INT,
                InStock INT
            )
        """)
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")


def insert_sample_data(connection):
    try:
        cursor = connection.cursor()

        products = [
            ('Tomato', 8, 'Burpee', 120, 25, 45, 4980),
            ('Cucumber', 6, 'Ferry-Morse', 150, 30, 40, 3500),
            ('Carrot', 10, 'Burpee', 100, 20, 50, 2000),
            ('Lettuce', 5, 'Seedsman', 60, 35, 30, 4500),
            ('Spinach', 6, 'Burpee', 75, 28, 35, 4700),
            ('Cabbage', 9, 'Ferry-Morse', 175, 15, 55, 3200),
            ('Pepper', 7, 'Bonnie Plants', 130, 22, 48, 4100),
            ('Onion', 8, 'Burpee', 140, 20, 38, 5000),
            ('Potato', 10, 'Gurney', 160, 18, 60, 3900),
            ('Zucchini', 7, 'Burpee', 110, 25, 42, 4600),
            ('Rose', 12, 'Jackson & Perkins', 75, 5, 30, 1500),
            ('Tulip', 8, 'American Meadows', 90, 10, 20, 3000),
            ('Daffodil', 14, 'Bulb Company', 100, 7, 25, 2700),
            ('Sunflower', 8, 'Burpee', 70, 18, 15, 4200),
            ('Chrysanthemum', 10, 'Burpee', 50, 12, 28, 1800),
            ('Lavender', 12, 'Seedsman', 60, 8, 18, 2300),
            ('Peony', 15, 'Park Seed', 80, 4, 45, 2000),
            ('Violet', 6, 'Burpee', 90, 20, 12, 3000),
            ('Geranium', 10, 'Bonnie Plants', 110, 15, 22, 1800),
            ('Marigold', 6, 'American Meadows', 50, 25, 12, 3300),
            ('Iris', 12, 'Blossom Hill', 100, 10, 18, 2400),
            ('Daisy', 8, 'Jackson & Perkins', 80, 18, 22, 2200),
            ('Aster', 10, 'Ferry-Morse', 70, 14, 19, 2100),
            ('Pansy', 6, 'Burpee', 75, 22, 16, 4000),
            ('Orchid', 20, 'David Austin', 55, 3, 75, 1500),
            ('Lily', 12, 'Eden Brothers', 125, 10, 24, 2900),
            ('Magnolia', 14, 'Monrovia', 150, 8, 40, 1700),
            ('Fuchsia', 8, 'Burpee', 95, 16, 15, 3500),
            ('Hibiscus', 10, 'Florida Nursery', 135, 18, 35, 2300),
            ('Crocus', 6, 'Bulb Company', 70, 12, 30, 1500),
            ('Carnation', 8, 'Seedsman', 110, 14, 17, 2800),
            ('Poppy', 8, 'Ferry-Morse', 80, 18, 20, 2200),
            ('Begonia', 12, 'American Meadows', 65, 9, 22, 2700),
            ('Ferns', 16, 'Home Depot', 50, 6, 18, 1500),
            ('Cactus', 12, 'Lowes', 55, 5, 12, 1000),
            ('Eucalyptus', 16, 'Park Seed', 175, 4, 60, 1200),
            ('Wisteria', 20, 'Jackson & Perkins', 150, 3, 50, 1100),
            ('Bougainvillea', 14, 'Burpee', 110, 6, 35, 1400),
            ('Camellia', 12, 'Monrovia', 130, 7, 40, 1600),
            ('Jasmine', 12, 'Bonnie Plants', 115, 6, 45, 1500),
            ('Honeysuckle', 15, 'Burpee', 90, 5, 20, 2100),
            ('Petunia', 8, 'Ferry-Morse', 85, 20, 18, 2500),
            ('Zinnia', 8, 'American Meadows', 100, 25, 12, 3500),
            ('Clematis', 14, 'David Austin', 125, 4, 30, 2200),
            ('Gerbera Daisy', 8, 'Burpee', 95, 12, 25, 2700),
            ('Pothos', 6, 'Home Depot', 120, 10, 15, 2300),
            ('Aloe Vera', 16, 'Lowes', 175, 8, 50, 1900),
            ('Cineraria', 10, 'Park Seed', 130, 14, 17, 2100),
            ('Snapdragon', 10, 'Bonnie Plants', 95, 15, 20, 2200),
            ('Freesia', 12, 'Blossom Hill', 85, 6, 22, 2000),
            ('Lobelia', 6, 'Burpee', 65, 16, 12, 3000),
            ('Morning Glory', 8, 'Ferry-Morse', 70, 18, 16, 2200),
            ('Calla Lily', 10, 'American Meadows', 110, 8, 32, 1800),
            ('Pineapple Sage', 12, 'Lowes', 125, 7, 28, 1500),
            ('Bamboo', 16, 'Home Depot', 175, 4, 40, 2200),
            ('Lavender', 12, 'Burpee', 130, 5, 15, 3000),
            ('Hoya', 14, 'Blossom Hill', 95, 5, 35, 1600),
            ('Yarrow', 12, 'Ferry-Morse', 85, 10, 20, 1800),
            ('Buttercup', 8, 'Burpee', 55, 22, 12, 2400),
            ('Pine', 15, 'Monrovia', 160, 3, 45, 1400),
            ('Cotton', 16, 'Seedsman', 170, 6, 60, 1000),
            ('Mint', 8, 'Burpee', 100, 25, 20, 3200),
            ('Basil', 8, 'Seedsman', 75, 28, 22, 2700),
            ('Thyme', 10, 'Bonnie Plants', 90, 18, 25, 2500),
            ('Chive', 6, 'Ferry-Morse', 130, 30, 18, 3700),
            ('Parsley', 8, 'Lowes', 80, 25, 15, 3900),
            ('Oregano', 9, 'Burpee', 115, 18, 23, 2800),
            ('Rosemary', 10, 'American Meadows', 140, 15, 28, 2200),
            ('Sage', 10, 'Ferry-Morse', 95, 20, 25, 2600),
            ('Chamomile', 12, 'Blossom Hill', 100, 10, 18, 1500),
            ('Lemon Balm', 10, 'Burpee', 120, 15, 20, 1700),
            ('Chili Pepper', 6, 'Park Seed', 140, 35, 28, 2400),
            ('Serrano Pepper', 6, 'Home Depot', 110, 32, 25, 2100),
            ('Bell Pepper', 8, 'Lowes', 95, 28, 30, 2200),
            ('Paprika', 7, 'Seedsman', 105, 27, 22, 2800),
            ('Cilantro', 6, 'Ferry-Morse', 125, 30, 20, 3500),
            ('Celery', 10, 'Bonnie Plants', 150, 20, 22, 2200),
            ('Asparagus', 16, 'Gurneys', 175, 10, 50, 1700),
            ('Radish', 5, 'Burpee', 75, 35, 12, 3300),
            ('Turnip', 8, 'Ferry-Morse', 90, 22, 18, 3100),
            ('Kale', 8, 'Seedsman', 120, 25, 28, 3300),
            ('Squash', 8, 'Bonnie Plants', 155, 30, 20, 3600),
            ('Pumpkin', 10, 'Lowes', 140, 18, 25, 2200),
            ('Okra', 12, 'Home Depot', 95, 15, 28, 2000),
            ('Clover', 10, 'Ferry-Morse', 110, 10, 18, 2500),
            ('Dill', 6, 'Burpee', 60, 20, 12, 2700),
            ('Fenugreek', 10, 'Seedsman', 80, 12, 25, 2400),
            ('Arugula', 6, 'American Meadows', 75, 22, 15, 2800),
            ('Watermelon', 12, 'Bonnie Plants', 175, 8, 50, 3000),
            ('Grapevine', 20, 'Burpee', 160, 5, 60, 2500),
            ('Strawberry', 8, 'Park Seed', 105, 18, 28, 3700),
            ('Blueberry', 12, 'Monrovia', 155, 12, 40, 3200),
            ('Blackberry', 14, 'Burpee', 140, 10, 35, 2900),
            ('Raspberry', 12, 'Bonnie Plants', 125, 14, 32, 3100),
            ('Cranberry', 16, 'Ferry-Morse', 115, 8, 42, 2800),
            ('Mulberry', 20, 'Blossom Hill', 175, 3, 45, 1500),
            ('Fig', 14, 'Eden Brothers', 90, 7, 50, 2200),
            ('Gooseberry', 12, 'Lowes', 135, 6, 30, 2000),
            ('Date Palm', 20, 'Home Depot', 170, 4, 75, 1800),
            ('Coconut', 16, 'Seedsman', 175, 2, 100, 1200)
        ]

        insert_query = """
            INSERT INTO Seeds (SeedName, Weeks, SeedBreeder, NetWt, Sales, Price, InStock)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.executemany(insert_query, products)

        connection.commit()
        cursor.close()
        print(f"{cursor.rowcount} records inserted.")
        
    except mysql.connector.Error as err:
        print(f"Error inserting sample data: {err}")

