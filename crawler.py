from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import json


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# open link
driver.get("https://www.amazon.com/s?k=candles&crid=WOK2TIK1EHE3&sprefix=candle%2Caps%2C198&ref=nb_sb_noss_1")


# find search result elements
search_results = driver.find_elements(By.CSS_SELECTOR, ".s-result-item")

# extract ASINs
asins = []
for result in search_results:
    asin = result.get_attribute("data-asin")
    if asin:
        asins.append(asin)
#print(asins)

# open the first product
product_link = driver.find_element(By.CSS_SELECTOR, ".a-link-normal.a-text-normal")
product_link.click()

# open the reviews for this product
reviews_link = driver.find_element(By.ID,'acrCustomerReviewText')
reviews_link.click()

time.sleep(2)

# JSON file
reviews_file = open('reviews.json', 'w')

# load all of the reviews
all_reviews = driver.find_element(By.CSS_SELECTOR,'.a-link-emphasis.a-text-bold')
all_reviews.click()

while True:
    try:
        reviews = driver.find_elements(By.CSS_SELECTOR, '.review-text-content')
        for review in reviews:
            json.dump({'review_text': review.text}, reviews_file, indent=6)
            reviews_file.write('\n')
        time.sleep(2)
        next_page = driver.find_element(By.CSS_SELECTOR, '.a-last')
        next_page.click()
    except:
        break

# quit
time.sleep(5)
driver.quit()

# scrape the first review
#review1 = driver.find_element(By.CSS_SELECTOR,'.review-text-content')
#print(review1.text)

# scrape all reviews
#reviews = driver.find_elements(By.CSS_SELECTOR,'.review-text-content')
#for review in reviews:
#    print(review.text)

# dump reviews in separate lines in a JSON file
#reviews_file = open('reviews.json', 'w')
#for review in reviews:
#    json.dump({'review_text': review.text}, reviews_file, indent=6)
#    reviews_file.write('\n')
#reviews_file.close()
    

