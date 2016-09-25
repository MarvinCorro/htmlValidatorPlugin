import unittest
import htmlValidatorPlugin as sut


@unittest.skip("Don't forget to test!")
class HtmlvalidatorpluginTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.htmlValidatorPlugin_example()
        self.assertEqual("Happy Hacking", result)
