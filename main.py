def find_synonym_groups(synonyms):
    groups = []
    visited = set()

    def dfs(synonym):
        if synonym in visited:
            return
        visited.add(synonym)
        group = [synonym]
        for map in synonyms:
            if synonym in map:
                for s in map:
                    if s != synonym:
                        group.append(s)
                        dfs(s)
        groups.append(group)

    for map in synonyms:
        for s in map:
            dfs(s)

    return groups

synonyms = [ {"Dg set": "Diesel generator"},{"Organization": "Organisation"},{"Group": "Organization"},{"Orange": "Kinnu"},{"Orange": "narangi"} ]
print(find_synonym_groups(synonyms))
