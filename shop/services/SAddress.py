# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from models.model import Address

from SBase import SBase, close_session


class SAddress(SBase):

    def __init__(self):
        super(SAddress, self).__init__()

    @close_session
    def get_Address_by_Uid(self, uid):
        return self.session.query(Address.ADid, Address.ADabo, Address.ADcity, Address.ADcounty, Address.ADprovince)\
            .filter(Address.USid == uid).all()

    @close_session
    def update_Address(self, adid, address):
        self.session.query(Address).filter(Address.ADid == adid).update(address)
