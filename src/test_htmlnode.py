import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_parents(self):
        grandchild_one = LeafNode("b", "gchild 1")
        grandchild_two = LeafNode("i", "gchild 2")
        child_one = ParentNode("p", [grandchild_one, grandchild_two])
        child_two = ParentNode("span", [grandchild_two, grandchild_one], {"class": "childs"})
        parent_node = ParentNode("div", [child_one, child_two])
        self.assertEqual(
            parent_node.to_html(),
            '<div><p><b>gchild 1</b><i>gchild 2</i></p><span class="childs"><i>gchild 2</i><b>gchild 1</b></span></div>',
        )


if __name__ == "__main__":
    unittest.main()
