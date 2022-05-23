# CHAIN OF RESPONSIBILITY pattern

from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def handler(self, data):
        raise NotImplementedError()


class UserAdminHandler(Handler):
    def handler(self, data):
        if data.user.is_admin:
            data.user.type = 'ADMIN'

        return data


class UserVerifiedHandler(Handler):
    def handler(self, data):
        if data.user.is_verified:
            data.user.type = 'VERIFIED'

        return data


class Chain:
    def __init__(self):
        self.handlers = []

    def add_handler(self, handler: Handler):
        self.handlers.append(handler)

    def handle(self, data):
        for handler in self.handlers:
            data = handler(data)
        return data
