import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


d1 = {
    "href": "https://www.google.com", 
    "target": "_blank",
}
d2 = {
    "href": "https://www.duckduckgo.com", 
    "target": "_green_____",
    }
lc1 = ["children1", "children2", "children3"]

node1 = HTMLNode("tag name 1", "html tag value", lc1, d1)
node2 = HTMLNode("tag name 2", "second  value", lc1, d1)

leaf_node1 = LeafNode("a", "Click me!", d1)


class TestHTMLNode(unittest.TestCase):

    def test__repr__(self):   
        self.assertEqual(node1.__repr__(), "HTMLNode(tag name 1, html tag value, ['children1', 'children2', 'children3'], {'href': 'https://www.google.com', 'target': '_blank'})")

    def test_props_to_html(self):
        self.assertEqual(node1.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")
        
    def test_to_html(self):
        with self.assertRaises(NotImplementedError, msg="Expected NotImplementedError"):
            node1.to_html()
            node2.to_html()


class TestLeafNode(unittest.TestCase):

    def test_no_children1(self):
        # Making sure LeafNode doesn't accept more than 3 args (no children)
        with self.assertRaises(TypeError, msg="Expected TypeError"):
            leaf_node1 = LeafNode("tag name 2", "second  value", lc1, d1)

    def test_no_children2(self):
        with self.assertRaises(AttributeError, msg="Expected AttributeError"):
            leaf_node1.children

    def test__repr__(self):
        self.assertEqual(leaf_node1.__repr__(), "LeafNode(a, Click me!, {'href': 'https://www.google.com', 'target': '_blank'})")


    def test_to_html(self):
        # 
        self.assertEqual(leaf_node1.to_html(), "<a href=\"https://www.google.com\" target=\"_blank\">Click me!</a>")


class TestParentNode(unittest.TestCase):

    def test__repr__(self):

        parent_node1 = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )

        parent_node2 = ParentNode(
        "io",
        [
            LeafNode("p", "This is a paragraph of text."),
            parent_node1,
            LeafNode("a", "Click me!", d1),
            LeafNode("gg", "non text"),
        ],
        d2,
        )

        self.assertEqual(parent_node2.__repr__(), "ParentNode(io, [LeafNode(p, This is a paragraph of text., None), ParentNode(p, [LeafNode(b, Bold text, None), LeafNode(None, Normal text, None), LeafNode(i, italic text, None), LeafNode(None, Normal text, None)], None), LeafNode(a, Click me!, {'href': 'https://www.google.com', 'target': '_blank'}), LeafNode(gg, non text, None)], {'href': 'https://www.duckduckgo.com', 'target': '_green_____'})")


    def test_no_value(self):

        parent_node1 = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
    
        with self.assertRaises(AttributeError, msg="Expected AttributeErrore"):
            parent_node1.value


    def test_to_html(self):
        # testing with nested ParentNode, and multiple children

        parent_node1 = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )

        parent_node2 = ParentNode(
        "io",
        [
            LeafNode("p", "This is a paragraph of text."),
            parent_node1,
            LeafNode("a", "Click me!", d1),
            LeafNode("gg", "non text"),
        ],
        d2,
        )

        #
        self.assertEqual(parent_node2.to_html(), "<io href=\"https://www.duckduckgo.com\" target=\"_green_____\"><p>This is a paragraph of text.</p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><a href=\"https://www.google.com\" target=\"_blank\">Click me!</a><gg>non text</gg></io>")


    def test_no_children(self):

        parent_node3 = ParentNode("nc",[],)
        self.assertEqual(parent_node3.to_html(), "<nc></nc>")




if __name__ == "__main__":
    unittest.main()