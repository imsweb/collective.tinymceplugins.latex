from Products.Five import BrowserView
from plone.app.theming.utils import getTheme, getCurrentTheme
import plone.api as api


class DialogClass(BrowserView):
    def theme(self):
        _theme = getTheme(getCurrentTheme())
        return api.portal.get().absolute_url() + _theme.production_css
