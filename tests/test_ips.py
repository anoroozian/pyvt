# Copyright (c) 2009-2014 Arman Noroozian

from unittest import TestCase
import json
import pyvt


class QueryIPs(TestCase):

    def setUp(self):
        self.api = pyvt.API('~/.virustotal.key')

    def test_retrieve_ip(self):
        response = self.api.retrieve('173.236.179.77')
        print(json.dumps(response, indent=2))

    def test_retrieve_multiple_ips(self):
        response = self.api.retrieve(['173.236.179.77', '66.33.221.102'])
        print(json.dumps(response, indent=2))