# POS SYSTEM
This is terminal based POs system that does customer,product and purchase operations.
This is all done using python programming language

# DESCRIPTION<br/>
The POS system works by first creating an object then saving,retrieving,manipulating the data which is stored in json files.

# POS FEATURES
# 1.Customer Operations
This includes creating,updating,deleting and displaying customer data.<br/>

CREATE A USER<br/>
A menu with options is presented when the program is run with the following command python sprint.py -c.<br/>
To insert a new customer type 1 into the terminal and hit enter then enter teir details such as name, email etc.<br/>
This is then saved to a file called customers.json.<br/>

UPDATE A USER<br/>
To update a user type in 3 into the terminal and simply  pass in the user id which is automatically generated when the user is created
Then enter the new data and changes saved are saved in  customers.json file.<br/>

DELETE A USER<br/>
To delete a user type in 4 into the terminal and simply  pass in the user id which is automatically generated when the user is created
and the customer associated with that id will be deleted from the  customers.json file.<br/>

SEARCH A USER<br/>
To search a user type in 5 into the terminal and simply  pass in the user id which is automatically generated when the user is created
and the customer associated with that id will be read from the  customers.json file and their data returned.<br/>


# 2.Product Operations
This includes creating,updating,deleting and displaying product data.

CREATE A PRODUCT<br/>
A menu with options is presented when the program is run with the following command python sprint.py -p.<br/>
To insert a new product type 1 into the terminal and hit enter then enter the product details such as name, price etc.<br/>
This is then saved to a file called products.json.<br/>

UPDATE A PRODUCT<br/>
To update a product type in 3 into the terminal and simply  pass in the product id which is automatically generated when the product is created
Then enter the new data and changes saved are saved in  products.json file.<br/>

DELETE A PRODUCT<br/>
To delete a product type in 4 into the terminal and simply  pass in the product id which is automatically generated when the product is created and the product associated with that id will be deleted from the  products.json file.<br/>

SEARCH A PRODUCT<br/>
To search a product type in 5 into the terminal and simply  pass in the product id which is automatically generated when the user is created and the product associated with that id will be read from the  products.json file and their data returned.<br/>

# 3.Purchase Operations
This includes selling products as well as keeping stock of remaining products as well as the remaining amount in a customers wallet.<br/>
If the purchase is successful a receipt is generated and saved in a receipt.json file and the details displayed on the terminal.<br/>
The product stock and customers wallet balance are also updated automatically after the transaction.

# Basic Usage
Here is a basic usage of the commands<br/>
usage: sprint.py [-h] [-c,] [-p,] [-P,]<br/>
-h, --help  show this help message and exit<br/>
  -c,         Takes you to customer menu<br/>
  -p,         Takes you to product menu<br/>
  -P,         Takes you to purchase menu<br/>
  
  python sprint.py -c

# Installation
Ensure you have git and python3 installed on your system
Clone this repository by running<br/>
git clone https://github.com/Haxor44/sprint1/tree/master/Sprint<br/>

Then run python sprint.py -h to see list of commands to use.
# Support
For any issues contact the team Email:evolmalek04@gmail.com
# Buy Me coffee
<a href="https://www.buymeacoffee.com/gbraad" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
