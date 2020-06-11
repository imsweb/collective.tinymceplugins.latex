import collective.tinymceplugins.latex
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.testing import z2


class TinyMceLatexLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.tinymceplugins.latex)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.tinymceplugins.latex:default')


TINYMCE_LATEX_FIXTURE = TinyMceLatexLayer()

TINYMCE_LATEX_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TINYMCE_LATEX_FIXTURE,),
    name='TinyMceLatexLayer:IntegrationTesting',
)

IMS_JAMIS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TINYMCE_LATEX_FIXTURE,),
    name='TinyMceLatexLayer::FunctionalTesting',
)

IMS_JAMIS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        TINYMCE_LATEX_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='TinyMceLatexLayer::AcceptanceTesting',
)
