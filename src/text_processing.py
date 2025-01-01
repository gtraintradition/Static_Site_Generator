import re

from textnode import TextNode
from node_processing import split_nodes_delimiter, split_nodes_image, split_nodes_link

from generator_enums import TextType, BlockTypes



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

    processed_list_bold = split_nodes_delimiter([text_node], "**", TextType.BOLD)
    processed_list_italic = split_nodes_delimiter(processed_list_bold, "*", TextType.ITALIC)
    processed_list_code = split_nodes_delimiter(processed_list_italic, "`", TextType.CODE)
    processed_list_image = split_nodes_image(processed_list_code)
    processed_list_link = split_nodes_link(processed_list_image)
    #######


    return processed_list_link


def text_to_html(text):

    # bold
    splitted = re.split(r"(\*\*.*?\*\*)", text)
    filtered = []
    for split in splitted:
        if split != "" and split[0:2] == split[-2:] == "**":
            filtered.append("<b>" + split.strip("**") + "</b>")
        else:
            filtered.append(split)
    text = "".join(filtered)

    # italic
    splitted = re.split(r"(\*.*?\*)", text)
    filtered = []
    for split in splitted:
        if split != "" and split[0] == split[-1] == "*":
            filtered.append("<i>" + split.strip("*") + "</i>")
        else:
            filtered.append(split)
    text = "".join(filtered)

    # image
    pattern = r"(!\[[^\[\]]*\]\([^\(\)]*\))"
    splitted = re.split(pattern, text)
    filtered = []
    for split in splitted:
        if split != "" and re.match(pattern, split):
            extracted = extract_markdown_images(split)[0]

            filtered.append(f"<img src=\"{extracted[1]}\" alt=\"{extracted[0]}\">")
        else:
            filtered.append(split)   
    text = "".join(filtered)     

    # link
    pattern = r"((?<!!)\[[^\[\]]*\]\([^\(\)]*\))"
    splitted = re.split(pattern, text)
    filtered = []
    for split in splitted:
        if split != "" and re.match(pattern, split):
            extracted = extract_markdown_links(split)[0]

            filtered.append(f"<a href=\"{extracted[1]}\">{extracted[0]}</a>")
        else:
            filtered.append(split)   
    text = "".join(filtered)     

    # code 3 ticks
    pattern = r"(\`\`\`.*?\`\`\`)"
    splitted = re.split(pattern, text)
    filtered = []
    for split in splitted:
        if split != "" and re.match(pattern, split):
            filtered.append(f"<code>{split.strip("```")}</code>")
        else:
            filtered.append(split)   
    text = "".join(filtered)     

    # code 1 tick
    pattern = r"(\`.*?\`)"
    splitted = re.split(pattern, text)
    filtered = []
    for split in splitted:
        if split != "" and re.match(pattern, split):
            filtered.append(f"<code>{split.strip("`")}</code>")
        else:
            filtered.append(split)   
    text = "".join(filtered)     

    return text

