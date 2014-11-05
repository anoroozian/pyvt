__author__ = 'arman'

from unittest import TestCase
import json
import pyvt

class ScanURLS(TestCase):
    def setUp(self):
        self.api = pyvt.API('~/.virustotal.key')

    def test_scan_single_url(self):
        self.api._urls_per_retrieve = 4
        response = self.api.retrieve('http://3dtaller.com.ar/')
        print(json.dumps(response, indent=2))

    def test_scan_multiple_urls_within_limit(self):
        self.api._urls_per_retrieve = 4
        response = self.api.retrieve(['http://3dtaller.com.ar/',
                                      'http://3dtaller.com.ar/wp-content/themes/theme1392/js/jquery.loader.js',
                                      'http://3dtaller.com.ar/wp-includes/js/swfobject.js',
                                      'http://3dtaller.com.ar/wp-content/themes/theme1392/js/modernizr-2.0.js'])
        print(json.dumps(response, indent=2))

    def test_scan_multiple_urls_exceed_limit_1(self):
        self.api._urls_per_retrieve = 1
        response = self.api.retrieve(['http://3dtaller.com.ar/',
                                      'http://3dtaller.com.ar/wp-content/themes/theme1392/js/jquery.loader.js',
                                      'http://3dtaller.com.ar/wp-includes/js/swfobject.js',
                                      'http://3dtaller.com.ar/wp-content/themes/theme1392/js/modernizr-2.0.js',
                                      'http://3dtaller.com.ar/wp-content/themes/theme1392/js/custom.js'])
        print(json.dumps(response, indent=2))

    def test_scan_multiple_urls_exceed_limit_2(self):
        self.api._urls_per_retrieve = 2
        response = self.api.retrieve(['http://3dtaller.com.ar/',
                                      'http://3dtaller.com.ar/wp-content/themes/theme1392/js/jquery.loader.js',
                                      'http://3dtaller.com.ar/wp-includes/js/swfobject.js',
                                      'http://3dtaller.com.ar/wp-content/themes/theme1392/js/modernizr-2.0.js',
                                      'http://3dtaller.com.ar/wp-content/themes/theme1392/js/custom.js',
                                      'http://3dtaller.com.ar/wp-content/themes/theme1392/js/jquery-1.6.4.min.js'])
        print(json.dumps(response, indent=2))
