__author__ = 'arman'

from unittest import TestCase
import json
import pyvt


class ScanURLS(TestCase):
    def setUp(self):
        self.api = pyvt.API('~/.virustotal.key')

    def test_scan_single_url(self):
        response, fail = self.api.scan('http://3dtaller.com.ar/')
        print(json.dumps(response, indent=2))

    def test_scan_single_url_blocking(self):
        response, fail = self.api.scan('http://3dtaller.com.ar/', blocking=True)
        print(json.dumps(response, indent=2))

    def test_scan_multiple_urls_blocking(self):
        response, fail = self.api.scan(['http://3dtaller.com.ar/',
                                        'http://3dtaller.com.ar/wp-content/themes/theme1392/js/jquery.loader.js',
                                        'http://3dtaller.com.ar/wp-includes/js/swfobject.js',
                                        'http://3dtaller.com.ar/wp-content/themes/theme1392/js/modernizr-2.0.js'],)
        print(json.dumps(response, indent=2))

    def test_scan_multiple_urls_blocking(self):
        response, fail = self.api.scan(['http://3dtaller.com.ar/',
                                        'http://3dtaller.com.ar/wp-content/themes/theme1392/js/jquery.loader.js',
                                        'http://3dtaller.com.ar/wp-includes/js/swfobject.js',
                                        'http://3dtaller.com.ar/wp-content/themes/theme1392/js/modernizr-2.0.js'], blocking=True)
        print(json.dumps(response, indent=2))
