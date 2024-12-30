import unittest

from block_processing import *



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





if __name__ == "__main__":
    unittest.main()