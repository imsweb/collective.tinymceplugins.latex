import unittest
import os

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
        self.view = self.portal.restrictedTraverse('@@latex')

    def test_render_image(self):
        img = self.view.render_image('f=ma', 16)
        self.assertIn(b'\x89PNG', img)
        base_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(base_path, 'formula.png'), 'rb') as expected:
            expected = expected.read()
        self.assertEqual(expected, img)
