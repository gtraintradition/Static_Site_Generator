import re

from htmlnode import HTMLNode
from block_processing import block_to_block_type

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

    html_nodes = list(map(block_to_html_node, blocks))


    parent_node = HTMLNode()

    return parent_node



def block_to_html_node(block):

    block_type = block_to_block_type(block)

    html_node_tag_props = block_to_html_tag_props(block_type)
    html_node_value = block_to_value(block, block_type)
    #html_node_props = block_to_props(block_type)

    html_node = HTMLNode(html_node_tag_props["tag"], html_node_value, None, html_node_tag_props["props"])

    return html_node



def block_to_html_tag_props(block_type):
    if block_type not in BlockTypes:
       raise ValueError("\"block_type\" not recognised: either wrong type, or not supported in enum file")
    
    tag_type = block_type_to_tag_type(block_type)
    
    return tag_type.value
    

def block_to_value(block, block_type):

    text = re.sub(block_type.value, "", block, 1)

    return text


#def block_to_props(block_type):
    #return



def block_type_to_tag_type(block_type):

        if block_type not in BlockTypes:
            raise ValueError("\"block_type\" not recognised: either wrong type, or not supported in enum file")

        match block_type:
                case BlockTypes.HEADING:
                    return TagType.HEADING
                case BlockTypes.CODE:
                    return TagType.CODE
                case BlockTypes.QUOTE:
                    return TagType.QUOTE
                case BlockTypes.UNORDERED_LIST:
                    return TagType.UNORDERED_LIST
                case BlockTypes.ORDERED_LIST:
                    return TagType.ORDERED_LIST
                case BlockTypes.PARAGRAPH:
                    return TagType.TEXT

        raise Exception("Couldn't find a match for \"block_type\", make sure \"block_type\" is supported by the function, and in enum file")


#### might not need the following
def block_type_to_text_type(block_type):

        if block_type not in BlockTypes:
            raise ValueError("\"block_type\" not recognised: either wrong type, or not supported in enum file")

        match block_type:
                case BlockTypes.HEADING:
                    return TagType.HEADING
                case BlockTypes.CODE:
                    return TagType.CODE
                case BlockTypes.QUOTE:
                    return TagType.QUOTE
                case BlockTypes.UNORDERED_LIST:
                    return TagType.UNORDERED_LIST
                case BlockTypes.ORDERED_LIST:
                    return TagType.ORDERED_LIST
                case BlockTypes.PARAGRAPH:
                    return TextType.TEXT

        raise Exception("Couldn't find a match for \"block_type\", make sure \"block_type\" is supported by the function, and in enum file")
