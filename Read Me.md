Walmart API 
===========
Project Requirements:
---------------------
1. Search for products based upon a user-provided search string
2. Use the first item in the search response as input for a product recommendation search
3. Retrieve reviews of the first 10 product recommendations
4. Rank order the recommended products based upon the review sentiments

Assumptions:
------------
1. No front end GUI or REST API was implemented. 
2. The API KEY in use is mine and the user is not asked to enter his own API key.
3. The ratings of each product is averaged and is sorted in descending order.

Development Environment:
-----------------------
1. This program was developed in Python version 2.7.9
2. O.S. : Ubuntu 15.04

Instructions to Run:
--------------------
1. Install Python on the local system.
2. Open the terminal and run the following command : pip install requests.
3. Once the installation is complete , Download the walmart.py from the submission and navigate to the folder where the above file is present.
4. Type in the following command : python walmart.py ------- . (Replace the '-' with your search string) and press enter.
5. Example: python walmart.py ipad.

