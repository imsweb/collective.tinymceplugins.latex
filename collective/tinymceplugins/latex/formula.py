from Products.Five.browser import BrowserView
import cgi


class RenderLatex(BrowserView):
    def __call__(self):
        try:
            import matplotlib
            import io
            matplotlib.rcParams['text.latex.preamble'].append(r'\usepackage{amsmath}')
            matplotlib.use('Agg')  # png
            import matplotlib.pyplot as plt

            formula = self.request.get('formula') or self.request.get('f')
            size = self.request.get('size') or self.request.get('s') or 16
            if not formula:
                return
            try:
                size = int(size)
            except ValueError:  # invalid int
                size = 16

            buf = io.BytesIO()
            fig = plt.figure(figsize=(0.1, 0.1))
            fig.text(0, 0, '$%s$' % formula, size=size)
            fig.savefig(buf, bbox_inches='tight', pad_inches=0)

            buf.seek(0)
            self.request.response.setHeader('Content-Type', 'image/png')
            data = buf.read()
            plt.close()
            return data
        except Exception, e:
            return 'error: %s' % cgi.escape(e.message).replace('\n', '<br/>')

    def absolute_url(self):
        """ Appease the plone.outputfilters gods """
        return self.context.absolute_url() + '/@@latex'
