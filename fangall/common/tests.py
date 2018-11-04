import re

from ddt import ddt, data, unpack

from django.test import TestCase

from common.utils import to_md5_hex, gen_mobile_code, gen_captcha_text


class TestHelpers(TestCase):

    def test_foo(self):
        pass

    def test_bar(self):
        pass


@ddt
class TestUtils(TestCase):

    @data(('123456', 'e10adc3949ba59abbe56e057f20f883e'),
          ('1qaz2wsx', '1c63129ae9db9c60c3e8aa94d3e00495'),
          ('123123', '4297f44b13955235245b2497399d7a93'))
    @unpack
    def test_to_md5_hex(self, origin_str, md5_str):
        self.assertEqual(md5_str, to_md5_hex(origin_str))

    def test_gen_mobile_code(self):
        pattern = re.compile(r'^\d{6}$')
        for _ in range(100):
            self.assertIsNotNone(pattern.match(gen_mobile_code()))

    def test_gen_captcha_text(self):
        pattern = re.compile(r'^[0-9a-zA-Z]{4}$')
        for _ in range(100):
            self.assertIsNotNone(pattern.match(gen_captcha_text()))
