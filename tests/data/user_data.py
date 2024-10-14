# Need to complete login parameterize. add string is empty for valid login.
user_data: list[tuple[str, str, str]] = [
    ("standard_user", "secret_sauce", ""),
    (
        "standard_user",
        "incorrect_password",
        "Epic sadface: Username and password do not match any user in this service",
    ),
    (
        "incorrect_username",
        "secret_sauce",
        "Epic sadface: Username and password do not match any user in this service",
    ),
    (
        "incorrect_username",
        "incorrect_password",
        "Epic sadface: Username and password do not match any user in this service",
    ),
    (
        "",
        "secret_sauce",
        "Epic sadface: Username is required",
    ),
    (
        "standard_user",
        "",
        "Epic sadface: Password is required",
    ),
    (
        "",
        "",
        "Epic sadface: Username is required",
    ),
]
