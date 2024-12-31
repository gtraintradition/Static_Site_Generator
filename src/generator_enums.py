from enum import Enum



class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TagType(Enum):
    TEXT = {"tag": None, "props": None}
    BOLD = {"tag": "b", "props": None}
    ITALIC = {"tag": "i", "props": None}
    CODE = {"tag": "code", "props": None}
    LINK = {"tag": "a", "props": ["href",]}
    IMAGE = {"tag": "img", "props": ["src","alt",]}

    HEADING = {"tag": ["h1", "h2", "h3", "h4", "h5", "h6"], "props": None}
    QUOTE = {"tag": "blockquote", "props": None}
    UNORDERED_LIST = {"tag": "ul", "props": None}
    ORDERED_LIST = {"tag": "ol", "props": None} # will need further processing for "li" tag


class DelimiterType(Enum):
    BOLD = "**"
    ITALIC = "*"
    CODE = "`"


class BlockTypes(Enum):
    HEADING = r"#{1,6} " # checked
    CODE = r"\`\`\`" # (.*?)\`\`\`
    QUOTE = r"\>"
    UNORDERED_LIST = r"[\*\-] " 
    ORDERED_LIST = r"\d\. "
    PARAGRAPH = ""

