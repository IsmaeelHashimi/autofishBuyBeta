# Ismaeel Hashimi

# Import libraries
import time
import logging
import os
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Prompt user for account and payment details
email = input("What is your e-mail?: ")
card_number = input("What is your credit card number?: ")
expiry_month = input("What is your expiry month of the card?: ")
expiry_year = input("What is your expiry year of the card?: ")
cvv = input("What is the CVV of the card?: ")
firstName = input("What is your first name?: ")
lastName = input("What is your last name?: ")
address = input("What is your address?: ")
apt = input("APT Number?: ")
city = input("What is your city?: ")
state = input("What state are you in?: ")
zipCode = input("What is your zipcode?: ")
phone = input("What is your phone number?: ")
discountCode = "aquariumcoop"
# Initialize Selenium WebDriver while specifying the ChromeDriver path
driver = webdriver.Chrome(executable_path="C:/Users/MrFla/aquahuna")  # For Chrome

# Defining dictionary that converts full state names to abbreviated versions for website
states_dict = {
    "alabama": "AL",
    "alaska": "AK",
    "american samoa": "AS",
    "arizona": "AZ",
    "arkansas": "AR",
    "california": "CA",
    "colorado": "CO",
    "connecticut": "CT",
    "delaware": "DE",
    "washington dc": "DC",
    "micronesia": "FM",
    "florida": "FL",
    "georgia": "GA",
    "guam": "GU",
    "hawaii": "HI",
    "idaho": "ID",
    "illinois": "IL",
    "indiana": "IN",
    "iowa": "IA",
    "kansas": "KS",
    "kentucky": "KY",
    "louisiana": "LA",
    "maine": "ME",
    "marshall islands": "MH",
    "maryland": "MD",
    "massachusetts": "MA",
    "michigan": "MI",
    "minnesota": "MN",
    "mississippi": "MS",
    "missouri": "MO",
    "montana": "MT",
    "nebraska": "NE",
    "nevada": "NV",
    "new hampshire": "NH",
    "new jersey": "NJ",
    "new mexico": "NM",
    "new york": "NY",
    "north carolina": "NC",
    "north dakota": "ND",
    "northern mariana islands": "MP",
    "ohio": "OH",
    "oklahoma": "OK",
    "oregon": "OR",
    "palau": "PW",
    "pennsylvania": "PA",
    "puerto rico": "PR",
    "rhode island": "RI",
    "south carolina": "SC",
    "south dakota": "SD",
    "tennessee": "TN",
    "texas": "TX",
    "utah": "UT",
    "vermont": "VT",
    "virginia": "VA",
    "washington": "WA",
    "west virginia": "WV",
    "wisconsin": "WI",
    "wyoming": "WY",
    "virgin islands": "VI",
    "armed forces americas": "AA",
    "armed forces europe": "AE",
    "armed forces pacific": "AP",


}

# Converts the inputted state to the abbreviated version
state = states_dict[state.lower()]

def add_to_cart():
    while True:
        print("Checking for fish in stock...")

        # Open product page
        driver.get("https://aquahuna.com/collections/freshwater-shrimps/products/singapore-shrimp-bamboo-shrimp")

        time.sleep(2)  # 2-second delay for page to load
        # Search for "add to cart" button
        add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[@name='add']")

        # Checking if "add to cart" button is disabled
        if add_to_cart_buttons:
            add_to_cart_button = add_to_cart_buttons[0]
            is_disabled = add_to_cart_button.get_attribute("disabled")

            # If "add to cart" button is not disabled (specimen in stock)
            if not is_disabled:
                driver.execute_script("arguments[0].click();", add_to_cart_button)
                time.sleep(4)
                return True # Specimen is added to cart
            else:
                # If product isn't in stock, wait 30 seconds before checking again
                print("Fish not in stock. Retrying in 30 seconds...")
                time.sleep(30)



def checkout():
    """Function that proceeds to check out and fills all necessary information"""
    print("Proceeding to checkout...")

    # Open cart page
    driver.get("https://aquahuna.com/cart")
    print("Going to cart...")

    # Wait for the page to load and update
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'CHECK OUT')]")))
    print("First check out done...")
    driver.find_element(By.XPATH, "//button[contains(text(), 'CHECK OUT')]").click()

    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email)
    print("Added email...")
    ''' Skipping Country '''
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(firstName)
    print("first name added...")
    '''First Name'''
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys(lastName)
    print("last name added...")
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "address1"))).send_keys(address)
    print("address added...")
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "address2"))).send_keys(apt)
    print("apt added...")
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "city"))).send_keys(city)
    print("city added...")
    Select(driver.find_element(By.NAME, "zone")).select_by_value(state)
    print("state added...")
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "postalCode"))).send_keys(zipCode)
    print("zipcode added...")
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "phone"))).send_keys(phone)
    print("phone added...")

    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/form/div[1]/div/div[2]/div[2]/div[1]/button').click()
    print("continued after entering shipping info...")

    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/form/div[1]/div/div/div[2]/div[1]/button').click()
    time.sleep(3)
    print("going to enter credit card info...")

    # Switch to the 'Card number' iframe
    card_number_iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='number']/iframe")))
    driver.switch_to.frame(card_number_iframe)
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "number"))).send_keys(card_number)
    print("card number added...")
    driver.switch_to.default_content()

    # Switch to the 'Name on card' iframe
    name_on_card_iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='name']/iframe")))
    driver.switch_to.frame(name_on_card_iframe)
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "name"))).send_keys(
        firstName + " " + lastName)
    print("name on card added...")
    driver.switch_to.default_content()

    # Switch to the 'Expiration date' iframe
    expiry_date_iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='expiry']/iframe")))
    driver.switch_to.frame(expiry_date_iframe)
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "expiry"))).send_keys(expiry_month)
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "expiry"))).send_keys(expiry_year)
    print("expiry date added...")
    driver.switch_to.default_content()

    # Switch to the 'Security code' iframe
    security_code_iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='verification_value']/iframe")))
    driver.switch_to.frame(security_code_iframe)
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "verification_value"))).send_keys(cvv)
    print("cvv added...")
    driver.switch_to.default_content()
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "reductions"))).send_keys(discountCode)
    driver.find_element(By.CSS_SELECTOR, "button.QT4by.rqC98.EbLsk.VDIfJ.janiy.hlBcn").click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/div/form/div[1]/div/div[2]/div[1]/button').click()

    time.sleep(20)


# Run the bot
if __name__ == "__main__":
    while True:
        # Check if product is in stock, if so, it gets added to cart
        if add_to_cart():
            checkout() # Proceed to checkout
            print("Fish successfully purchased!")
            break
        else:
            print("Fish not in stock. Retrying in 30 seconds...")
            time.sleep(30) # Waits 30 seconds before checking again


