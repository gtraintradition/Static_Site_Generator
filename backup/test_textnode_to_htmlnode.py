import unittest

from textnode import *
from htmlnode import LeafNode
from textnode_to_htmlnode import text_node_to_html_node


class Test_text_node_to_html_node(unittest.TestCase):

    def test_convert_image_node(self):
        dummy = TextNode("alt text", "image", "https://url.org")
        converted = text_node_to_html_node(dummy)
        self.assertEqual(str(converted), "LeafNode(img, , {'src': 'https://url.org', 'alt': 'alt text'})")


    def test_convert_link_node(self):
        dummy = TextNode("anchor text", "link", "https://url.org")
        converted = text_node_to_html_node(dummy)
        self.assertEqual(str(converted), "LeafNode(a, anchor text, {'href': 'https://url.org'})")


    def test_convert_bold_node(self):
        dummy = TextNode("dummy text", "bold", "https://url.org")
        converted = text_node_to_html_node(dummy)
        self.assertEqual(str(converted), "LeafNode(b, dummy text, None)")

    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    def test_leaf_node_passed(self):
        dummyLeafNode1 = LeafNode("p", "This is a paragraph of text.")
        with self.assertRaises(ValueError, msg="Expected ValueError"):
            text_node_to_html_node(dummyLeafNode1)
        

if __name__ == "__main__":
    unittest.main()