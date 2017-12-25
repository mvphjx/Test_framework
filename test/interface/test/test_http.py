import unittest

from utils.assertion import assertHTTPCode
from utils.client import HTTPClient
from utils.log import logger


class TestHTTP(unittest.TestCase):
    URL1 = "http://www.baidu.com"
    URL2 = "http://192.168.129.107:7950X/abisweb"
    URL3 = "https://mvphjx.github.io/starDemo/LearnAndTest/notexist.html"

    def setUp(self):
        pass

    def subTest1(self):
        self.client = HTTPClient(url=self.URL1, method='GET')
        res = self.client.send()
        logger.debug(res.text)
        assertHTTPCode(res, [200])
        self.assertIn('百度一下，你就知道', res.text)

    def subTest2(self):
        self.client = HTTPClient(url=self.URL2, method='GET')
        res = self.client.send()
        logger.debug(res.text)
        assertHTTPCode(res, [200])
        self.assertIn('abisweb', res.text)

    def subTest3(self):
        self.client = HTTPClient(url=self.URL3, method='GET')
        res = self.client.send()
        logger.debug(res.text)
        assertHTTPCode(res, [200])
        self.assertIn('github', res.text)

    def test_http(self):
        with self.subTest(data="百度"):
            self.subTest1()
        with self.subTest(data="abisweb"):
            self.subTest2()
        with self.subTest(data="github"):
            self.subTest3()
