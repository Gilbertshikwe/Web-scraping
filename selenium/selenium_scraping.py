from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the webdriver (in this case, we're using Chrome)
driver = webdriver.Chrome()

# Navigate to the target website
driver.get("https://www.remnantrva.com/")

# Find an element on the page
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "h1, h2, h3"))
)

# Extract the text content of the element
text = element.text
print(text)

# Close the browser
driver.quit()