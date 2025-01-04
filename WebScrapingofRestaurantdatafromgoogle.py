import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to ChromeDriver executable
chromedriver_path = r'C:\webdrivers\chromedriver.exe'

# Initialize WebDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

# Function to search Google for restaurants
def search_google(query):
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)  # Wait for search results to load

# Function to scroll down the page to load lazy-loaded results
def scroll_page():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Function to scrape restaurant data
def scrape_restaurants():
    # Scroll to ensure all content is loaded
    scroll_page()

    # Wait for restaurant listings to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='VkpGBb']"))
    )

    # Locate restaurant listings
    restaurant_elements = driver.find_elements(By.XPATH, "//div[@class='VkpGBb']")
    restaurants = []

    for element in restaurant_elements:
        try:
            # Extract restaurant name
            name = element.find_element(By.XPATH, ".//div[@role='heading']").text.strip()

            # Extract rating
            try:
                rating = element.find_element(By.XPATH, ".//span[contains(text(), '★')]").text.strip()
            except:
                rating = "Not Available"

            # Extract address and phone
            try:
                address = element.find_element(By.XPATH, ".//span[@class='LrzXr']").text.strip()
            except:
                address = "Not Available"

            phone = "Not Available"  # Phone numbers may not always be available

            # Append to the list
            restaurants.append([name, rating, phone, address])

        except Exception as e:
            print(f"Error extracting data: {e}")

    return restaurants

# Main function
def main():
    try:
        query = "restaurants in Downtown Toronto"
        search_google(query)
        restaurants = scrape_restaurants()

        # Save to CSV
        df = pd.DataFrame(restaurants, columns=['Name', 'Rating', 'Phone', 'Address'])
        df.to_csv('downtown_toronto_restaurants.csv', index=False)
        print("Data saved to 'downtown_toronto_restaurants.csv'")

    finally:
        driver.quit()  # Ensure the driver is closed

if __name__ == "__main__":
    main()
