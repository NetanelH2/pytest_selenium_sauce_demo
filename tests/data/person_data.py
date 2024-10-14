from faker import Faker


def generate_person_details() -> tuple[str, str, str]:
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    postal_code = fake.postcode()
    return first_name, last_name, postal_code
