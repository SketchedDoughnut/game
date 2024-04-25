import shutil
import os

def decide(
    if_full_redo
):
    if if_full_redo:
        print('------------------------------------')
        print("""Files are missing from your installation. This is an issue with the developer.
Please notify them via the feedback form. Your update will be rolled back, and functionality will be
restored.""")
        return