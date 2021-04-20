from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import csv


options = Options()
options.headless = True
driver = webdriver.Firefox(executable_path='drivers/geckodriver')

#navigate to page
driver.get('https://www.bloomberg.com/quote/SPX:IND')
#driver.page_source

name = driver.find_element_by_class_name("companyName__99a4824b").text
#.get_attribute("class") returns the class attribute

value = driver.find_element_by_class_name("priceText__1853e8a5").text

joined_details = (name, value)
joined_list = []
joined_list.append(joined_details)
print(joined_list, sep=',')

#create a csv file to save the scraped data

with open("detail.csv", 'a') as csv_file:
    writer = csv.writer(csv_file)
    for content in joined_list:
        writer.writerow(content)

driver.quit()