#!f:\buysellbooks\sell-engineering_books\buyandsell\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'gitignore==0.0.8','console_scripts','gitignore'
__requires__ = 'gitignore==0.0.8'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('gitignore==0.0.8', 'console_scripts', 'gitignore')()
    )
