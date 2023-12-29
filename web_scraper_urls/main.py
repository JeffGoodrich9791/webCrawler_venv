from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import re
import json

# Set the URL for Google search
search_url = "https://www.google.com/search"


query = "Meditereanean Recipes"

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Optional: Run headless to hide the browser window
driver = webdriver.Chrome(options=options)  # You'll need to have ChromeDriver installed
driver.get(search_url)

# Find the search box and input the query
search_box = driver.find_element("name", "q")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)

# Scroll down to load more results (adjust the number of scrolls as needed)
for _ in range(6):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Add a sleep to allow the page to load

# Get the page source after scrolling
search_result = driver.page_source
search_doc = BeautifulSoup(search_result, "html.parser")

# Create a list to store URLs containing "recipe"
recipe_urls = []

# Extract URLs containing "recipe"
for link in search_doc.find_all("a", href=True):
    url = link["href"]

    # Exclude Google-related links
    if not any(keyword in url.lower() for keyword in ["google.com", "maps.google.com", "accounts.google.com", "facebook.com", "youtube.com"]):
        # Check if the URL contains "recipe"
        if re.search(r'recipe', url, re.IGNORECASE):
            # Extract the actual URL from the Google search results link
            url_match = re.search(r'(https?://\S+)', url)
            if url_match:
                recipe_urls.append(url_match.group(1))

            # Break the loop if we have collected 150 URLs
            if len(recipe_urls) >= 150:
                break

# Close the WebDriver
driver.quit()

# Specify the full path where you want to save the JSON file
output_filename = r"C:\Users\Win10User\Desktop\webCrawlers\webCrawler_venv\indexed_recipe_urls.json"

# Load existing indexed URLs from the JSON file
try:
    with open(output_filename, "r") as json_file:
        existing_indexed_recipe_urls = json.load(json_file)
except FileNotFoundError:
    existing_indexed_recipe_urls = []

# Identify the starting index for the new URLs
start_index = len(existing_indexed_recipe_urls)

# Create a list of new URLs with sequential indices
new_indexed_recipe_urls = [{"index": start_index + i, "url": url} for i, url in enumerate(recipe_urls)]

# Append the new URLs to the existing ones
all_indexed_recipe_urls = existing_indexed_recipe_urls + new_indexed_recipe_urls

# Overwrite the entire file with the updated list of indexed URLs
with open(output_filename, "w") as json_file:
    formatted_indexed_recipe_urls = [{"index": i, "url": obj["url"]} for i, obj in enumerate(all_indexed_recipe_urls)]
    json.dump(formatted_indexed_recipe_urls, json_file, indent=2)

# Print the list of recipe URLs
print("List of the first 150 URLs containing 'recipe':")
for indexed_url in formatted_indexed_recipe_urls:
    print(f"{indexed_url['index']}: {indexed_url['url']}")

print(f"\nIndexed URLs saved to '{output_filename}'")
