import unittest

from block_processing import *




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
    def test_sign_in_every_line(self):
        self.assertEqual(block_to_block_type(">list\n>items\n>items"), BlockTypes.QUOTE)
    def test_not_sign_in_every_line(self):
        self.assertEqual(block_to_block_type(">list\n items\n>items"), BlockTypes.PARAGRAPH)

    # Unordered list test
    def test_1_asterisk(self):
        self.assertEqual(block_to_block_type("* this is a test"), BlockTypes.UNORDERED_LIST)
    def test_1_asterisk(self):
        self.assertEqual(block_to_block_type("-> this is a test"), BlockTypes.UNORDERED_LIST)
    def test_1_asterisk_every_line(self):
        self.assertEqual(block_to_block_type("* list\n* items\n* items"), BlockTypes.UNORDERED_LIST)
    def test_1_minus_every_line(self):
        self.assertEqual(block_to_block_type("- list\n- items\n- items"), BlockTypes.UNORDERED_LIST)
    def test_mixed_every_line(self):
        self.assertEqual(block_to_block_type("* list\n- items\n* items"), BlockTypes.UNORDERED_LIST)
    def test_missing_sign_line_2(self):
        self.assertEqual(block_to_block_type("* list\n items\n* items"), BlockTypes.PARAGRAPH)
    def test_missing_sign_line_1(self):
        self.assertEqual(block_to_block_type(" list\n *items\n items"), BlockTypes.PARAGRAPH)
    
    # Ordered list tests
    def test_1_patern_not_starting_at_1(self):
        self.assertEqual(block_to_block_type("4. this is a test"), BlockTypes.PARAGRAPH)
    def test_1_patern_starting_at_1(self):
        self.assertEqual(block_to_block_type("1. this is a test"), BlockTypes.ORDERED_LIST)
    def test_2_digits(self):
        self.assertEqual(block_to_block_type("11. this is a test"), BlockTypes.PARAGRAPH)
    def test_0_digits(self):
        self.assertEqual(block_to_block_type(". this is a test"), BlockTypes.PARAGRAPH)
    def test_no_dot(self):
        self.assertEqual(block_to_block_type("4 this is a test"), BlockTypes.PARAGRAPH)
    def test_1_pattern_every_line(self):
        self.assertEqual(block_to_block_type("1. list\n2. items\n3. items"), BlockTypes.ORDERED_LIST)
    def test_digits_wrong_order(self):
        self.assertEqual(block_to_block_type("1. list\n4. items\n3. items"), BlockTypes.PARAGRAPH)
    def test_missing_digit_line_2(self):
        self.assertEqual(block_to_block_type("1. list\n. items\n3. items"), BlockTypes.PARAGRAPH)
    
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