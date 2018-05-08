# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from config.Logs import PRINT_API_NAME
from config.status import response_system_error
from config.status_code import error_wrong_apis
from config.messages import error_messages_wrong_api
from control.CAddress import CAddress


class AAddress(Resource):
    def __int__(self):
        self.apis_wrong = {}
        self.apis_wrong["status"] = response_system_error
        self.apis_wrong["status_code"] = error_wrong_apis
        self.apis_wrong["messages"] = error_messages_wrong_api

    def post(self, address):
        print(PRINT_API_NAME.format(address))

        control_address = CAddress()
        apis = {
            "delete_address": "control_address.del_address()",
            "update": "control_address.add_or_update_address()"
        }

        if address in apis:
            return eval(apis[address])

        return self.apis_wrong

    def get(self, address):
        print(PRINT_API_NAME.format(address))

        control_address = CAddress()
        apis = {
            "get_all": "control_address.get_address_by_uid()"
        }

        if address in apis:
            return eval(apis[address])

        return self.apis_wrong
