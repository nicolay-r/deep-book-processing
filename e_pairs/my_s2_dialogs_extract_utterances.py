import os
from utils_my import MyAPI

# Using a side project `gutenberg-dialog` for utterances extraction.

# Origin.
cmd = "python3 -m gutenberg_dialog.main -l=en -f1 -e -f2 -dir {books_dir}".format(
    books_dir=MyAPI.books_storage)

os.system(cmd)