#!C:\Users\pmann\Documents\CodingDojo_Python\MyEnvironments\djangoEnv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'complex-dist==0.1','console_scripts','complex-dist2'
__requires__ = 'complex-dist==0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('complex-dist==0.1', 'console_scripts', 'complex-dist2')()
    )
