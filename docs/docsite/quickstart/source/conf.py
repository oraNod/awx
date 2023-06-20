
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../', '../'))
from common.source.conf import *

project = u'Ansible Automation Platform Quick Setup'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None
html_title = 'Ansible Automation Platform Quick Setup Guide v%s' % version


# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None
html_short_title = 'Automation Platform Quick Setup Guide'

htmlhelp_basename = 'AnsibleAutomationPlatformQuickSetup'

latex_documents = [
  (master_doc, 'AnsibleAutomationPlatformQuickSetupGuide.tex', u'Ansible Automation Platform Quick Setup Guide',
   u'Red Hat, Inc.', 'manual'),
]

man_pages = [
    (master_doc, 'ansibleautomationplatformquicksetup', u'Ansible Automation Platform Quick Setup Guide',
     [author], 1)
]

texinfo_documents = [
  (master_doc, 'AnsibleAutomationPlatformQuickSetup', u'Ansible Automation Platform Quick Setup Guide ',
   author, 'AnsibleAutomationPlatformDocs', 'One line description of project.',
   'Miscellaneous'),
]