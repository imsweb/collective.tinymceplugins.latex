from Products.Five.browser import BrowserView

class RenderLatexExample(BrowserView):
    def get_image(self):
      try:
        import matplotlib.pyplot as plt
      except:
        return None

      a = '\\frac{a}{b}'  #notice escaped slash
      plt.plot()
      plt.text(0.5, 0.5,'$%s$'%a)
      return plt.show()