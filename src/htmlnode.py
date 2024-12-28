

class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        # returns a string representation of the object
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        # overridden by class children
        raise NotImplementedError
    
    def props_to_html(self):
        # returns a string that represents the HTML attributes of the node
        to_join = map(lambda k: f" {k}=\"{self.props[k]}\"", self.props)
        return "".join(to_join)
    

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__()
        self.tag = tag
        self.value = value
        self.props = props
        
    def to_html(self):
        # renders a leaf node as an HTML string
        if self.value == None:
            raise Exception("All leaf nodes must have a value.")
        if self.tag == None:
            return self.value
        if self.props == None:
            rendered = f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            rendered = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        return rendered