import re

from textnode import TextNode
from htmlnode import LeafNode, ParentNode
from block_processing import block_to_block_type
from node_processing import *

from generator_enums import TextType, TagType, BlockTypes




def markdown_to_blocks(markdown):
    # Accepts a markdown string, returns a list of block strings
    
    if type(markdown) != str:
        raise ValueError("Only a string is accepted")
    
    block_list = list(filter(lambda split: split != "", markdown.split("\n\n")))
    
    if len(block_list) == 1:
        return [block_list[0].strip()]
    
    stripped_block_list = list(map(lambda block: block.strip(), block_list))

    return stripped_block_list


def markdown_to_html_node(markdown):
    # converts a full markdown document (one string) into a single parent HTMLNode

    if type(markdown) != str:
        raise ValueError("Only a string is accepted")
    
    blocks = markdown_to_blocks(markdown)
    text_nodes = blocks_to_text_nodes(blocks)

    html_nodes = list(map(text_node_to_html_node, text_nodes))

    parent_node = ParentNode("div", html_nodes)

    return parent_node


def blocks_to_text_nodes(block_list):
    # takes a list of blocks, returns a list of text nodes

    if type(block_list) != list:
        raise ValueError("Only a list (of TextNodes) is accepted")

    node_list = list(map(lambda node: TextNode(node, TextType.TEXT), block_list))

    processed_list_bold = split_nodes_delimiter(node_list, "**", TextType.BOLD)
    processed_list_italic = split_nodes_delimiter(processed_list_bold, "*", TextType.ITALIC)
    processed_list_code = split_nodes_delimiter(processed_list_italic, "```", TextType.CODE)
    processed_list_code2 = split_nodes_delimiter(processed_list_code, "`", TextType.CODE)
    processed_list_image = split_nodes_image(processed_list_code2)
    processed_list_link = split_nodes_link(processed_list_image)
    #######
    processed_list_heading = split_nodes_heading(processed_list_link)
    processed_list_quote = split_nodes_quote(processed_list_heading)
    processed_list_unordered = split_nodes_unordered_list(processed_list_quote)
    processed_list_ordered = split_nodes_ordered_list(processed_list_unordered)

    return processed_list_ordered