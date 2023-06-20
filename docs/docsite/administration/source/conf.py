import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../', '../'))
from common.source.conf import *

project = u'Automation Controller Administration Guide'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None
html_title = 'Automation Controller Administration Guide v%s' % version

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None
html_short_title = 'Automation Controller Administration Guide'

htmlhelp_basename = 'AutomationControllerAdministrationGuidedoc'

latex_documents = [
  (master_doc, 'AutomationControllerAdministrationGuide.tex', u'Automation Controller Administration Guide',
   u'Red Hat, Inc.', 'manual'),
]

man_pages = [
    (master_doc, 'automationcontrolleradministrationguide', u'Automation Controller Administration Guide',
     [author], 1)
]

texinfo_documents = [
  (master_doc, 'AutomationControllerAdministrationGuide', u'Automation Controller Administration Guide',
   author, 'AutomationControllerAdministrationGuide', 'One line description of project.',
   'Miscellaneous'),
]
