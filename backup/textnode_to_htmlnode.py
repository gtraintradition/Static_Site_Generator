from htmlnode import LeafNode
from textnode import TextType, TagType, TextNode

from text_enums import *


def text_node_to_html_node(text_node):
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
    

def process_list_to_dict(props_list):
        if len(props_list) > 1:
            return {props_list[0]: ""} | process_list_to_dict(props_list[1:])
        return {props_list[0]: ""}
