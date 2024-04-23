def open_md(strain, PHYLO):  # Добавляем PHYLO как аргумент
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

def find_strain_root(strain, PHYLO, roots):  # Добавляем PHYLO и roots как аргументы
    metadata_dict = open_md(strain, PHYLO)  # Передаем PHYLO в open_md
    if metadata_dict == 0:
        return strain
    if type(metadata_dict) != dict:
        raise KeyError(f'Линия {strain} неизвестна')
    if "parent" in metadata_dict.keys() and strain not in roots.keys(): 
        res = metadata_dict["parent"]
        return find_strain_root(res, PHYLO, roots)  # Передаем PHYLO и roots в рекурсивный вызов
    else:
        return strain
    
def final_linage_name(name, PHYLO, roots):  # Добавляем PHYLO и roots как аргументы
    name = name.replace("пред. ", "")
    name = name.split(" ")[0]
    res = find_strain_root(name, PHYLO, roots)  # Передаем PHYLO и roots в find_strain_root
    if res in roots:
        res = roots[res]
    else:
        res = roots['Other']
    return res


def create_roots_add(path_to_lineage_dir):
    root_count = []
    for to_file in path_to_lineage_dir.glob(f"**/lineage*.md"):
        metadata_dict = open_md(strain=to_file.stem.split("lineage_")[1], PHYLO=path_to_lineage_dir)
        if "parent" not in metadata_dict.keys() or len(metadata_dict["parent"]) == 0:
            root_count.append(to_file.stem.split("_")[1])
    roots_add = {i: i+" (Omicron)" for i in root_count}
    return roots_add