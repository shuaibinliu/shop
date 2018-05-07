# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
import uuid
from config.status import response_ok as ok
from common.get_model_return_list import get_model_return_list


class CAddress():
    def __init__(self):
        from config.status import response_error
        from config.status_code import error_param_miss
        from config.messages import error_messages_param_miss
        self.param_miss = {}
        self.param_miss["status"] = response_error
        self.param_miss["status_code"] = error_param_miss
        self.param_miss["messages"] = error_messages_param_miss

        from config.status import response_system_error
        from config.messages import error_system_error
        self.system_error = {}
        self.system_error["status"] = response_system_error
        self.system_error["messages"] = error_system_error

        from services.SAddress import SAddress
        self.address = SAddress()
        from services.SUsers import SUsers
        self.users = SUsers()

    def get_address_by_uid(self):
        args = request.args.to_dict()
        if "token" not in args:
            return self.param_miss

        #todo uid 验证未实现
        uid = args.get("token")
        res_get_all = {}

        try:
            address_info_list = []
            userinfo = self.users.get_uname_utel_by_uid(uid)
            address_list = get_model_return_list(self.address.get_Address_by_Uid(uid))
            for address_info in address_list:
                address_info["USname"] = userinfo.USname
                address_info["UStelphone"] = userinfo.UStelphone
                address_info_list.append(address_info)
            res_get_all["data"] = address_info_list
            res_get_all["status"] = ok
            from config.messages import messages_get_cart_success as msg
            res_get_all["message"] = msg
            return res_get_all

        except Exception as e:
            print(e.message)
            return self.system_error