from os import listdir
from pathlib import Path

path_parent = Path('./app/models')


for module in listdir(path_parent):
    if 'model' in module:
        __import__(
            f'app.models.{module[:-3]}',
            locals(),
            globals()
        )
