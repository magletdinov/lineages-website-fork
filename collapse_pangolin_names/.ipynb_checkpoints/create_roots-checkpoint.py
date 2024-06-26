from pathlib import Path
import json
from modules import open_md, create_roots_add

roots = {#Pangolin
        "B": "B",
        "A": "A",
        "B.1": "B.1",
        "B.1.617.2": "B.1.617.2 (Delta)",
        "B.1.621": "B.1.621 (Mu)",
        "B.1.525": "B.1.525 (Eta)",
        "B.1.617.1": "B.1.617.1 (Kappa)",
        "B.1.177": "EU1",
        "B.1.526": "B.1.526 (Iota)",
        "B.1.427": "B.1.427 (Epsilon)",
        "B.1.351": "B.1.351 (Beta)",
        "B.1.2": "B.1.2",
        "B.1.1": "B.1.1",
        "B.1.1.529": "B.1.1.529 (Omicron)",
        "P.3": "P.3 (Theta)",
        "P.1": "P.1 (Gamma)",
        "B.1.1.7": "B.1.1.7 (Alpha)",
        "D.2": "D.2",
        "B.1.1.1": "B.1.1.1",
        "C.37": "C.37 (Lambda)",
        "BA.1": "BA.1 (Omicron)",
        "BA.2": "BA.2 (Omicron)",
        "BA.3": "BA.3 (Omicron)",
        "BA.4": "BA.4 (Omicron)",
        "BA.5": "BA.5 (Omicron)",
        "XBB": "XBB (Omicron)",
        "XBB.1.5": "XBB.1.5 (Omicron)",
        "XBB.1.16": "XBB.1.16 (Omicron)",
        "XBB.1.9.1": "XBB.1.9.1 (Omicron)",
        "XBB.2.3": "XBB.2.3 (Omicron)",
        "BA.2.75": "BA.2.75 (Omicron)",
        "BA.2.12.1": "BA.2.12.1 (Omicron)",
        "BQ.1": "BQ.1 (Omicron)",
        "XBB.2.3": "XBB.2.3 (Omicron)",
        "EG.5": "EG.5 (Omicron)",
        "BA.2.86": "BA.2.86 (Omicron)",
        "JN.1": "JN.1 (Omicron)",
        "EG.5.1": "EG.5.1 (Omicron)",
        "BF.5" : "BF.5 (Omicron)",
        "BF.7" : "BF.7 (Omicron)",
        "CL.1" : "CL.1 (Omicron)",
        #V-TRACE 
        "B.1.1.523": "B.1.1.523 (Omicron)",
        "AT.1": "AT.1",
        "BA.2.10.1": "BA.2.10.1 (Omicron)",
        "BA.4/BA.5": "BA.4/BA.5 (Omicron)",
        "XBB.1.1": "XBB.1.1 (Omicron)",
        "XBB.1.5/XBB.1.9.1": "XBB.1.5/XBB.1.9.1 (Omicron)",

        "Other": "Other"}


PHYLO = (Path().cwd() / ".." / "lineages").resolve()
roots_merge = roots | create_roots_add(path_to_lineage_dir=PHYLO)

path_to_save = Path('roots.json')
with open(path_to_save, 'w') as file:
    json.dump(roots_merge, file)