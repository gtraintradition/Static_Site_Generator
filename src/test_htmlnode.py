import unittest

from htmlnode import HTMLNode, LeafNode


d1 = {
    "href": "https://www.google.com", 
    "target": "_blank",
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

    def test_no_children(self):
        # Making sure LeafNode doesn't accept more than 3 args (no children)
        with self.assertRaises(TypeError, msg="Expected TypeError"):
            leaf_node1 = LeafNode("tag name 2", "second  value", lc1, d1)

    def test__repr__(self):
        self.assertEqual(leaf_node1.__repr__(), "HTMLNode(a, Click me!, None, {'href': 'https://www.google.com', 'target': '_blank'})")


    def test_to_html(self):
        self.assertEqual(leaf_node1.to_html(), "<a href=\"https://www.google.com\" target=\"_blank\">Click me!</a>")



if __name__ == "__main__":
    unittest.main()