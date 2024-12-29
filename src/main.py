from textnode import *
from htmlnode import *

from textnode_to_htmlnode import *
from inline_markdown import *




def main():

    d1 = {
    "href": "https://www.google.com", 
    "target": "_blank",
    }
    d2 = {
    "href": "https://www.duckduckgo.com", 
    "target": "_green_____",
    }
    lc1 = ["children1", "children2", "children3"]

    parent_node1 = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    text_node_1 = TextNode("alt text", "image", "https://url.org")
    text_node_2 = TextNode("dummy text", "bold", "https://url.org")
    text_node_3 = TextNode("anchor text", "link", "https://url.org")


    dummyHTML1 = HTMLNode("tag name 1", 
                         "html tag value",
                         lc1,
                         d1)
    
    dummyHTML2 = HTMLNode("tag name 1", 
                         "html tag value",
                         lc1,
                         )

    dummyLeafNode1 = LeafNode("p", "This is a paragraph of text.")
    dummyLeafNode2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    dummyLeafNode3 = LeafNode("a", "Click me!", d1)

    parent_node2 = ParentNode(
    "io",
    [
        dummyLeafNode1,
        parent_node1,
        dummyLeafNode3,
        LeafNode("gg", "non text"),
    ],
    d2
    )

    parent_node3 = ParentNode("nc",[],)


    text_node_4 = TextNode("This is text with a `code block` word", TextType.TEXT)
    text_node_5 = TextNode("This is text with a *code block* word", TextType.TEXT)
    text_node_6 = TextNode("This is text with a `code block` word", TextType.TEXT)
    text_node_7 = TextNode("This is text with a **code block** word", TextType.TEXT)


    #######


    node_list = [text_node_4, text_node_5, text_node_6, text_node_7]

    new_nodes1 = split_nodes_delimiter(node_list, "`", TextType.CODE)

    new_nodes2 = split_nodes_delimiter(node_list, "*", TextType.ITALIC)
  
    new_nodes3 = split_nodes_delimiter(node_list, "**", TextType.BOLD)




    print()
    print(new_nodes1)
    print()
    print(new_nodes2)
    print()
    print(new_nodes3)
    """
    print()
    print("-----")
    print("-----")
    print()
    print("Here are nodes1:")
    for obj in new_nodes1:
        print(f"    {obj}")
    print()
    print("Here are nodes2:")
    for obj in new_nodes2:
        print(f"    {obj}")
    print()
    print("Here are nodes3:")
    for obj in new_nodes3:
        print(f"    {obj}")
    """




if __name__ == "__main__":
    main()