import csv
import random
from faker import Faker
from datetime import datetime, timedelta

# Generate fake data using Faker library
fake = Faker()

# Set the range for birth dates (around 1990 to 2005)
birth_date_start = datetime(1990, 1, 1)
birth_date_end = datetime(2005, 12, 31)

# Generate 10 random customers
customers = []
for _ in range(500):
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=35)

    # Set the range for registration dates in 2023
    registration_date = fake.date_this_year(before_today=False, after_today=True)

    # Set the range for test dates in 2023 (sequential and after the registration date)
    days_between_registration_and_test = random.randint(1, 30)  # Adjust as needed
    theory_test_date = registration_date + timedelta(days=days_between_registration_and_test)
    practical_test_date = theory_test_date + timedelta(days=random.randint(1, 30))  # Adjust as needed

    phone_number = f"080-{fake.random_number(digits=4)}-{fake.random_number(digits=4)}"

    customer = {
        "Name": fake.name(),
        "Gender": random.choice(["Male", "Female"]),
        "Birthday": birth_date.strftime('%Y-%m-%d'),
        "Phone Number": phone_number,
        "Facebook": fake.user_name(),
        "Certificate Type": random.choice(["Car", "Truck", "Motorcycle"]),
        "Document ID": fake.random_number(digits=8),
        "Register Date": registration_date.strftime('%Y-%m-%d'),
        "Theory Test Date": theory_test_date.strftime('%Y-%m-%d'),
        "Practice Test Date": practical_test_date.strftime('%Y-%m-%d')
    }
    customers.append(customer)

# Specify the file path to save the CSV file
file_path = r"C:\Users\USER\Projects\20231203-Aichi-Customer-Manager\database\customers.csv"

# Write the customers data to the CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=customers[0].keys())
    writer.writeheader()
    writer.writerows(customers)

print("Customers data has been saved to the CSV file.")
