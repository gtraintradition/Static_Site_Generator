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



class Test_split_nodes_image(unittest.TestCase):


    def test_1_image_in_text(self):
        node1 = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ", TextType.TEXT,)
        self.assertEqual(str(split_nodes_image([node1])), "[TextNode(This is text with a , TextType.TEXT, None), TextNode(rick roll, TextType.IMAGE, https://i.imgur.com/aKaOqIh.gif), TextNode( and , TextType.TEXT, None)]")

    def test_2_images_in_text(self):
        node1 = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT,)
        self.assertEqual(str(split_nodes_image([node1])), "[TextNode(This is text with a , TextType.TEXT, None), TextNode(rick roll, TextType.IMAGE, https://i.imgur.com/aKaOqIh.gif), TextNode( and , TextType.TEXT, None), TextNode(obi wan, TextType.IMAGE, https://i.imgur.com/fJRm4Vk.jpeg)]")

    def test_only_image_in_text(self):
        node1 = TextNode("![rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.TEXT,)
        self.assertEqual(str(split_nodes_image([node1])), "[TextNode(rick roll, TextType.IMAGE, https://i.imgur.com/aKaOqIh.gif)]")

    def test_4_images_in_1_node(self):
        node1 = TextNode("![rick roll](https://i.imgur.com/aKaOqIh.gif)![rick roll](https://i.imgur.com/aKaOqIh.gif)![rick roll](https://i.imgur.com/aKaOqIh.gif)![rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.TEXT,)
        self.assertEqual(str(split_nodes_image([node1])), "[TextNode(rick roll, TextType.IMAGE, https://i.imgur.com/aKaOqIh.gif), TextNode(rick roll, TextType.IMAGE, https://i.imgur.com/aKaOqIh.gif), TextNode(rick roll, TextType.IMAGE, https://i.imgur.com/aKaOqIh.gif), TextNode(rick roll, TextType.IMAGE, https://i.imgur.com/aKaOqIh.gif)]")

    def test_no_images_in_text(self):
        node1 = TextNode("some test text", TextType.TEXT,)
        self.assertEqual(str(split_nodes_image([node1])), "[TextNode(some test text, TextType.TEXT, None)]")

    def test_empty_list(self):
        with self.assertRaises(Exception, msg="Expected Exception"):
            split_nodes_image([])

    def test_wrong_arg(self):
        with self.assertRaises(Exception, msg="Expected Exception"):
            split_nodes_image("test arg")

    def test_3_nodes_list(self):
        node1 = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT,)
        node2 = TextNode("NODE2TEXT ![IMAGE](https://i.LINK.com/LINK.gif) and ![5555](https://i.55555.com/fSFGk.jpeg) and some other text at the end", TextType.TEXT,)
        node3 = TextNode("![IMAGE](https://i.LINK.com/LINK.gif) and ![OUI](https://i.IIIIIII.com/fSFGk.jpeg) and some other text at the end", TextType.TEXT,)
        self.assertEqual(str(split_nodes_image([node1, node2, node3])), "[TextNode(This is text with a , TextType.TEXT, None), TextNode(rick roll, TextType.IMAGE, https://i.imgur.com/aKaOqIh.gif), TextNode( and , TextType.TEXT, None), TextNode(obi wan, TextType.IMAGE, https://i.imgur.com/fJRm4Vk.jpeg), TextNode(NODE2TEXT , TextType.TEXT, None), TextNode(IMAGE, TextType.IMAGE, https://i.LINK.com/LINK.gif), TextNode( and , TextType.TEXT, None), TextNode(5555, TextType.IMAGE, https://i.55555.com/fSFGk.jpeg), TextNode( and some other text at the end, TextType.TEXT, None), TextNode(IMAGE, TextType.IMAGE, https://i.LINK.com/LINK.gif), TextNode( and , TextType.TEXT, None), TextNode(OUI, TextType.IMAGE, https://i.IIIIIII.com/fSFGk.jpeg), TextNode( and some other text at the end, TextType.TEXT, None)]")

    #### boot.dev tests below
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


class Test_split_nodes_link(unittest.TestCase):

    def test_1_link_in_text(self):
        node1 = TextNode("This is text with a link [to boot dev](https://www.boot.dev)", TextType.TEXT,)
        self.assertEqual(str(split_nodes_link([node1])), "[TextNode(This is text with a link , TextType.TEXT, None), TextNode(to boot dev, TextType.LINK, https://www.boot.dev)]")

    def test_2_link_in_text(self):
        node1 = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT,)
        self.assertEqual(str(split_nodes_link([node1])), "[TextNode(This is text with a link , TextType.TEXT, None), TextNode(to boot dev, TextType.LINK, https://www.boot.dev), TextNode( and , TextType.TEXT, None), TextNode(to youtube, TextType.LINK, https://www.youtube.com/@bootdotdev)]")

    def test_only_link_in_text(self):
        node1 = TextNode("[to boot dev](https://www.boot.dev)", TextType.TEXT,)
        self.assertEqual(str(split_nodes_link([node1])), "[TextNode(to boot dev, TextType.LINK, https://www.boot.dev)]")

    def test_4_images_in_1_node(self):
        node1 = TextNode("[to boot dev](https://www.boot.dev)[to boot dev](https://www.boot.dev)[to boot dev](https://www.boot.dev)[to boot dev](https://www.boot.dev)", TextType.TEXT,)
        self.assertEqual(str(split_nodes_link([node1])), "[TextNode(to boot dev, TextType.LINK, https://www.boot.dev), TextNode(to boot dev, TextType.LINK, https://www.boot.dev), TextNode(to boot dev, TextType.LINK, https://www.boot.dev), TextNode(to boot dev, TextType.LINK, https://www.boot.dev)]")

    def test_no_link_in_text(self):
        node1 = TextNode("some test text", TextType.TEXT,)
        self.assertEqual(str(split_nodes_link([node1])), "[TextNode(some test text, TextType.TEXT, None)]")

    def test_empty_list(self):
        with self.assertRaises(Exception, msg="Expected Exception"):
            split_nodes_link([])

    def test_wrong_arg(self):
        with self.assertRaises(Exception, msg="Expected Exception"):
            split_nodes_link("test arg")

    def test_3_nodes_list(self):
        node1 = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT,)
        node2 = TextNode("This 22222nk [to boot dev](https://www.2222222.dev) and [to youtube](https://www.222222e.com/@boot222dev)", TextType.TEXT,)
        node3 = TextNode("This 33333 with a link [to 33333 dev](https://www.boot.dev) and [to3333be](https://www.yo333ube.com/@boo3333tdev)", TextType.TEXT,)
        self.assertEqual(str(split_nodes_link([node1, node2, node3])), "[TextNode(This is text with a link , TextType.TEXT, None), TextNode(to boot dev, TextType.LINK, https://www.boot.dev), TextNode( and , TextType.TEXT, None), TextNode(to youtube, TextType.LINK, https://www.youtube.com/@bootdotdev), TextNode(This 22222nk , TextType.TEXT, None), TextNode(to boot dev, TextType.LINK, https://www.2222222.dev), TextNode( and , TextType.TEXT, None), TextNode(to youtube, TextType.LINK, https://www.222222e.com/@boot222dev), TextNode(This 33333 with a link , TextType.TEXT, None), TextNode(to 33333 dev, TextType.LINK, https://www.boot.dev), TextNode( and , TextType.TEXT, None), TextNode(to3333be, TextType.LINK, https://www.yo333ube.com/@boo3333tdev)]")

    #### boot.dev tests below
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.TEXT),
            ],
            new_nodes,
        )



if __name__ == "__main__":
    unittest.main()