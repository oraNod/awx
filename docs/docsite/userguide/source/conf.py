import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../', '../'))
from common.source.conf import *

project = u'Automation Controller User Guide'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None
html_title = 'Automation Controller User Guide v%s' % version


# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None
html_short_title = 'Automation Controller User Guide'

htmlhelp_basename = 'AutomationControllerUserGuidedoc'

latex_documents = [
  (master_doc, 'AutomationControllerUserGuide.tex', u'Automation Controller User Guide',
   u'Red Hat, Inc.', 'manual'),
]

man_pages = [
    (master_doc, 'automationcontrolleruserguide', u'Automation Controller User Guide',
     [author], 1)
]

texinfo_documents = [
  (master_doc, 'AutomationControllerUserGuide', u'Automation Controller User Guide',
   author, 'AutomationControllerUserGuide', 'One line description of project.',
   'Miscellaneous'),
]
