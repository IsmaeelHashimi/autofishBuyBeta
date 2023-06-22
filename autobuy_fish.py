import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Replace these variables with your actual account and payment information
email = "walterclements@hotmail.com"
password = "waltoisndfo"
card_number = "1234123412341234"
expiry_month = "05"
expiry_year = "24"
cvv = "344"
firstName = "Ismaeel"
lastName = "Hashimi"
address = "144-41 26th Avenue, Flushing, NY, USA"
apt = "FL 2"
city = "Flushing"
state = "New York"
zipCode = "11354"
phone = "6463442302"
discountCode = "aquariumcoop"
# Initialize WebDriver
driver = webdriver.Chrome(executable_path="C:/Users/MrFla/aquahuna")  # For Chrome

def add_to_cart():
    while True:
        print("Checking for fish in stock...")
        driver.get("https://aquahuna.com/collections/freshwater-shrimps/products/singapore-shrimp-bamboo-shrimp")

        time.sleep(2)  # 2-second delay

        add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[@name='add']")

        if add_to_cart_buttons:
            add_to_cart_button = add_to_cart_buttons[0]
            is_disabled = add_to_cart_button.get_attribute("disabled")

            if not is_disabled:
                driver.execute_script("arguments[0].click();", add_to_cart_button)
                time.sleep(4)
                return True
            else:
                print("Fish not in stock. Retrying in 30 seconds...")
                time.sleep(30)


def checkout():
    print("Proceeding to checkout...")
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
    Select(driver.find_element(By.NAME, "zone")).select_by_value("NY")
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

if __name__ == "__main__":
    while True:
        if add_to_cart():
            checkout()
            print("Fish successfully purchased!")
            break
        else:
            print("Fish not in stock. Retrying in 30 seconds...")
            time.sleep(30)


