import unittest
from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another node", TextType.LINK, "https://debian.org/")
        self.assertNotEqual(node, node2)

    def test_text_diff(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_type_diff(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_diff(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://debian.org/")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_urlnone(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)



class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.debian.org/")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href": "https://www.debian.org/"})

    def test_image(self):
        node = TextNode(None, TextType.IMAGE, "https://www.debian.org/favicon.ico")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src": "https://www.debian.org/favicon.ico"})



class TestTextSplitNodeDelimeter(unittest.TestCase):
    def test_MDToText_bold(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        split_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)
        self.assertEqual(split_nodes, [
            TextNode("This is text with a ", TextType.TEXT), 
            TextNode("bolded phrase", TextType.BOLD), 
            TextNode(" in the middle", TextType.TEXT), 
            ])

    def test_MDToText_three_bold(self):
        node = TextNode("This is text with a **bolded phrase** in the **middle", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)

    def test_MDToText_two_italic(self):
        node = TextNode("_Two_ italic parts at start and _end_", TextType.TEXT)
        split_nodes = split_nodes_delimiter([node], '_', TextType.ITALIC)
        self.assertEqual(split_nodes, [
            TextNode("Two", TextType.ITALIC), 
            TextNode(" italic parts at start and ", TextType.TEXT), 
            TextNode("end", TextType.ITALIC), 
            ])

    def test_MDToText_bold_italic(self):
        node = TextNode("Now we got **bold** and _italic_ in here.", TextType.TEXT)
        split_nodes = split_nodes_delimiter([node], '_', TextType.ITALIC)
        split_nodes = split_nodes_delimiter(split_nodes, '**', TextType.BOLD)
        self.assertEqual(split_nodes, [
            TextNode("Now we got ", TextType.TEXT), 
            TextNode("bold", TextType.BOLD), 
            TextNode(" and ", TextType.TEXT), 
            TextNode("italic", TextType.ITALIC), 
            TextNode(" in here.", TextType.TEXT), 
            ])


    def test_MDToText_code(self):
        node = TextNode("`This is one big code block`", TextType.TEXT)
        split_nodes = split_nodes_delimiter([node], '`', TextType.CODE)
        self.assertEqual(split_nodes, [
            TextNode("This is one big code block", TextType.CODE),
            ])


if __name__ == "__main__":
    unittest.main()
