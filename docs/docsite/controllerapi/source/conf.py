import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../', '../'))
sys.path.insert(0, os.path.abspath('./_swagger'))
from common.source.conf import *

extensions += ['swagger']

project = u'Automation Controller API Guide'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None
html_title = 'Automation Controller API Guide v%s' % version


# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None
html_short_title = 'Automation Controller API Guide'

htmlhelp_basename = 'AutomationControllerAPIGuidedoc'

latex_documents = [
  (master_doc, 'AutomationControllerAPIGuide.tex', u'Automation Controller API Guide',
   u'Red Hat, Inc.', 'manual'),
]

man_pages = [
    (master_doc, 'automationcontrollerapiguide', u'Automation Controller API Guide',
     [author], 1)
]

texinfo_documents = [
  (master_doc, 'AutomationControllerAPIGuide', u'Automation Controller API Guide',
   author, 'AutomationControllerAPIGuide', 'One line description of project.',
   'Miscellaneous'),
]
