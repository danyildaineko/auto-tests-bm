from datetime import datetime
import allure


class Generator:



    @staticmethod
    def new_user_json():
        email = datetime.today().strftime("%d%m%H%M%S")
        new_user = {
            "email": "{}@auto.test".format('Auto' + email),
            "first_name": 'first_name',
            "password": "qweasd",
            "password_confirmation": "qweasd",
            "sub_id": ""
        }
        return new_user