from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options for headless mode
options = Options()
options.binary_location = '/path/to/chrome'  # Replace with the actual path to your Chrome binary
driver = webdriver.Chrome(options=options)

# chrome_options.add_argument('--headless')  # Enables headless mode
# chrome_options.add_argument('--disable-gpu')  # Necessary for headless mode

# # Initialize the Chrome WebDriver
# driver = webdriver.Chrome(options=chrome_options)

# Example: Open a website and capture its title
start_url = 'https://ebay.com'
driver.get(start_url)
print(f"Title of the page: {driver.title}")
def open_and_capture_screenshots(urls):
    driver = webdriver.Chrome()  # You can use other browsers as well
    for url in urls:
        driver.execute_script(f"window.open('{url}', '_blank');")

    # Switch to each tab and capture screenshots
    for i, handle in enumerate(driver.window_handles):
        driver.switch_to.window(handle)
        driver.save_screenshot(f'screenshot_{i}.png')

    driver.quit()

# Example usage:
urls_to_open = ['https://major-project2.vercel.app/profile/660e55f79540a6996312',
                'https://major-project2.vercel.app/profile/65dd796a31d83196d853']
open_and_capture_screenshots(urls_to_open)


# Close the WebDriver
driver.quit()
