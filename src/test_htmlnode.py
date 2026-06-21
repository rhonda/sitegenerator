import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_prop_1(self):
        node = HTMLNode(props={ "href": "https://www.debian.org/"})
        props = node.props_to_html()
        self.assertEqual(props, ' href="https://www.debian.org/"')

    def test_prop_2(self):
        node = HTMLNode(props={
            "href": "https://www.debian.org/",
            "target": "_blank"}
                        )
        props = node.props_to_html()
        self.assertEqual(props, ' href="https://www.debian.org/" target="_blank"')

    def test_prop_empty(self):
        node = HTMLNode(props={})
        props = node.props_to_html()
        self.assertEqual(props, '')

    def test_prop_none(self):
        node = HTMLNode(props=None)
        props = node.props_to_html()
        self.assertEqual(props, '')

    def test_prop_default(self):
        node = HTMLNode()
        props = node.props_to_html()
        self.assertEqual(props, '')


if __name__ == "__main__":
    unittest.main()
