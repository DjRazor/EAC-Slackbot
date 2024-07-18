# Automation for ID Badge Requests
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def main(username, password, email):
    print(f'Running badges script with {username}, {password}, {email}')
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # Example of visiting a website
    driver.get("https://mas.byu.edu/#/")
    title = driver.title
    driver.quit()

    return f"The title of the page is: {title}"

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
