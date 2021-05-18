class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dict_Content2Files = defaultdict(list)
        
        for path in paths:
            path_info = path.split()
            url = path_info[0]
            
            for f in path_info[1:]:
                content_index = f.index("(")
                dict_Content2Files[f[content_index+1:-1]].append(url+"/"+f[:content_index])
        
        res = []
        for key,val in dict_Content2Files.items():
            if len(val) >= 2:
                res.append(val)
        return res
