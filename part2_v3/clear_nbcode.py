#!/usr/bin/env python

import json,fire,re
from pathlib import Path

def is_codecell(cell:dict) -> bool:
    '''
        check whether a cell contains codes
    '''
    if cell['cell_type'] == 'code': return True
    return False

def clear_nbcode(fname: str):
    '''
    clearing only the codes in code_cells (inplace) without changing any other parts 
    in the jupyter-notebook, sothat it's easier both to follow up fastai-nbs, 
    and to write everything from scratch as Jeremy advises.
    '''
    fname = Path(fname)
    with open(fname,'r') as nb_json:
        main_dic = json.load(nb_json)
        code_cells = [c for c in main_dic['cells'] if is_codecell(c)]
    
    # clearing the source in code cells
    for cell in code_cells: 
        cell['source'] = '' 
    
#     import pdb; pdb.set_trace()
    with open(fname,'w') as nb_json:
        json.dump(main_dic, nb_json)   
        print(f'Cleared all the code_cells in "{fname}" (leaving other cells unchanged)')
if __name__ == '__main__': fire.Fire(clear_nbcode)

