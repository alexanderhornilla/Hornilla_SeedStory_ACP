I. PROJECT OVERVIEW

The SeedStory System exists to manage sales and inventory within a seed shop, removing inefficiencies from manual operation and improving customer experience. 
It automates processes such as tracking of inventory, browsing of products, and payment handling for accuracy and efficiency while reducing errors and 
administrative burdens. By allowing such features as sorted browsing, real-time stock updates, and a seamless checkout process through an application of discount, 
the system enables customer satisfaction and helps expand the business by way of data-driven sales and inventory performance. Lastly, it aligns with the shop's 
mission to reliably and conveniently deliver quality seeds while being sustainable and operationally excellent.

Included Features: 
    1. Product Variety: People can try to sort the seeds in numerous ways (by name, growth duration, and sales per week).

    2. Inventory: Seeds will be stored in groups arranged by seed name or kind, except for the time to grow, breeder, and weeks to grow, including the price for 
    each item.
    
    3. Cart: Customers can add items to the cart, view the selected product, and make the payment. The system gives the customer a 5% discount if the user purchases 
    five or more products.
    
    4. Easy Checkout: Multiple payment options—cash, Credit Card, and E-Wallet—are available with easy checkout so that customers do not face any hassle while shopping.
    
    5. User-Friendly Navigation: The system comprises intuitive menus for sorting, selecting, and buying seeds to enrich the customer experience.
    
Excluded Features:
    1. Online Payment: The system does not support payment processing through online platforms.
    
    2. Multi-Language Support: It operates in a single language and does not cater to multilingual users.
    
    3. Custom Seed Packaging: Customization options for seed packaging are unavailable.
    
    4. Customer Feedback: No functionality exists for collecting or managing customer feedback.

Achievable Outcomes:
    1. Improved Sales Tracking: Enable the ability to track seed sales, inventory, and customer transactions in full details up to 100% with the operational 
    database within the first month from deployment.

    2. Improved Customer Satisfaction: Score at least 90 percent good feedback about ease of use and the checkout process within the first three months.

    3. Inventory Updates: To reduce manual stock updates by 80% through database integration by the end of Q1 2025.

    4. Availability of Products: Sorts by name, growth duration, and sales per week, allowing customers to look for products within 30 seconds of search time at launch.


II. PYTHON CONCEPTS AND LIBRARIES

Feature/Concept                         Description                                                    Purpose/Implementation

1. Object-Oriented Programming (OOP)    Classes such as SeedDetails, Inventory, and ShoppingCart       Promotes modularity and reusability, with 
                                        encapsulate data and behavior.                                 each class handling specific parts of the 
                                                                                                       system (e.g., product details, cart).

2. Error Handling                       try-except blocks manage invalid inputs and database           Ensures smooth user experience by    
                                        errors gracefully.                                             preventing crashes and handling issues like 
                                                                                                       non-numeric input or database disconnections.

3. Database Integration                 Uses mysql.connector to interact with a MySQL database         Enables real-time updates for stock, cart, and 
                                        for inventory.                                                 transactions through SQL queries (CRUD operations).
                            
4. Sorting and Filtering                Python’s sorted() function organizes inventory based on        Simplifies navigation, allowing users to find products 
                                        criteria like seed name, growth duration, or sales.            efficiently based on their preferences.

5. User Input and Interaction           Input-handling capabilities create menus and prompts.          Provides a user-friendly interface for operations like 
                                                                                                       adding items to the cart and checking out.
                                                                                                    
6. Mathematical Calculations            Arithmetic operations calculate discounts, totals, and         Applies business logic for pricing, ensuring accurate
                                        change during checkout.                                        and efficient transactions.

7. Custom Libraries                     Includes create_connection and insert_sample_data to           Ensures integration with the database for inventory.
                                        manage database connectivity.
                            
8. Logical Flow                         Conditional statements and loops guide the application’s       Ensures logical progression in operations, like cart
                                        flow, such as retries for valid payments.                      clearing after checkout or asking users before proceeding 
                                                                                                       with payment.
 

III. SUSTAINABLE DEVELOPMENT GOALS

SDG: Decent Work and Economic Growth (SDG 8)

SDG 8 includes promoting sustained, inclusive, and sustainable economic growth, full and productive employment, and decent work for all. This is to be focused 
on the entrepreneurial opportunities required for high productivity and innovation to ensure better wages, safe working conditions, and economic development for 
all sections, particularly in the developing regions.

    1. Empowering Local Farmers: SeedStory will source seeds directly from local farmers and cooperatives. This will enable the company to make its market more 
    predictable for the farmers; thus, the farmers are empowered to grow their businesses and earn a steady income. It also nudges smallholder farmers to invest 
    in sustainable agriculture.

    2. Employment and Fair Labor: SeedStory will provide employment opportunities in all operations such as managing stores, logistics, marketing, and education. 
    It will provide a fair work environment at all times. Workers will be fairly compensated, safe, and included at all times, developing decent work conditions.

    3. Pushing Agri-preneurship: SeedStory will help entrepreneurs in agriculture, offering low-cost, high-quality seeds. Workshops and training programs help them 
    acquire techniques for effective planting and develop the ability to launch their own farms or businesses in order to uplift the local economies.

    4. Orienting Agriculture towards Sustainability: By providing climate-resilient and sustainable seed varieties, SeedStory supports farmers in increasing productivity 
    while minimizing environmental impact. This will help in ensuring sustainable economic growth by ensuring long-term viability in agriculture, which is critical for 
    economic stability.

    5. Strengthening Local Economies: SeedStory is working to energize the local economies through partnerships with local brands and organizations. Adding partnerships 
    with local suppliers based on communities, as well as some reliable manufacturers of eco-friendly agricultural tools, further energizes economic activity at the local 
    levels.

SDG 8, Decent Work and Economic Growth is integrated in SeedStory as the store would both develop as a business and benefit from growth in a more sustainable and inclusive economy. In this regard, SeedStory reflects commitment to growth helpful to people and the planet through fair employment, local farmers empowerment, and support of the agri-preneurs.


IV. PROGRAM/SYSTEM INSTRUCTIONS
1. Initialization: On the first run, the database, table, and sample data will be created. 
2. Main Menu: After the initial setup, the program will display the main menu for interaction.

    -----------MAIN MENU-------------
    (1) Browse Products
    (2) View Cart and Checkout

    (3) Exit
    ---------------------------------
    Enter your choice (1-3):

3. Browse Products: If you choose option 1 to browse products, you'll see the sort menu.

    --------Sort Products By:--------
    (1) Name (A-Z)
    (2) Growth Duration (Weeks)
    (3) Weekly Sales

    (4) BACK
    ---------------------------------
    Your choice (1-4):

Example output for sorting by Name (A-Z):

    SEED NAME       WEEKS(Growth)   SEED BREEDER        NET WT(g)     SALES(pw)   PRICE(PHP)   STOCK
    ------------------------------------------------------------------------------------------------------------------------
    Carrot          8               XYZ Seeds           200           15           30.00         120
    Lettuce         6               Green Leaf          100           18           25.00         80
    Tomato          10              ABC Breeders        150           20           50.00         100
    ------------------------------------------------------------------------------------------------------------------------

    Add an item to cart? (yes/no):

4. Add to Cart: If you choose to add an item to the cart, the program will prompt you to enter the Seed Name and Quantity to add. 

Example interaction:

    Enter seed name to add to cart: Carrot
    Enter quantity to add: 2

    2 Carrot(s) added.

    --------Sort Products By:--------
    (1) Name (A-Z)
    (2) Growth Duration (Weeks)
    (3) Weekly Sales

    (4) BACK
    ---------------------------------
    Your choice (1-4):
	
5. View Cart and Checkout: If you choose option 2 to checkout, the cart summary will be shown.

    CART SUMMARY - SEEDSTORY
    ------------------------------------------------------------------------------
    SEED NAME       SEED BREEDER        PRICE(PHP)   QUANTITY       TOTAL(PHP)
    ------------------------------------------------------------------------------
    Carrot          XYZ Seeds           30.00        2              60.00
    ------------------------------------------------------------------------------
    Subtotal: PHP 60.00
    Discount: -PHP 0.00 (5% off for 5 or more items)
    Total: PHP 60.00
    ------------------------------------------------------------------------------

    Proceed to payment? (yes/no):

6. Payment: Upon proceeding to payment:

    Enter payment (Total: PHP 57.00):

After entering payment (e.g., PHP 200):

    Payment successful.

    RECEIPT - SEEDSTORY
    -----------------------------------------------------------------------------
    SEED NAME       SEED BREEDER        PRICE(PHP)   QUANTITY       TOTAL(PHP)
    -----------------------------------------------------------------------------
    Carrot          XYZ Seeds           30.00        2              60.00
    -----------------------------------------------------------------------------
    Subtotal: PHP 60.00
    Discount: -PHP 0.00 (5% off for 5 or more items)
    Total: PHP 60.00
    Cash: PHP 100.00
    Change: PHP 40.00
    -----------------------------------------------------------------------------

7. Exit: If you choose to exit, the program will close with:

    Exited SeedStory.