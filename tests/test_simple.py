# Copyright (c) 2009-2014 Arman Noroozian
from unittest import TestCase
import pyvt
import json


class Simple(TestCase):
    def setUp(self):
        self.api = pyvt.pyvt('~/.virustotal.key')

    def test_whatis(self):
        self.assertEqual(self.api._CONST_SCANID, self.api._whatis(
            "1d1db799fbe0fea8407d388f7317d8ae783d81cbfa32b5b7e9455bdf7d2ffeab-1406914632"))

        self.assertEqual(self.api._CONST_URL, self.api._whatis("http://3dtaller.com.ar/"))

        self.assertEqual(self.api._CONST_DOMAIN, self.api._whatis("3dtaller.com.ar"))

        self.assertEqual(self.api._CONST_IP, self.api._whatis("173.236.179.77"))

        # TODO: test other types of queirs, files, hashes, ...

    def test_grouping(self):
        items = [1, 2, 3, 4, 5]
        self.assertListEqual([[1,2], [3,4], [5]], self.api._grouped(items, 2))

        items = [1]
        self.assertListEqual([[1]], self.api._grouped(items, 2))