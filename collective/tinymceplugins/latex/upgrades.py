from bs4 import BeautifulSoup
import plone.api
from plone.app.textfield import RichTextValue
import six


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
                page.text = RichTextValue(six.text_type(soup), mimeType=page.text.mimeType,
                                          outputMimeType=page.text.outputMimeType)
