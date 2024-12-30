import re

from textnode import TextNode

from text_enums import TextType, DelimiterType



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


