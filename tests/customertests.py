import unittest
from unittest.mock import patch
from datautils import customerdata


class TestCustomer(unittest.TestCase):

    def test_vaidate_customer(self):
        gm = customerdata.customer(100, "General Motors", "info@gm.com")
        self.assertTrue(gm.validate(),"Validation failed")
        gm = customerdata.customer(100, "General Motors", "gm.com")
        self.assertFalse(gm.validate(), "Validation failed")
        gm = customerdata.customer("100XY", "General Motors", "info@gm.com")
        self.assertFalse(gm.validate(),"Validation failed")

