
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../', '../'))
from common.source.conf import *

project = u'Ansible Automation Platform Upgrade and Migration Guide'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None
html_title = 'Ansible Automation Platform Upgrade and Migration Guide'


# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None
html_short_title = 'Automation Platform Upgrade and Migration Guide'

htmlhelp_basename = 'AnsibleAutomationPlatform4UpgradeandMigrationGuidedoc'

latex_documents = [
  (master_doc, 'AnsibleAutomationPlatform4UpgradeandMigrationGuide.tex', u'Ansible Automation Platform Upgrade and Migration',
   u'Red Hat, Inc.', 'manual'),
]

man_pages = [
    (master_doc, 'ansibleautomationplatform4upgradeandmigrationguide', u'Ansible Automation Platform Upgrade and Migration Guide',
     [author], 1)
]

texinfo_documents = [
  (master_doc, 'AnsibleAutomationPlatform4UpgradeandMigrationGuide', u'Ansible Automation Platform Upgrade and Migration Guide',
   author, 'AnsibleAutomationPlatform4UpgradeandMigrationGuide', 'One line description of project.',
   'Miscellaneous'),
]
