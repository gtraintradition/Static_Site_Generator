from enum import Enum



class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

    HEADING1 = "heading 1"
    HEADING2 = "heading 2"
    HEADING3 = "heading 3"
    HEADING4 = "heading 4"
    HEADING5 = "heading 5"
    HEADING6 = "heading 6"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


class TagType(Enum):
    TEXT = {"tag": "p", "props": None}
    BOLD = {"tag": "b", "props": None}
    ITALIC = {"tag": "i", "props": None}
    CODE = {"tag": "code", "props": None}
    LINK = {"tag": "a", "props": ["href",]}
    IMAGE = {"tag": "img", "props": ["src","alt",]}

    QUOTE = {"tag": "blockquote", "props": None} # will need further processing 
    UNORDERED_LIST = {"tag": "ul", "props": None} # will need further processing for "li" tag
    ORDERED_LIST = {"tag": "ol", "props": None} # will need further processing for "li" tag

    HEADING1 = {"tag": "h1", "props": None}
    HEADING2 = {"tag": "h2", "props": None}
    HEADING3 = {"tag": "h3", "props": None}
    HEADING4 = {"tag": "h4", "props": None}
    HEADING5 = {"tag": "h5", "props": None}
    HEADING6 = {"tag": "h6", "props": None}


class DelimiterType(Enum):
    BOLD = "**"
    ITALIC = "*"
    CODE = "`"
    CODE2 = "```"


class BlockTypes(Enum):
    HEADING = r"#{1,6} " # checked
    CODE = r"\`\`\`" # (.*?)\`\`\`
    QUOTE = r"\>"
    UNORDERED_LIST = r"[\*\-] " 
    ORDERED_LIST = r"\d\. "
    PARAGRAPH = ""

    BOLD = r"\*\*.*?\*\*"
    ITALIC = r"\*.*?\*"
    LINK = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    IMAGE = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
