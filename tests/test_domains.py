# Copyright (c) 2009-2014 Arman Noroozian

from unittest import TestCase
import json
import pyvt


class QueryDomains(TestCase):

    def setUp(self):
        self.api = pyvt.API('~/.virustotal.key')

    def test_retrieve_domain(self):
        response = self.api.retrieve('3dtaller.com.ar')
        print(json.dumps(response, indent=2))