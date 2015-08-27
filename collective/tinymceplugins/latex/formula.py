from Products.Five.browser import BrowserView

class RenderLatex(BrowserView):
    def __call__(self):
      try:
        import matplotlib, io
        matplotlib.use('Agg') # png
        import matplotlib.pyplot as plt
      except:
        return None

      formula = self.request.get('formula') or self.request.get('f')

      buf = io.BytesIO()
      fig = plt.figure(figsize=(0.1,0.1))
      fig.text(0, 0, '$%s$' % formula, size=20)
      fig.savefig(buf,bbox_inches='tight',pad_inches=0)

      buf.seek(0)
      self.request.response.setHeader('Content-Type','image/png')
      return buf.read()

    def absolute_url(self):
      """ Appease the plone.outputfilters gods """
      return self.context.absolute_url()+'/@@latex'