import re

from text_enums import *

from textnode import TextNode




def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # old_nodes is a list, 
    # delimiter, text_type are strings (?)

    if delimiter not in DelimiterType:
        raise ValueError("\"Delimiter\" not recognized, only the following delimiters are accepted: \"**\", \"*\", \"`\".")

    splitted_nodes = map(lambda node: (process_node(node, delimiter, text_type)) , old_nodes)

    final = []
    for node in splitted_nodes:
        final.extend(node)

    return final


def process_node(node, delimiter, text_type):
    # node is a TextNode object, of TextType.TEXT only

    if node.text_type not in TextType or delimiter not in node.text:
        return [node]
    
    if delimiter == "*" and "**" in node.text:
        return [node]

    splitted_node = node.text.split(delimiter)

    if len(splitted_node) <= 1:
        return splitted_node

    text_node_1 = TextNode(splitted_node[0], TextType.TEXT)
    text_node_2 = TextNode(splitted_node[1], text_type)
    text_node_3 = TextNode(splitted_node[2], TextType.TEXT)

    result = [text_node_1, text_node_2, text_node_3]

    return result

