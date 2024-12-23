from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def register_test(driver, username, password):
    # Open the registration page
    driver.get("http://localhost:5000/register")

    # Wait for the page to load
    wait = WebDriverWait(driver, 30)
    username_input = wait.until(EC.visibility_of_element_located((By.ID, "username")))

    # Enter username, password, and confirm password
    username_input.send_keys(username)
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_input.send_keys(password)
    confirm_password_input = wait.until(EC.visibility_of_element_located((By.ID, "confirm-password")))
    confirm_password_input.send_keys(password)

    # Submit the registration form
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit_button.click()

    # Wait for the registration result
    result_message = wait.until(EC.visibility_of_element_located((By.ID, "register-error")))
    result_text = result_message.text

    # Print the registration result
    print("Registration Result: ", result_text)

def login_test(driver, username, password):
    # Open the login page
    driver.get("http://localhost:5000/login")

    # Wait for the page to load
    wait = WebDriverWait(driver, 30)
    username_input = wait.until(EC.visibility_of_element_located((By.ID, "username")))

    # Enter username and password
    username_input.send_keys(username)
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_input.send_keys(password)

    # Submit the login form
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit_button.click()

    # Wait for the login result
    wait.until_not(EC.visibility_of_element_located((By.ID, "login-error")))

    # The condition for successful login is the absence of the login-error element
    try:
        wait = WebDriverWait(driver, 5)
        login_error_element = wait.until(EC.visibility_of_element_located((By.ID, "login-error")))
        print("Login Failed")
    except TimeoutException:
        print("Login Success")


def chat_test(driver):
    # Open the chat page
    driver.get("http://localhost:5000/chat")

    # Wait for the page to load
    wait = WebDriverWait(driver, 30)
    input_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".chat-input input")))

    # Enter a chat message and send
    input_box.send_keys("Hello")
    send_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".chat-input button")))
    send_button.click()

    # Wait for the chat reply
    reply_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".message-bot p")))
    reply_text = reply_message.text

    # Print the chat reply
    print("Chatbot Reply: ", reply_text)


def search_test(driver):
    # Open the search page
    driver.get("http://localhost:5000/search")

    # Wait for the page to load
    wait = WebDriverWait(driver, 30)
    input_box = wait.until(EC.visibility_of_element_located((By.ID, "keyword")))

    # Enter the search keyword and submit the search
    input_box.send_keys('Hello')
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit_button.click()

    # Wait for the search result
    result_div = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-result")))
    result_text = result_div.text

    # Print the search result
    print("Search Result: ", result_text)
    

# Run the tests
def run_tests(driver):
    register_test(driver, username='Selenium', password='testing')
    login_test(driver, username='Selenium', password='testing')
    chat_test(driver)
    search_test(driver)

# Launch Google Chrome
chrome_driver = webdriver.Chrome()

# Run the tests on Google Chrome browser
run_tests(chrome_driver)
chrome_driver.quit()

# Launch Microsoft Edge
edge_driver = webdriver.Edge()

# Run the tests on Microsoft Edge browser
run_tests(edge_driver)
edge_driver.quit()

