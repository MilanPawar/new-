import cv2
import mysql.connector 
import webbrowser

def open_multiple_tabs(urls):
    for url in urls:
        webbrowser.open(url, new=2)  # Opens in a new tab

# Example usage:
urls_to_open = ['https://major-project2.vercel.app/profile/660e55f79540a6996312',
                'https://major-project2.vercel.app/profile/65dd796a31d83196d853']
open_multiple_tabs(urls_to_open)

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

from PIL import ImageGrab

# Capture the entire screen
screenshot = ImageGrab.grab()

# Save the screenshot to a file
screenshot.save("shot.png")


from selenium import webdriver

# # Connect to the database
# connection = mysql.connector.connect(
#     host="your_host",
#     user="your_username",
#     password="your_password",
#     database="your_database"
# )

# # Create a cursor object
# cursor = connection.cursor()

# # Define the SQL query
# query = "SELECT username, password FROM users WHERE id = %s"

# # Execute the query
# cursor.execute(query, (user_id,))

# # Fetch the result
# result = cursor.fetchone()

# # Close cursor and connection
# cursor.close()
# connection.close()

# # Process the result
# if result:
#     username, password = result
#     print("Username:", username)
#     print("Password:", password)
# else:
#     print("User not found")
# # from selenium import webdriver
# # from webdriver_manager.chrome import ChromeDriverManager

# # options = webdriver.ChromeOptions()
# # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

# print(cv2.__version__)


# Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://www.ebay.com")
driver.save_screenshot("screenshot.png")
driver.quit()


