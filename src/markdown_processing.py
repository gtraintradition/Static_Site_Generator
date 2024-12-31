import re

from htmlnode import LeafNode, ParentNode
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
            case BlockTypes.PARAGRAPH:
                return TagType.TEXT.value

    raise Exception(f"Coudn't find a match for \"{block}\" and \"{block_type}\"")



def block_to_value(block, block_type):


    match block_type:
        case BlockTypes.PARAGRAPH:     
            return block

    match block_type:
         case BlockTypes.CODE:
            text = block.strip("```")
            return text
         
    match block_type:
        case BlockTypes.HEADING:
            text = re.sub(block_type.value, "", block, 1)
            return text
         
    match block_type:
        case BlockTypes.QUOTE:     
            return block
         
    match block_type:
        case BlockTypes.UNORDERED_LIST:     
            lines = block.split("\n")
            tagged_lines = list(map(lambda line: f"<li>{line[2:]}<li>", lines))
            joined_lines =  "\n".join(tagged_lines)
            return joined_lines
         
    match block_type:
        case BlockTypes.ORDERED_LIST:
            lines = block.split("\n")
            tagged_lines = list(map(lambda line: f"<li>{line[3:]}<li>", lines))
            joined_lines =  "\n".join(tagged_lines)
            return joined_lines


    text = re.sub(block_type.value, "", block, 1)

    return text


#def block_to_props(block_type):
    #return


#### might not need the following
def block_type_to_tag_type(block, block_type):    
    if block_type not in BlockTypes:
        raise ValueError("\"block_type\" not recognised: either wrong type, or not supported in enum file")
    return


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
