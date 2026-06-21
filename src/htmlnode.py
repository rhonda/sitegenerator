class HTMLNode:
    def __init__(
            self,
            tag: str | None = None,
            value: str | None = None,
            children: list["HTMLNode"] | None = None,
            props: dict | None = None
            ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props == None:
            return ""

        all_props = ""
        for prop in self.props:
            all_props += f' {prop}="{self.props[prop]}"'
        return all_props

    def __repr__(self) -> str:
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"



class LeafNode(HTMLNode):
    def __init__(
            self,
            tag: str | None,
            value: str,
            props: dict | None = None
            ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value == None:
            raise ValueError("LeafNode requires a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode(tag: {self.tag}, value: {self.value}, props: {self.props})"



class ParentNode(HTMLNode):
    def __init__(
            self,
            tag: str,
            children: list["HTMLNode"],
            props: dict | None = None
            ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag == None:
            raise ValueError("ParentNode requires a tag")
        if self.children == None:
            raise ValueError("ParentNode requires children")

        result = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            result += child.to_html()
        result += f"</{self.tag}>"

        return result

    def __repr__(self) -> str:
        return f"ParentNode(tag: {self.tag}, children: {self.children}, props: {self.props})"
