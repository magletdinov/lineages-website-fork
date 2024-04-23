from pathlib import Path
from argparse import ArgumentParser
from modules import open_md, find_strain_root, final_linage_name
import json

with open('roots.json') as f:
    roots = json.load(f)

parser = ArgumentParser()

parser.add_argument("-i", "--input", dest="INPUT", help="Pangolin lineage", required=True)
#parser.add_argument("-p", "--phyloDir", dest="PHYLO", help="Path to 'lineages' directory", required=True)
 
args = parser.parse_args()

INPUT = args.INPUT
#PHYLO = args.PHYLO
ROOT = Path().cwd()
PHYLO = Path("../lineages").resolve()

collapsed_name = final_linage_name(INPUT, PHYLO, roots)
print(collapsed_name)