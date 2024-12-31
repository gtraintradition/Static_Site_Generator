import re

from textnode import TextNode
from htmlnode import LeafNode, ParentNode
from text_processing import text_to_textnodes
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


    html_nodes = list(map(block_to_leaf_node, blocks))

    #print(html_nodes)



    parent_node = ParentNode("body", html_nodes)

    return parent_node



def block_to_leaf_node(block):

    block_type = block_to_block_type(block)

    html_node_tag_props = block_to_html_tag_props(block, block_type)
    html_node_value = block_to_value(block, block_type)
    

    # handling h
    if html_node_tag_props["tag"] in TagType:
        return LeafNode(html_node_tag_props["tag"], html_node_value, html_node_tag_props["props"])

    # handling ol, ul
    if html_node_tag_props["tag"] == "ol" or html_node_tag_props["tag"] == "ul":
        return LeafNode(html_node_tag_props["tag"], html_node_value, html_node_tag_props["props"])


    return LeafNode(html_node_tag_props["tag"], html_node_value, html_node_tag_props["props"])




def block_to_html_tag_props(block, block_type):
    if block_type not in BlockTypes:
       raise ValueError("\"block_type\" not recognised: either wrong type, or not supported in enum file")

    match block_type:
            case BlockTypes.PARAGRAPH:
                return TagType.TEXT.value
            case BlockTypes.HEADING:
                match = re.match(BlockTypes.HEADING.value, block[0:8])
                if match != None:
                    return {"tag": f"h{len(match[0]) - 1}", "props": None}
            case BlockTypes.CODE:
                return TagType.CODE.value
            case BlockTypes.QUOTE:
                return TagType.QUOTE.value
            case BlockTypes.UNORDERED_LIST:
                return TagType.UNORDERED_LIST.value
            case BlockTypes.ORDERED_LIST:
                return TagType.ORDERED_LIST.value
        
            case BlockTypes.BOLD:
                return TagType.BOLD.value
            case BlockTypes.ITALIC:
                return TagType.ITALIC.value
            case BlockTypes.LINK:
                return TagType.LINK.value
            case BlockTypes.IMAGE:
                return TagType.IMAGE.value


    raise Exception(f"Coudn't find a match for \"{block}\" and \"{block_type}\"")



def block_to_value(block, block_type):


    match block_type:
        case BlockTypes.PARAGRAPH:     
            return block

        case BlockTypes.CODE:
            text = block.strip("```")
            return text
         
        case BlockTypes.HEADING:
            text = re.sub(block_type.value, "", block, 1)
            return text
         
        case BlockTypes.QUOTE:
            lines = block.split("\n")
            tagged_lines = list(map(lambda line: line[1:], lines))
            joined_lines =  "\n".join(tagged_lines)
            return joined_lines
         
        case BlockTypes.UNORDERED_LIST:     
            lines = block.split("\n")
            tagged_lines = list(map(lambda line: f"<li>{line[2:]}<li>", lines))
            joined_lines =  "\n".join(tagged_lines)
            return joined_lines
         
        case BlockTypes.ORDERED_LIST:
            lines = block.split("\n")
            tagged_lines = list(map(lambda line: f"<li>{line[3:]}<li>", lines))
            
            joined_lines =  "\n".join(tagged_lines)
            return joined_lines

        case BlockTypes.BOLD:
            # might want to change that if i want to implement nested markdown support
            return re.findall(r"\*\*(.*?)\*\*", block)[0]
        
        case BlockTypes.ITALIC:
            # might want to change that if i want to implement nested markdown support
            return re.findall(r"\*(.*?)\*", block)[0]
        
        case BlockTypes.LINK:
             # might want to change that if i want to implement nested markdown support
            return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", block)[0]
        
        
        case BlockTypes.IMAGE:
             # might want to change that if i want to implement nested markdown support
            return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", block)[0]
        
        


    text = re.sub(block_type.value, "", block, 1)

    return text



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