from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import csv
import time

path = "D:\My Programs\DS Internship Task\chromedriver.exe"

def get_linkedin_data_browser(first_name, last_name):
    # Set up Chrome options to ignore version mismatch
    chrome_options = Options()
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Set up WebDriver with Chrome options
    service = Service(path)  # Update this path
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open LinkedIn and perform a search
    driver.get('https://www.linkedin.com/')
    time.sleep(2)  # Add sleep to allow the page to load

    search_box = driver.find_element('name', 'q')
    search_box.send_keys(f'{first_name} {last_name}')
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    # Extract relevant information from the search results
    users_data = []
    search_results = driver.find_elements_by_css_selector('li.search-result')
    for result in search_results[:5]:
        user_data = {
            'First Name': result.find_element_by_css_selector('span.actor-name').text,
            'Last Name': result.find_element_by_css_selector('span.actor-name').text,
            'Profile URL': result.find_element_by_css_selector('a.search-result__result-link').get_attribute('href')
        }
        users_data.append(user_data)

    driver.quit()
    return users_data

def save_to_csv(data, filename='linkedin_data_browser.csv'):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['First Name', 'Last Name', 'Profile URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for user in data:
            writer.writerow(user)

if __name__ == '__main__':
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')

    linkedin_data = get_linkedin_data_browser(first_name, last_name)
    save_to_csv(linkedin_data)