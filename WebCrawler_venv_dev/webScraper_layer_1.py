from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Initialize the WebDriver with Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')
options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"

# Use ChromeDriverManager to automatically download the correct version of ChromeDriver

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# Navigate to the given URL
url = "https://www.foodandwine.com/appetizers/meze/mediterranean"
driver.get(url)
driver.maximize_window()
time.sleep(10)
# Scroll down the page using JavaScript (adjust the number of scrolls based on the page structure)
#for _ in range(5):  # You may need to adjust this based on the page structure
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #time.sleep(2)  # Adjust the sleep time based on your needs

# Find all elements with the specified span and alt attributes
recipe_elements = driver.find_elements(class_=".*list,*" and "recipe")

# Print the results
#for recipe_element in recipe_elements:
    #print(recipe_element.get_attribute('innerHTML'), limit=50)quit


# Close the browser
driver.quit()

print(recipe_elements.innerHTML)
