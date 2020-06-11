# -*- coding: utf-8 -*-
"""Setup tests for this package."""
import unittest

from plone import api
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from ..testing import TINYMCE_LATEX_INTEGRATION_TESTING

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that this is properly installed."""

    layer = TINYMCE_LATEX_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.tinymceplugins.latex is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.tinymceplugins.latex'))


class TestUninstall(unittest.TestCase):

    layer = TINYMCE_LATEX_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['collective.tinymceplugins.latex'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.tinymceplugins.latex is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.tinymceplugins.latex'))
