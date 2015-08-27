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

      fig = plt.figure(figsize=(3,3))

      buf = io.BytesIO()
      def save(buf):
        fig.savefig(buf,bbox_inches='tight',pad_inches=0)

      fig.text(0, 0, '$%s$' % formula)
      save(buf); del buf # render once so we can get size
      buf = io.BytesIO()
      txtw = fig.texts[0].get_window_extent()
      fig.set_figheight((txtw.y1-txtw.y0)/fig.get_dpi())
      fig.set_figwidth((txtw.x1-txtw.x0)/fig.get_dpi())
      save(buf)

      buf.seek(0)
      self.request.response.setHeader('Content-Type','image/png')
      return buf.read()