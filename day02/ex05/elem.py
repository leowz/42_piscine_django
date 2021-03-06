#!/usr/bin/python3

class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        new = super().__str__().replace('>', '&gt;').replace('<', '&lt;')
        if new == '"': 
            new = new.replace('"', '&quot;')
        return new.replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        def __init__(self, msg= "This content is not a Text or a elem."):
            Exception.__init__(self, msg)

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        print(content);
        print(attr);
        print(tag);
        print(tag_type);
        self.tag = tag;
        self.attr = attr;
        self.tag_type = tag_type;
        self.content = [];
        if content:
            self.add_content(content);
        elif content != None and not isinstance(content, Text):
            raise Elem.ValidationError()

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            result = '<{0}{1}>{2}</{0}>'.format(self.tag,
                    self.__make_attr(), self.__make_content());
        elif self.tag_type == 'simple':
            result = '<{0}{1}/>'.format(self.tag, self.__make_attr());
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            result += "  " + str(elem).replace('\n', '\n  ') + "\n";
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    print(Elem(content=Elem(content=Elem(content=Elem(content=Text("some text for test"))))))
