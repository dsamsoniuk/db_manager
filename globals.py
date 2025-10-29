from typing import Optional
import os, sys

if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.abspath(".")

VIEWS_DIR: Optional[str] = os.path.join(BASE_DIR, "views")
