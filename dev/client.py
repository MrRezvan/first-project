import logging
from unicodedata import name


class Client:
    def __init__(self, name: str, login : str, password: str, balance: int) -> None:
        self.name = name
        self.login = login
        self.password = password
        self.balance = balance