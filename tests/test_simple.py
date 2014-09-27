# Copyright (c) 2009-2014 Arman Noroozian
from unittest import TestCase
import pyvt
from pyvt import API_Constants


class Simple(TestCase):
    def setUp(self):
        self.api = pyvt.API('~/.virustotal.key')

    def test_whatis(self):
        self.assertEqual(API_Constants.SCANID, self.api._whatis(
            "1d1db799fbe0fea8407d388f7317d8ae783d81cbfa32b5b7e9455bdf7d2ffeab-1406914632"))

        self.assertEqual(API_Constants.URL, self.api._whatis("http://3dtaller.com.ar/"))

        self.assertEqual(API_Constants.DOMAIN, self.api._whatis("3dtaller.com.ar"))

        self.assertEqual(API_Constants.IP, self.api._whatis("173.236.179.77"))

        # TODO: test other types of queirs, files, hashes, ...

    def test_grouping(self):
        items = [1, 2, 3, 4, 5]
        self.assertListEqual([[1,2], [3,4], [5]], self.api._grouped(items, 2))

        items = [1]
        self.assertListEqual([[1]], self.api._grouped(items, 2))