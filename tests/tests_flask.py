from __future__ import print_function

from faker import Faker
from flask import Flask, request
from flask_restful import Api

fake = Faker()

from halolib.flask.utilx import status
from bian.abs_bian_srv import AbsBianMixin
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
            assert ret.code == status.HTTP_200_OK

    def test_get_request_with_ref_returns_a_given_string(self):
        with app.test_request_context('/?name=Peter'):
            self.t1 = T1()
            ret = self.t1.process_get(request, {"cr_reference_id": "123"})
            assert ret.code == status.HTTP_200_OK

    def test_get_request_with_ref_bq_returns_a_given_string(self):
        with app.test_request_context('/?name=Peter'):
            self.t1 = T1()
            try:
                ret = self.t1.process_get(request, {"cr_reference_id": "123", "behavior_qualifier": "456"})
                assert False
            except Exception as e:
                print(str(e) + " " + str(type(e).__name__))
                assert type(e).__name__ == 'BianMethodNotImplementedException'

    def test_get_request_with_ref_bq_not_returns_a_given_string(self):
        with app.test_request_context('/?name=Peter'):
            self.t1 = T1()
            try:
                ret = self.t1.process_get(request, {"cr_reference_id": "123", "behavior_qualifier": "457"})
                assert False
            except Exception as e:
                print(str(e) + " " + str(type(e)))
                assert type(e).__name__ == "IllegalBQException"


    def test_post_request_returns_a_given_string(self):
        with app.test_request_context('/?name=Peter'):
            self.t1 = T1()
            ret = self.t1.process_post(request, {})
            if ret.code == status.HTTP_200_OK:
                return True

    def test_patch_request_returns_a_given_string(self):
        with app.test_request_context('/?name=Peter'):
            self.t1 = T1()
            ret = self.t1.process_patch(request, {})
            if ret.code == status.HTTP_200_OK:
                return True

    def test_put_request_returns_a_given_string(self):
        with app.test_request_context('/?name=Peter'):
            self.t1 = T1()
            ret = self.t1.process_put(request, {})
            if ret.code == status.HTTP_200_OK:
                return True

    def test_delete_request_returns_a_given_string(self):
        with app.test_request_context('/?name=Peter'):
            self.t1 = T1()
            ret = self.t1.process_delete(request, {})
            if ret.code == status.HTTP_200_OK:
                return True
