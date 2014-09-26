# Copyright (c) 2009-2014 Arman Noroozian

from unittest import TestCase
import pyvt
import json


class QueryDomains(TestCase):

    def setUp(self):
        self.api = pyvt.pyvt('~/.virustotal.key')

    def test_retrieve_domain(self):
        """
            Tests if pyasn is consistently loaded and that it returns a consistent answer
        """
        response = self.api.retrieve('3dtaller.com.ar')
        print(json.dumps(response, indent=2))