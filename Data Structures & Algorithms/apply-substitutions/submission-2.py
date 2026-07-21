class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        mapping = {}
        for r in replacements:
            mapping[r[0]] = r[1]

        resolved = {}
        for key in mapping:
            if key not in resolved:
                resolved[key] = self.resolve(key, mapping, resolved)
        parts = text.split("%")
        res = []
        for i in range(len(parts)):
            if i%2==0:
                res.append(parts[i])
            else:
                res.append(resolved[parts[i]])
        return "".join(res)

    def resolve(self, key, mapping, resolved):
        if key in resolved:
            return resolved[key]
        val = mapping[key]
        if "%" not in val:
            resolved[key] = val
            return resolved[key]
        parts = val.split("%")
        res = []
        for i in range(len(parts)):
            if i%2==0:
                res.append(parts[i])
            else:
                res.append(self.resolve(parts[i],mapping,resolved))
        resolved[key] = "".join(res)
        return resolved[key]