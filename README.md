**AUTO PURCHASE BOT FOR AQUAHUNA (Online Fish Retailer)**
This is a Python script that automatically checks for a specific specimen's availability, (currently only for Bamboo Shrimp, can be changed to any link on the store).
The following script uses Selenium to interact with the website and to automate the operations in the Chrome browser.

**REQUIREMENTS**
- Python3
- Selenium
- Chrome Browser
- ChromeDriver that is compatible with your Chrome browser version (this is a local project so you will have to change the path in the script to the ChromeDriver)

**RUNNING**
From the terminal, write the command "python autobuy_fish.py"
Once ran the following information will be prompted to be answered by the user:
- E-mail
- Credit Card Number
- Expiry Month of Card
- CVV of Card
- First Name
- Last Name
- Address
- APT Number (Optional)
- City
- State
- Zip Code
- Phone Number
Once done going through all prompts, the script will automatically check the Aquahuna website for the availability of the specified aquatic specimen.
If the specimen is in stock, the script will add it to the cart, proceed to checkout, apply a discount code for 5% off, and complete the purchase.
If the specimen is out of stock, the script will wait 30 seconds before checking again. This process repeats until specimen is available.

**TO-DO**
- Add error handling
- Add user interface
- Add options of specimen/allow users to paste their own link to automate

**DISCLAIMER**
The use of this script should comply with the policies of the Aquahuna aquarium store website.
Be responsible and respectful with the frequency of requests sent by the script to the website. 
Automated purchase might be against the website's terms of service. Use this script responsibly.

**LICENSE**
This project is licensed under the MIT License.
