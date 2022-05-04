from os import listdir
from pathlib import Path

path_parent = Path('./app/routers')


for module in listdir(path_parent):
    if 'router' in module:
        __import__(
            f'app.routers.{module[:-3]}',
            locals(),
            globals()
        )
