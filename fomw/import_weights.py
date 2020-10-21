from functools import partial
from torch import torch
from pathlib import Path, PurePath

base_url = Path('weights').resolve()

def load_partial(url_path):

    url = PurePath(base_url, url_path)

    partial_load = partial(torch.load, url)

    return load_partial


    

