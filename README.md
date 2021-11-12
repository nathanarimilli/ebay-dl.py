# Ebay scrapper HW 03
## Description of Code

They ebay-dl.py file contains a program that scrapes ebay for information and stores the results in a json file. It uses the argparse library to get a search term for any item on ebay (e.g. hammers, stuffed animals, clothes, shoes, textbooks, etc.). Then the program will download the first 10 pages of results on the search term unless fewer pages are specified. The program also uses beautiful soup to extract items from the search results. Finally, the program creates a list with dictionaries for six categories. These include Name: the name of the item on ebay, Price: the price of the item in cents, Status: the status of the item such as whether it is new or refurbished, Shipping: the price of shipping, Free_returns: whether the item has free returns, and Items_sold: how many items have been previously sold.

At the end, the program will return a json file named after the search term that has the information for all of these categories for each item in the first ten pages of the search term.

## How to Run the Code
To run the code for any item on ebay, use the following command in the ebay-dl.py terminal to get a JSON file of information for the chosen item:

    python3 ebay-dl.py 'item_name' --num_pages=10
    
The code I used to download `kettle.json` :

     python3 ebay-dl.py 'kettle' --num_pages=10
    
The code I used to download `zippo.json` :

    python3 ebay-dl.py 'zippo' --num_pages=10
    
The code I used to download `big lebowski.json` :

    python3 ebay-dl.py 'big lebowski' --num_pages=10

Finally, [here is the link](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03) to the course project.


    

  
  
