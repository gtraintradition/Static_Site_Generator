from textnode import *
from htmlnode import *



d1 = {
    "href": "https://www.google.com", 
    "target": "_blank",
}
lc1 = ["children1", "children2", "children3"]



def main():

    dummy = TextNode("dummy text", "italic", "https://url.org")


    dummyHTML = HTMLNode("tag name 1", 
                         "html tag value",
                         lc1,
                         d1)

    dummyLeafNode1 = LeafNode("p", "This is a paragraph of text.")
    dummyLeafNode2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    dummyLeafNode3 = LeafNode("a", "Click me!", d1)
    
    print(dummyLeafNode1)
    print(dummyLeafNode2)
    print("-----")
    print(dummyLeafNode1.to_html())
    print()
    print(dummyLeafNode2.to_html())
    print()
    print(dummyLeafNode3.to_html())
    print()
    print(dummyLeafNode3)



if __name__ == "__main__":
    main()