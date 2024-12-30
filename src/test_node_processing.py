import unittest

from textnode import TextNode
from htmlnode import LeafNode
from node_processing import *


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
        

class Test_split_nodes_delimiter(unittest.TestCase):

    def test_process_code(self):
        text_node = TextNode("This is text with a `code block` word", TextType.TEXT)
        processed_node = split_nodes_delimiter([text_node], "`", TextType.CODE)
        self.assertEqual(str(processed_node), "[TextNode(This is text with a , TextType.TEXT, None), TextNode(code block, TextType.CODE, None), TextNode( word, TextType.TEXT, None)]")
        

    def test_process_only_code(self):
        text_node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
        text_node2 = TextNode("This is text with an *italic block* word", TextType.TEXT)
        text_node3 = TextNode("This is text with a **bold block** word", TextType.TEXT)
        processed_node = split_nodes_delimiter([text_node1, text_node2, text_node3], "`", TextType.CODE)
        self.assertEqual(str(processed_node), "[TextNode(This is text with a , TextType.TEXT, None), TextNode(code block, TextType.CODE, None), TextNode( word, TextType.TEXT, None), TextNode(This is text with an *italic block* word, TextType.TEXT, None), TextNode(This is text with a **bold block** word, TextType.TEXT, None)]")


    def test_process_italic(self):
        text_node = TextNode("This is text with an *italic block* word", TextType.TEXT)
        processed_node = split_nodes_delimiter([text_node], "*", TextType.ITALIC)
        self.assertEqual(str(processed_node), "[TextNode(This is text with an , TextType.TEXT, None), TextNode(italic block, TextType.ITALIC, None), TextNode( word, TextType.TEXT, None)]")


    def test_process_only_italic(self):
        text_node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
        text_node2 = TextNode("This is text with an *italic block* word", TextType.TEXT)
        text_node3 = TextNode("This is text with a **bold block** word", TextType.TEXT)
        processed_node = split_nodes_delimiter([text_node1, text_node2, text_node3], "*", TextType.ITALIC)
        self.assertEqual(str(processed_node), "[TextNode(This is text with a `code block` word, TextType.TEXT, None), TextNode(This is text with an , TextType.TEXT, None), TextNode(italic block, TextType.ITALIC, None), TextNode( word, TextType.TEXT, None), TextNode(This is text with a **bold block** word, TextType.TEXT, None)]")


    def test_process_bold(self):
        text_node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        processed_node = split_nodes_delimiter([text_node], "**", TextType.BOLD)
        self.assertEqual(str(processed_node), "[TextNode(This is text with a , TextType.TEXT, None), TextNode(bold block, TextType.BOLD, None), TextNode( word, TextType.TEXT, None)]")


    def test_process_only_bold(self):
        text_node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
        text_node2 = TextNode("This is text with an *italic block* word", TextType.TEXT)
        text_node3 = TextNode("This is text with a **bold block** word", TextType.TEXT)
        processed_node = split_nodes_delimiter([text_node1, text_node2, text_node3], "**", TextType.BOLD)
        self.assertEqual(str(processed_node), "[TextNode(This is text with a `code block` word, TextType.TEXT, None), TextNode(This is text with an *italic block* word, TextType.TEXT, None), TextNode(This is text with a , TextType.TEXT, None), TextNode(bold block, TextType.BOLD, None), TextNode( word, TextType.TEXT, None)]")


    def test_process_multiple_of_same_type(self):
        text_node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
        text_node2 = TextNode("This is text with an *italic block* word", TextType.TEXT)
        text_node3 = TextNode("This is text with a **bold block** word", TextType.TEXT)
        text_node4 = TextNode("This is text with a `code block` word", TextType.TEXT)
        text_node5 = TextNode("This is text with an *italic block* word", TextType.TEXT)
        processed_node = split_nodes_delimiter([text_node1, text_node2, text_node3, text_node4, text_node5], "*", TextType.ITALIC)
        self.assertEqual(str(processed_node), "[TextNode(This is text with a `code block` word, TextType.TEXT, None), TextNode(This is text with an , TextType.TEXT, None), TextNode(italic block, TextType.ITALIC, None), TextNode( word, TextType.TEXT, None), TextNode(This is text with a **bold block** word, TextType.TEXT, None), TextNode(This is text with a `code block` word, TextType.TEXT, None), TextNode(This is text with an , TextType.TEXT, None), TextNode(italic block, TextType.ITALIC, None), TextNode( word, TextType.TEXT, None)]")


    ##### boot.dev checks below
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )





if __name__ == "__main__":
    unittest.main()