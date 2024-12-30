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


class Test_block_to_block_type(unittest.TestCase):

    # Heading tests
    def test_1_hashtag_1_space(self):
        self.assertEqual(block_to_block_type("# this is a test"), BlockTypes.HEADING)
    def test_2_hashtag_1_space(self):
        self.assertEqual(block_to_block_type("## this is a test"), BlockTypes.HEADING)
    def test_3_hashtag_1_space(self):
        self.assertEqual(block_to_block_type("### this is a test"), BlockTypes.HEADING)
    def test_4_hashtag_1_space(self):
        self.assertEqual(block_to_block_type("#### this is a test"), BlockTypes.HEADING)
    def test_5_hashtag_1_space(self):
        self.assertEqual(block_to_block_type("##### this is a test"), BlockTypes.HEADING)
    def test_6_hashtag_1_space(self):
        self.assertEqual(block_to_block_type("###### this is a test"), BlockTypes.HEADING)
    def test_2_hashtag_no_space(self):
        self.assertEqual(block_to_block_type("##this is a test"), BlockTypes.PARAGRAPH)
    def test_6_hashtag_no_space(self):
        self.assertEqual(block_to_block_type("######this is a test"), BlockTypes.PARAGRAPH)
    def test_7_hashtag_1_space(self):
        self.assertEqual(block_to_block_type("####### this is a test"), BlockTypes.PARAGRAPH)

    # Code tests
    def test_3_backtick_start_3_end(self):
        self.assertEqual(block_to_block_type("```this is a test```"), BlockTypes.CODE)
    def test_3_backtick_start_0_end(self):
        self.assertEqual(block_to_block_type("```this is a test"), BlockTypes.PARAGRAPH)

    # Quote test
    def test_1_greater_than(self):
        self.assertEqual(block_to_block_type(">this is a test"), BlockTypes.QUOTE)

    # Unordered list test
    def test_1_asterisk(self):
        self.assertEqual(block_to_block_type("* this is a test"), BlockTypes.UNORDERED_LIST)
    def test_1_asterisk(self):
        self.assertEqual(block_to_block_type("-> this is a test"), BlockTypes.UNORDERED_LIST)
    
    # Ordered list tests
    def test_1_asterisk(self):
        self.assertEqual(block_to_block_type("4. this is a test"), BlockTypes.ORDERED_LIST)
    def test_1_asterisk(self):
        self.assertEqual(block_to_block_type("44. this is a test"), BlockTypes.PARAGRAPH)
    def test_1_asterisk(self):
        self.assertEqual(block_to_block_type(". this is a test"), BlockTypes.PARAGRAPH)
    def test_1_asterisk(self):
        self.assertEqual(block_to_block_type("4 this is a test"), BlockTypes.PARAGRAPH)
    
    # Paragraph Test
    def test_1_asterisk(self):
        self.assertEqual(block_to_block_type("this is a test"), BlockTypes.PARAGRAPH)
    def test_empty_string(self):
        self.assertEqual(block_to_block_type(""), BlockTypes.PARAGRAPH)

    def test_wrong_arg(self):
        with self.assertRaises(ValueError, msg="Exêcted ValueError"):
            block_to_block_type(456)

    # Boot.dev tests, adjusted for my enum outputs
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockTypes.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockTypes.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockTypes.QUOTE)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), BlockTypes.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockTypes.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockTypes.PARAGRAPH)



if __name__ == "__main__":
    unittest.main()