import unittest

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



class Test_text_to_textnodes(unittest.TestCase):

    # the following one is from boot.dev solution and asignment
    def test_1_of_each_texttype(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertEqual(str(text_to_textnodes(text)), "[TextNode(This is , TextType.TEXT, None), TextNode(text, TextType.BOLD, None), TextNode( with an , TextType.TEXT, None), TextNode(italic, TextType.ITALIC, None), TextNode( word and a , TextType.TEXT, None), TextNode(code block, TextType.CODE, None), TextNode( and an , TextType.TEXT, None), TextNode(obi wan image, TextType.IMAGE, https://i.imgur.com/fJRm4Vk.jpeg), TextNode( and a , TextType.TEXT, None), TextNode(link, TextType.LINK, https://boot.dev)]")

    def test_only_text(self):
        text = "This is only text"
        self.assertEqual(str(text_to_textnodes(text)), "[TextNode(This is only text, TextType.TEXT, None)]")

    def test_only_1_italic(self):
        text = "*This is only text*"
        self.assertEqual(str(text_to_textnodes(text)), "[TextNode(This is only text, TextType.ITALIC, None)]")

    def test_only_1_image(self):
        text = "![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(str(text_to_textnodes(text)), "[TextNode(rick roll, TextType.IMAGE, https://i.imgur.com/aKaOqIh.gif)]")

    def test_wrong_arg(self):
        with self.assertRaises(ValueError, msg="Expected ValueError"):
            text_to_textnodes(456)

    # not sure about the following one
    def test_empty_string(self):
        text = ""
        self.assertEqual(str(text_to_textnodes(text)), "[TextNode(, TextType.TEXT, None)]")





if __name__ == "__main__":
    unittest.main()