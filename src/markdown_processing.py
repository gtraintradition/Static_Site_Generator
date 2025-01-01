import re

from htmlnode import ParentNode, LeafNode
from text_processing import text_to_textnodes, text_to_html
from node_processing import text_node_to_html_node

from generator_enums import BlockTypes




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

    parent_node = ParentNode("div", html_nodes)

    return parent_node


def block_to_html_node(block):

    #print("-------working on block")
    #print(block)
    #print()


    # Handling Heading
    match = re.match(BlockTypes.HEADING.value, block[0:8])
    if match != None:
        text = re.sub(match[0], "", block)
        text = text_to_html(text)
        return LeafNode(f"h{len(match[0]) - 1}", text)
        

    # Handling Ordered List
    if block[0:3] == "1. ":
        result = handle_ol(block)
        if result != None:
            return result
        

    # Handling Unordered List
    match = re.match(BlockTypes.UNORDERED_LIST.value, block[0:3])
    if match != None:
        result = handle_ul(block)
        if result != None:
            return result
        

    # Handling Quote
    if block[0] == ">":
        result = handle_quote(block)
        if result != None:
            return result
        

    # Handling Code
    if block[0:4] == block[-3:] == "```" or block[0] == block[-1] == "`":
        result = handle_code(block)
        if result != None:
            return result

    # If every check before fail block is considered s paragraph
    # Handling Paragraph
    result = handle_paragraph(block)
    return result


def handle_ol(block):

    lines = block.split("\n")
    children_nodes_list = []
    for i in range(len(lines)):
        if lines[i][0:3] != f"{i + 1}. ":
            return
        line = lines[i][3:]
        line = text_to_html(line)
        textnodes_list = text_to_textnodes(line)

        if len(textnodes_list) == 1:
            children_nodes_list.append(LeafNode("li", line))
        
        else:
            html_node_list = []
            for text_node in textnodes_list:
                htmlnode = text_node_to_html_node(text_node)
                html_node_list.append(htmlnode)
            children_nodes_list.append(ParentNode("li", html_node_list))

    return ParentNode("ol", children_nodes_list)    


def handle_ul(block):

    lines = block.split("\n")
    children_nodes_list = []
    for line in lines:
        if re.match(BlockTypes.UNORDERED_LIST.value, line[0:3]) == None:
            return
        line = line[2:]
        line = text_to_html(line)
        textnodes_list = text_to_textnodes(line)

        if len(textnodes_list) == 1:
            children_nodes_list.append(LeafNode("li", line))
        
        else:
            html_node_list = []
            for text_node in textnodes_list:
                htmlnode = text_node_to_html_node(text_node)
                html_node_list.append(htmlnode)
            children_nodes_list.append(ParentNode("li", html_node_list))

    return ParentNode("ul", children_nodes_list)     


def handle_quote(block):

    lines = block.split("\n")
    new_lines = [] 

    for i in range(len(lines)):
        line = lines[i]
        if line[0] != ">":
            print("breaking")
            return
        line = line[1:]
        line = text_to_html(line)
        #if i != (len(lines) - 1):
            #line += "<br>"
        new_lines.append(line)
        
    return LeafNode("blockquote", "".join(new_lines).strip())     


def handle_code(block):

    block = block.strip("```")
    lines = block.split("\n")
    new_lines = [] 

    for i in range(len(lines)):
        line = lines[i]
        line = text_to_html(line)
        if i != (len(lines) - 1):
            #line += "<br>"
            line += " "
        new_lines.append(line)
        
    return LeafNode("code", "".join(new_lines))     


def handle_paragraph(block):

    lines = block.split("\n")
    new_lines = [] 

    for i in range(len(lines)):
        line = lines[i]
        line = text_to_html(line)
        if i != (len(lines) - 1):
            #line += "<br>"
            line += " "
        new_lines.append(line)
        
    return LeafNode("p", "".join(new_lines))     
