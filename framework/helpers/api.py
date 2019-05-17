import allure
import requests

url = 'http://api.dev.btm.idl.local'


class Api:

    @allure.step
    def create_user(self, user_json):
        return requests.post(url + '/user', json=user_json)

    @allure.step
    def verification_user(self, verification_code):
        return requests.get(url + '/user/verification/{:s}'.format(verification_code))
