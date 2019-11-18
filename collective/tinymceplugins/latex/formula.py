import html
import io

from Products.Five.browser import BrowserView
from plone.memoize.instance import memoize


class RenderLatex(BrowserView):
    @memoize
    def render_image(self, formula, size, pad_inches=0):
        import matplotlib.pyplot as plt
        buf = io.BytesIO()
        fig = plt.figure(figsize=(0.1, 0.1))
        fig.text(0, 0, '${}$'.format(formula), size=size)
        fig.savefig(buf, bbox_inches='tight', pad_inches=pad_inches)

        buf.seek(0)
        self.request.response.setHeader('Content-Type', 'image/png')
        data = buf.read()
        plt.close()
        return data

    def __call__(self):
        try:
            import matplotlib
            matplotlib.rcParams['text.latex.preamble'].append(r'\usepackage{amsmath}')
            matplotlib.use('Agg')  # png

            formula = self.request.get('formula') or self.request.get('f')
            size = self.request.get('size') or self.request.get('s') or 16
            pad_inches = self.request.get('pad_inches') or self.request.get('p') or 0
            if not formula:
                return
            try:
                size = int(size)
            except ValueError:  # invalid int
                size = 16
            try:
                pad_inches = float(pad_inches)
            except ValueError:
                pad_inches = 0

            return self.render_image(formula, size, pad_inches)
        except Exception as e:
            return 'error: {}'.format(html.escape(e).replace('\n', '<br/>'))

    def absolute_url(self):
        """ Appease the plone.outputfilters gods """
        return self.context.absolute_url() + '/@@latex'
