import unittest


from markdown_processing import *



class Test_markdown_to_blocks(unittest.TestCase):

    def test_3_blocks_1_w_3_newlines_whitespace(self):
        text = "# This is a heading    \n\n    This is a paragraph of text. It has some **bold** and *italic* words inside of it.    \n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n\n"
        self.assertEqual(markdown_to_blocks(text), ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item'])

    def test_1_block_whitespace(self):
        text = "   # This is a heading    "
        self.assertEqual(markdown_to_blocks(text), ['# This is a heading'])

    def test_empty_string(self):
        text = ""
        self.assertEqual(markdown_to_blocks(text), [])

    def test_wrong_arg(self):
        text = 4
        with self.assertRaises(ValueError, msg="Expcted ValueError"):
            markdown_to_blocks(text)

    #### Boot.dev tests below, "bad" formatting is necessary
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )



class Test_markdown_to_html_nodes(unittest.TestCase):

    def test_markdown_to_html_node_each_type(self):
        markdown = """#### Header 4

This is a test paragraph. This is a test paragraph. This is a test paragraph. This is a test paragraph. This is a test paragraph. This is a test paragraph. This is a test paragraph. This is a test paragraph. This is a test paragraph. 

* Listing an item
- Listing an other item
- Listing one more item
* Listing a final item

[NASA](https://www.nasa.gov/)

```
some code
here again code
one last code
```

![Hubble Reinartz](https://apod.nasa.gov/apod/image/2412/NGC4753_HubbleReinartz_3900.jpg)

1. Listing a 1st item
2. Listing a 2nd item
3. Listing a 3rd item
4. Listing a 4th item
5. Listing a 5th item

`
some code with only one backtick
here again code with only one backtick
one last code with only one backtick
`

*Some italic text. Some italic text. Some italic text. Some italic text. Some italic text. Some italic text. *

>This is a quote.
>And an other one.
>And an other.
>This is the final quote.

**Some bold text. Some bold text. Some bold text. Some bold text. Some bold text. Some bold text. Some bold text. Some bold text.**"""

        self.assertEqual(str(markdown_to_html_node(markdown)), """ParentNode(div, [LeafNode(h4, Header 4, None), LeafNode(p, This is a test paragraph. This is a test paragraph. This is a test paragraph. This is a test paragraph. This is a test paragraph. This is a test paragraph. This is a test paragraph. This is a test paragraph. This is a test paragraph., None), LeafNode(ul, <li>Listing an item</li>
<li>Listing an other item</li>
<li>Listing one more item</li>
<li>Listing a final item</li>, None), LeafNode(a, NASA, {'href': 'https://www.nasa.gov/'}), LeafNode(code, 
some code
here again code
one last code
, None), LeafNode(img, , {'src': 'https://apod.nasa.gov/apod/image/2412/NGC4753_HubbleReinartz_3900.jpg', 'alt': 'Hubble Reinartz'}), LeafNode(ol, <li>Listing a 1st item</li>
<li>Listing a 2nd item</li>
<li>Listing a 3rd item</li>
<li>Listing a 4th item</li>
<li>Listing a 5th item</li>, None), LeafNode(code, 
some code with only one backtick
here again code with only one backtick
one last code with only one backtick
, None), LeafNode(i, Some italic text. Some italic text. Some italic text. Some italic text. Some italic text. Some italic text. , None), LeafNode(blockquote, This is a quote.
And an other one.
And an other.
This is the final quote., None), LeafNode(b, Some bold text. Some bold text. Some bold text. Some bold text. Some bold text. Some bold text. Some bold text. Some bold text., None)], None)""")




if __name__ == "__main__":
    unittest.main()