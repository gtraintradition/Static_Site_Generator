import unittest

from htmlnode import HTMLNode


d1 = {
    "href": "https://www.google.com", 
    "target": "_blank",
}
lc1 = ["children1", "children2", "children3"]

node1 = HTMLNode("tag name 1", "html tag value", lc1, d1)
node2 = HTMLNode("tag name 2", "second  value", lc1, d1)


class TestHTMLNode(unittest.TestCase):

    def test__repr__(self):   
        self.assertEqual(node1.__repr__(), "HTMLNode(tag name 1, html tag value, ['children1', 'children2', 'children3'], {'href': 'https://www.google.com', 'target': '_blank'})")

    def test_props_to_html(self):
        self.assertEqual(node1.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")
        
    def test_to_html(self):
        with self.assertRaises(NotImplementedError, msg="Expected NotImplementedError"):
            node1.to_html()
            node2.to_html()

if __name__ == "__main__":
    unittest.main()