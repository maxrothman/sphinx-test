from docutils.parsers.rst import Directive
from docutils import nodes

class TestDirective(Directive):
  has_content = True

  def run(self):
    return [nodes.paragraph('', 'Hi there!',
      ids=['foo'],
      names = ['foobar']
    )]

def setup(app):
  app.add_directive('testing', TestDirective)
  return {'version': '0.1'}