import allure
import pytest
import requests

from data.generator import Generator
from framework.helpers.api import Api


class TestAuthorization:

    @allure.title("TEST1")
    @pytest.mark.api
    @pytest.mark.smoke
    def test_create_new_user(self):
        self.user_json = Generator.new_user_json()
        self.api = Api()
        self.result = self.api.create_user(self.user_json)

        assert self.result.status_code == 201
        assert self.result.json()['email'] == self.user_json['email']

    @allure.title("TEST2")
    @pytest.mark.api
    @pytest.mark.smoke
    def test_verification_new_user(self):
        self.user_json = Generator.new_user_json()
        self.api = Api()
        self.verification_code = self.api.create_user(self.user_json).json()['verification_code']

        self.result = self.api.verification_user(self.verification_code)
        
        assert self.result.status_code == 200
        assert self.result.json()['verified']
