#!C:\Users\Administrator\PycharmProjects\oxox\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'apistar==0.7.2','console_scripts','apistar'
__requires__ = 'apistar==0.7.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('apistar==0.7.2', 'console_scripts', 'apistar')()
    )
