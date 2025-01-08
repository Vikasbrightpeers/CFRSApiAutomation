
from faker import Faker

# Generate voter data
def generate_voter_data():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "address": fake.address(),
        "phone_number": fake.phone_number(),
    }

# # Initialize WebDriver (e.g., Chrome)
# driver = webdriver.Chrome()

# # Function to add a voter
# def add_voter(voter_data):
#     driver.get("https://your-website.com/add-voter")  # Replace with your actual URL
#
#     # Wait for the page to load
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "first_name")))
#
#     # Fill in the form
#     driver.find_element(By.NAME, "first_name").send_keys(voter_data["first_name"])
#     driver.find_element(By.NAME, "last_name").send_keys(voter_data["last_name"])
#     driver.find_element(By.NAME, "email").send_keys(voter_data["email"])
#     driver.find_element(By.NAME, "address").send_keys(voter_data["address"])
#     driver.find_element(By.NAME, "phone_number").send_keys(voter_data["phone_number"])
#
#     # Submit the form
#     driver.find_element(By.NAME, "submit").click()

    # Wait for submission to complete
    # time.sleep(3)

# Function to delete a voter (assuming there's a way to search and delete by email)
# def delete_voter(email):
#     driver.get("https://your-website.com/search-voter")  # Replace with your actual URL
#
#     # Wait for the page to load
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "search")))
#
#     # Search for the voter by email
#     driver.find_element(By.NAME, "search").send_keys(email + Keys.RETURN)
#
#     # Wait for search results
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Delete']")))
#
#     # Click the delete button
#     driver.find_element(By.XPATH, "//a[text()='Delete']").click()
#
#     # Confirm deletion
#     WebDriverWait(driver, 10).until(EC.alert_is_present())
#     driver.switch_to.alert.accept()
#
#     # Wait for deletion to complete
#     time.sleep(3)
#
# # Run the script
# if __name__ == "__main__":
#     for _ in range(5):  # Run 5 times or any number of times you want
#         voter_data = generate_voter_data()
#         add_voter(voter_data)
#         delete_voter(voter_data["email"])
#
#     # Close the browser
#     driver.quit()
