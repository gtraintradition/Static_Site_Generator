




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
        raise NotImplementedError
    
    def props_to_html(self):
        # returns a string that represents the HTML attributes of the node
        to_join = map(lambda k: f" {k}=\"{self.props[k]}\"", self.props)
        return "".join(to_join)