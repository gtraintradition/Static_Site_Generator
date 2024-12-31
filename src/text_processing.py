import re

from textnode import TextNode
from node_processing import split_nodes_delimiter, split_nodes_image, split_nodes_link

from generator_enums import TextType



def extract_markdown_images(text):
    # takes raw markdown text and returns a list of tuples, each tuple should contain the alt text and the URL of any markdown images

    if not isinstance(text, str):
        raise ValueError("Argument passed must be a string")

    #pattern = r"\!\[(.*?)\]\((.*?://.*?\..*?)\)"     
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    filtered = re.findall(pattern, text)

    return filtered


def extract_markdown_links(text):
    # takes raw markdown text and returns a list of tuples, each tuple should contain the anchor text and the URL

    if not isinstance(text, str):
        raise ValueError("Argument passed must be a string")

    #pattern = r"\[(.*?)\]\((.*?://.*?\..*?)\)"
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    filtered = re.findall(pattern, text)

    return filtered


def text_to_textnodes(text):
    # takes a string, returns a list of TextNodes
    # maybe where to start if i want to add nested markdown handling
    
    if type(text) != str:
        raise ValueError("Only a string is accepted")

    text_node = TextNode(text, TextType.TEXT)

    ######## start





    ######## end
    processed_list_bold = split_nodes_delimiter([text_node], "**", TextType.BOLD)
    processed_list_italic = split_nodes_delimiter(processed_list_bold, "*", TextType.ITALIC)
    processed_list_code = split_nodes_delimiter(processed_list_italic, "`", TextType.CODE)
    processed_list_image = split_nodes_image(processed_list_code)
    processed_list_link = split_nodes_link(processed_list_image)

    return processed_list_link
