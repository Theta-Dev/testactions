from selenium import webdriver

def query_page_selenium(url) -> str:
    print("Using selenium to fetch " + url)

    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument("--no-sandbox")
    chrome_opt.add_argument("--disable-extensions")
    chrome_opt.add_argument("--disable-gpu")
    chrome_opt.add_argument("--disable-dev-shm-usage")
    chrome_opt.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_opt)
    driver.get(url)
    data = driver.page_source
    driver.quit()
    return data

print(query_page_selenium('https://raw.githubusercontent.com/Theta-Dev/testactions/master/README.md'))
