

class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def __repr__(self):
        # returns a string with class name and variables
        final = list(map(str, vars(self).values()))
        return f"{self.__class__.__name__}({", ".join(final)})"

        

    def to_html(self):
        # overridden by class children
        raise NotImplementedError
    

    def props_to_html(self):
        # returns a string that represents the HTML attributes of the node
        if self.props == None:
            return ""
        to_join = map(lambda k: f" {k}=\"{self.props[k]}\"", self.props)
        return "".join(to_join)
    


class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        HTMLNode().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value
        self.props = props


    def to_html(self):
        # renders a leaf node as an HTML string
        if self.value == None:
            raise Exception("LeafNode value can't be \"None\".")
        if self.tag == None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


    


class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        HTMLNode().__init__(tag, None, children, props)
        self.tag = tag
        self.children = children
        self.props = props


    def to_html(self):
        if self.tag == None:
            raise ValueError("\"tag\" value can't be \"None\"")
        if self.children == None:
            raise ValueError("\"children\" value can't be \"None\"")    

        if len(self.children) > 0:
            processed_lines = map(lambda child: child.to_html(), self.children)
        
        if self.children == []:
            processed_lines = [""]

        joined_lines = "".join(processed_lines)

        return f"<{self.tag}{self.props_to_html()}>{joined_lines}</{self.tag}>"
        

        

 