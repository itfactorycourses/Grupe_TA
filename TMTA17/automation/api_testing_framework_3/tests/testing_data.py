from requests_folder.request_admin import generate_token
from faker import Faker
data_generator = Faker()

token = generate_token().json()['accessToken']
customer_name = data_generator.name()