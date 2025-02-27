import csv
from faker import Faker


def generate_fake_users(num_users=1000, output_file="fake_users.csv"):
    fake = Faker()

    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["User Name", "First Name", "Last Name", "Email", "Contact Number"])

        for _ in range(num_users):
            first_name = fake.first_name()
            last_name = fake.last_name()
            user_name = fake.user_name()
            email = fake.email()
            contact_number = fake.phone_number()

            writer.writerow([user_name, first_name, last_name, email, contact_number])

    print(f"{num_users} fake users generated and saved to {output_file}")


if __name__ == "__main__":
    generate_fake_users()
