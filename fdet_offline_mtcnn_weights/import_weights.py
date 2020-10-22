from functools import partial
from torch import torch
from pathlib import Path, PurePath

base_url = Path('weights/').resolve()

def load_partial(mtcnn_type):

    if mtcnn_type == 'onet':
        url_path = 'mtcnn_onet.pt'
    if mtcnn_type == 'pnet':
        url_path = 'mtcnn_pnet.pt'
    if mtcnn_type == 'rnet':
        url_path = 'mtcnn_rnet.pt'
    else:
        print(f'mtcnn_type is not recognized: {mtcnn_type}')

    url = str(PurePath(base_url, url_path))

    partial_load = partial(torch.load, url)

    return partial_load


    

