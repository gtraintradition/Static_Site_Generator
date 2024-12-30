from htmlnode import LeafNode
from textnode import TextNode

from text_enums import *




def text_node_to_html_node(text_node):

    def process_list_to_dict(props_list):
        if len(props_list) > 1:
            return {props_list[0]: ""} | process_list_to_dict(props_list[1:])
        return {props_list[0]: ""}

    if not isinstance(text_node, TextNode):
        raise ValueError("Argument passed is not a TextNode")
    
    if text_node.text_type not in TextType:
        raise Exception(f"text_type: \"{text_node.text_type}\" not recognized")
    
    for tag in TagType:
        if text_node.text_type.name == tag.name:
            leaf_tag = tag.value['tag']
            props = tag.value['props']

    if props == None:
        new_LeafNode = LeafNode(leaf_tag, text_node.text, props)
        return new_LeafNode

    if props != None and props != []:
        leaf_props = process_list_to_dict(props)
        for prop in leaf_props.keys():
            match prop:
                case "href":
                    leaf_props["href"] = text_node.url
                case "src":
                    leaf_props["src"] = text_node.url
                case "alt":
                    leaf_props["alt"] = text_node.text
        
        leaf_text = text_node.text
        if text_node.text_type == TextType.IMAGE:
            leaf_text = ""
        new_LeafNode = LeafNode(leaf_tag, leaf_text, leaf_props)
        return new_LeafNode
    

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # old_nodes is a list of TextNodes, 
    # delimiter, text_type are strings (?)


    def process_node(node, delimiter, text_type):
    # node is a TextNode object, of TextType.TEXT only

        if type(node) != TextNode:
            raise Exception(f"Can only process TextNode objects")

        if node.text_type not in TextType or delimiter not in node.text:
            return [node]
        
        if delimiter == "*" and "**" in node.text:
            return [node]

        splitted_node = node.text.split(delimiter)

        if len(splitted_node) <= 1:
            return splitted_node

        # after thinking about it, it could be a choice of the user to use an odd number of delimiters
        # to check if the number of delimiters present in the node is even (we must have an odd number of splits),
        # if not it means there is too much or not enough delimiters. The markdown is invalid
        if len(splitted_node) % 2 == 0:
            raise Exception(f"Number of delimiters must be an even number/section must be closed for the markdown to be valid.")

        result = []
        for i in range(len(splitted_node)):
            if splitted_node[i] == "":
                continue
            if i % 2 == 0:
                result.append(TextNode(splitted_node[i], TextType.TEXT))
            else:
                result.append(TextNode(splitted_node[i], text_type))

        return result


    if type(old_nodes) != list:
        raise Exception("\"old_nodes\" (arg 1) needs to be a list of TextNodes.")
    if old_nodes == []:
        raise Exception("\"old_nodes\" (arg 1) can't be empty.")
    if delimiter not in DelimiterType:
        raise ValueError("\"Delimiter\" not recognized, only the following delimiters are accepted: \"**\", \"*\", \"`\".")

    splitted_nodes = map(lambda node: (process_node(node, delimiter, text_type)) , old_nodes)

    final = []
    for node in splitted_nodes:
        final.extend(node)

    return final




def split_nodes_image(old_nodes):
    # takes a list of nodes, returns a list of nodes

    pass




def split_nodes_link(old_nodes):
    pass
