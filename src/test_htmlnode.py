import unittest
from htmlnode import HTMLNode, LeafNode

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


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_notag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_a_props(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://www.debian.org/"})
        self.assertEqual(node.to_html(), '<a href="https://www.debian.org/">Hello, world!</a>')

    def test_leaf_to_html_p_novalue(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()
