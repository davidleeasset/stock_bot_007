from unittest import TestCase

from services.cool_service import Cool


class TestYes(TestCase):
    def test_yes(self):
        assert Cool().a()
