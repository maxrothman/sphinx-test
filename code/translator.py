from sphinx.writers import html

class NonCodeSmartyPantsHTMLTranslator(html.SmartyPantsHTMLTranslator):
  def visit_desc_name(self, node):
    self.body.append(self.starttag(node, 'span', '', CLASS='descname'))

  def depart_desc_name(self, node):
    self.body.append('</span>')