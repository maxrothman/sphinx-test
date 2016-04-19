from sphinx.writers import html

class NonCodeSmartyPantsHTMLTranslator(html.SmartyPantsHTMLTranslator):
  '''
  Makes desc_name nodes render as <span> instead of <code> tags

  The default Sphinx behavior is to output the names of all domain objects
  inside <code> tags (from writers/html.py@HTMLTranslator). Since we are not
  documenting code, <span> tags are a better choice.

  This subclasses SmartyPantsHTMLTranslator so as to also include the
  SmartyPants functionality (--- em-dash, etc.)
  '''
  def visit_desc_name(self, node):
    self.body.append(self.starttag(node, 'span', '', CLASS='descname'))

  def depart_desc_name(self, node):
    self.body.append('</span>')