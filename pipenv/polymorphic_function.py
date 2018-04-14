class Heading:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<h1>{self.content}</h1>'

class Div:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<div>{self.content}</div>'


dive_one = Div( 'asome special content')
heading = Heading('Some special heading content')
div_two = Div('another special div content')

def html_render(tag_object):
    print(tag_object.render())


html_render(dive_one)
html_render(heading)
html_render(div_two)
