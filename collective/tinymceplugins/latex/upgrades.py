import plone.api
from Products.CMFPlone.interfaces import INonInstallable
from bs4 import BeautifulSoup
from plone.app.textfield import RichTextValue
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'collective.tinymceplugins.latex:uninstall',
        ]


def uninstall(context):
    buttons = plone.api.portal.get_registry_record('plone.custom_buttons')
    buttons = [b for b in buttons if b != 'latex']
    plone.api.portal.set_registry_record('plone.custom_buttons', buttons)

    plugins = plone.api.portal.get_registry_record('plone.custom_plugins')
    plugins = [p for p in plugins if not p.startswith('latex|')]
    plone.api.portal.set_registry_record('plone.custom_plugins', plugins)


def upgrade_3(context):
    pages = plone.api.portal.get_tool('portal_catalog')(portal_type='Document')
    for page in pages:
        changed = False
        page = page.getObject()
        if page.text:
            soup = BeautifulSoup(page.text.raw, 'html.parser')
            for elem in soup.find_all('img'):
                src = elem.attrs.get('src')
                if '@@latex' in src:
                    elem.attrs['data-mce-object'] = 'latex'
                    changed = True
            if changed:
                page.text = RichTextValue(str(soup), mimeType=page.text.mimeType,
                                          outputMimeType=page.text.outputMimeType)
