from Products.CMFCore.DirectoryView import registerDirectory
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('collective.tinymceplugins.latex')

registerDirectory('skins', globals())