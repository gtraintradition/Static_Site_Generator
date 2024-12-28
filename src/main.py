from textnode import *
from htmlnode import *



d1 = {
    "href": "https://www.google.com", 
    "target": "_blank",
}
lc1 = ["children1", "children2", "children3"]



def main():

    dummy = TextNode("dummy text", "italic", "https://url.org")

    print(dummy)

    print()

    dummyHTML = HTMLNode("tag name 1", 
                         "html tag value",
                         lc1,
                         d1)

    print(dummyHTML.to_html())
    print()
    print(dummyHTML.props_to_html())

if __name__ == "__main__":
    main()