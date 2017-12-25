import unittest
import ddt
from utils.assertion import assertHTTPCode
from utils.client import HTTPClient
from utils.log import logger


@ddt.ddt
class TestDdtHTTP(unittest.TestCase):
    URL1 = "http://www.baidu.com"
    URL2 = "http://192.168.129.107:7950X/abisweb"
    URL3 = "https://mvphjx.github.io/starDemo/LearnAndTest/notexist.html"

    def setUp(self):
        pass

    def subTestUrl(self, url):
        self.client = HTTPClient(url=url, method='GET')
        res = self.client.send()
        logger.debug(res.text)
        assertHTTPCode(res, [200])
        self.assertIn('百度一下，你就知道', res.text)

    @ddt.data(['http://www.baidu.com'], ['http://www.baidu.com'])
    @ddt.unpack
    def test_http(self, url):
        self.subTestUrl(url)
