import random
import string


def generate_first_name():
    first_name = ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=5))
    return first_name


def generate_middle_name():
    middle_name = ''.join(random.choices(string.ascii_uppercase, k=1))
    return middle_name


def generate_last_name():
    last_name = ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=5))
    return last_name


def generate_random_name():
    first_name = ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=5))
    last_name = ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=5))
    middle_name = ''.join(random.choices(string.ascii_uppercase, k=1))
    return f"{first_name} {last_name} {middle_name} "


def generate_random_organization_name():
    name_length = random.randint(5, 7)
    organization_name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + " ", k=name_length)).strip()
    return organization_name + " Pvt Ltd"


def generate_random_zipcode():
    return f"{random.randint(10000, 99999)}"


def generate_random_mobile_number():
    prefixes = ['7', '8', '9']
    first_digit = random.choice(prefixes)
    remaining_digits = ''.join(random.choices('0123456789', k=9))
    return first_digit + remaining_digits


def generate_random_email():
    username_length = random.randint(6, 8)  # Username length between 6 and 12 characters
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=username_length))
    domain = "yoyomail.com"
    email = f"{username}@{domain}"
    return email


def generate_random_website():
    domain_length = random.randint(5, 7)
    domain_name = ''.join(random.choices(string.ascii_lowercase, k=domain_length))
    tlds = ['.com', '.net', '.org', '.io', '.tech', '.dev', '.co']
    tld = random.choice(tlds)
    website = f"https://{domain_name}{tld}"
    return website


def generate_random_address_line_1():
    house_number = random.randint(1, 9999)

    street_names = [
        "Main Street", "High Street", "Park Avenue", "Maple Street",
        "Oak Street", "Pine Street", "Elm Street", "Cedar Street",
        "Walnut Street", "Sunset Boulevard", "Broadway", "Hilltop Drive"
    ]
    street_name = random.choice(street_names)
    address_line_1 = f"{house_number} {street_name}"
    return address_line_1