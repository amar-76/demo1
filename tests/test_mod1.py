from unittest import TestCase
from amazon.mod1 import hello_world


class Mod1Test(TestCase):

    def test_hello_world(self):
        assert hello_world() == 'Hello World!!'
