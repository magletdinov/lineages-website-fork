from pathlib import Path
from argparse import ArgumentParser

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
        #V-TRACE 
        "B.1.1.523": "B.1.1.523 (Omicron)",
        "AT.1": "AT.1",
        "BA.2.10.1": "BA.2.10.1 (Omicron)",
        "BA.4/BA.5": "BA.4/BA.5 (Omicron)",
        "XBB.1.1": "XBB.1.1 (Omicron)",
        "XBB.1.5/XBB.1.9.1": "XBB.1.5/XBB.1.9.1 (Omicron)",
        "EG.5.1": "EG.5.1 (Omicron)",

        "Other": "Other"}


def open_md(strain):
    to_file = [i for i in PHYLO.glob(f"**/lineage_{strain}.md")]
    if len(to_file) == 0:
        #print(f'Линия {strain} неизвестна')
        return 0
    #if len(to_file) != 1:
    #    print(f"Найдено два файла для {strain}")
    with open(to_file[0], 'r') as f:
        md_content = f.read()    
    metadata_dict = {}
    # Проходим по каждой строке и добавляем ее в словарь
    for line in md_content.split('\n')[1:-2]:
        key, value = line.split(': ', 1)
        metadata_dict[key] = value
    return metadata_dict

def find_strain_root(strain):
    metadata_dict = open_md(strain)
    if metadata_dict == 0:
        return strain
    if type(metadata_dict) != dict:
        raise KeyError(f'Линия {strain} неизвестна')
    if "parent" in metadata_dict.keys() and strain not in roots.keys(): 
        res = metadata_dict["parent"]
        return find_strain_root(res)
    else:
        return strain
    
def final_linage_name(name):
    name = name.split(" ")[0]
    res = find_strain_root(name)
    if res in roots:
        res = roots[res]
    else:
        res = roots['Other']
    return res

parser = ArgumentParser()

parser.add_argument("-i", "--input", dest="INPUT", help="Pangolin lineage", required=True)
parser.add_argument("-p", "--phyloDir", dest="PHYLO", help="Path to 'lineages' directory", required=True)
 
args = parser.parse_args()

INPUT = args.INPUT
PHYLO = args.PHYLO

ROOT = Path().cwd()
PHYLO = Path(PHYLO).resolve()

collapsed_name = final_linage_name(INPUT)
print(collapsed_name)