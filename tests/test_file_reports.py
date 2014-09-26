# Copyright (c) 2009-2014 Arman Noroozian

from unittest import TestCase
import pyvt
import json


class QueryFileReports(TestCase):

    def setUp(self):
        self.api = pyvt.pyvt('~/.virustotal.key')

    def test_retrieve_file_report(self):
        """
            Tests if pyasn is consistently loaded and that it returns a consistent answer
        """
        response = self.api.retrieve('8725ffa2f7467e5f2147058a512ea65c6d349927d4ae064a69bd1348d8d002c2')
        print(json.dumps(response, indent=2))

    def test_retrieve_multiple_file_reports(self):
        """
            Tests if pyasn is consistently loaded and that it returns a consistent answer
        """
        response = self.api.retrieve(['8725ffa2f7467e5f2147058a512ea65c6d349927d4ae064a69bd1348d8d002c2',
                                      '5fc71212d5f80194f946cc9239d030aae8b51879ec22bd6f9a793c49e543d1c0',
                                      '2a48165551c8f91091d6495d36e96ab5a5196b1c6dc999d8966881c7e7306762'])
        print(json.dumps(response, indent=2))
