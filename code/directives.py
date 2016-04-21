from docutils.parsers.rst import Directive
from docutils import nodes
from sphinx import addnodes

class TestDirective(Directive):
  has_content = False

  def run(self):
    #no good
    # node = nodes.paragraph('', 'Hi there!',
    #   ids=['foo'],
    #   names = ['foobar']
    # )

    #works
    # node = nodes.section(names=['foobar'])
    # self.state.document.note_explicit_target(node)
    # node.append(nodes.paragraph('', "foo foo"))
    
    #no good
    # node = nodes.admonition(names=['foobar'])
    # self.state.document.note_explicit_target(node)
    # node.append(nodes.paragraph('', "foo foo"))

    # node = nodes.paragraph('', 'foo foo', names=['foobar'])
    # self.state.document.note_explicit_target(node)

    #This doesn't properly render
    desc = addnodes.desc('',
      addnodes.desc_signature('',
        addnodes.desc_name('', 'namename'),
        addnodes.desc_parameterlist('',
          addnodes.desc_parameter('', 'def')
        ),
      names=['namename'], fullname="namename", ids=['namename'], module=None, first=False),
    desctype="function", domain="py", objtype='objtype')
    
    #no link (because didn't properly render?)
    self.state.document.note_explicit_target(desc)
    return [desc]

def setup(app):
  app.add_directive('testing', TestDirective)
  return {'version': '0.1'}


"""
    <desc ids="id1" objtype="objtype">
      <desc_signature names="namename">&lt;desc_name&gt;namename&lt;/desc_name&gt;</desc_signature>
      <desc_content>
        <paragraph/>
      </desc_content>
    </desc>

    <desc desctype="function" domain="py" noindex="False" objtype="function">
      <desc_signature class="" first="False" fullname="abc" ids="abc" module="None" names="abc">
        <desc_name>abc</desc_name>
        <desc_parameterlist>
          <desc_parameter>def</desc_parameter>
        </desc_parameterlist>
      </desc_signature>
      <desc_content/>
    </desc>




"""