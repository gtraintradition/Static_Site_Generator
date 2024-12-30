import unittest

from textnode import TextNode
from text_enums import TextType

from text_processing import *



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