from __future__ import print_function

from faker import Faker
from flask import Flask, request
from flask_restful import Api

fake = Faker()

from halolib.flask.utilx import status
from abs_bian_srv import AbsBianMixin
import unittest

app = Flask(__name__)
api = Api(app)
app.config.from_object('settings')


class T1(AbsBianMixin):
    pass


class TestUserDetailTestCase(unittest.TestCase):
    """
    Tests /users detail operations.
    """

    # def setUp(self):
    # self.t1 = T1()

    def test_get_request_returns_a_given_string(self):
        with app.test_request_context('/?name=Peter'):
            self.t1 = T1()
            ret = self.t1.process_get(request, {})
            if ret.code == status.HTTP_200_OK:
                return True
