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

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )


    def test_to_html_props2(self):
        # empty props
        dummyHTML2 = HTMLNode("tag name 1", 
                        "html tag value",
                        lc1,
                        )
        self.assertEqual(dummyHTML2.props_to_html(), "")


    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )


    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, None, {'class': 'primary'})",
        )


    def test__repr__2(self):   
        self.assertEqual(node1.__repr__(), "HTMLNode(tag name 1, html tag value, ['children1', 'children2', 'children3'], {'href': 'https://www.google.com', 'target': '_blank'})")


    def test_props_to_html3(self):
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


    def test_to_html_no_children3(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")



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


    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )


    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )



if __name__ == "__main__":
    unittest.main()