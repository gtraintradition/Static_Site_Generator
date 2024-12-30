import unittest

from textnode import TextNode
from text_enums import TextType

from text_processing import *


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


class Test_extract_markdown_images(unittest.TestCase):

    def test_2_img_links_in_1_str(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])


    def test_str_is_entire_img_link(self):
        text = "![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(extract_markdown_images(text), [('rick roll', 'https://i.imgur.com/aKaOqIh.gif')])


    def test_no_img_link_in_str(self):
        text = "This is a test."
        self.assertEqual(extract_markdown_images(text), [])


    def test_empty_string(self):
        text = ""
        self.assertEqual(extract_markdown_images(text), [])


    def test_arg_passed_not_str(self):
        text = []
        with self.assertRaises(ValueError, msg="Expected ValueError"):
            extract_markdown_images(text)


    ###### Boot.dev test
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)



class Test_extract_markdown_links(unittest.TestCase):

    def test_2_links_in_1_str(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')])


    def test_2_links_1_str(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')])


    def test_no_link_in_str(self):
        text = "This is a test."
        self.assertEqual(extract_markdown_links(text), [])


    def test_empty_string(self):
        text = ""
        self.assertEqual(extract_markdown_links(text), [])


    def test_arg_passed_not_str(self):
        text = []
        with self.assertRaises(ValueError, msg="Expected ValueError"):
            extract_markdown_links(text)


    ###### Boot.dev test
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )


if __name__ == "__main__":
    unittest.main()