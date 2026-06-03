class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_aschii_list(s: str) -> str:
            ascii_list = []
            for char in s:
                ascii_list.append(str(ord(char)))

            ascii_list.sort()
            code = ",".join(ascii_list)
            return code
        
        groups = []
        done = []
        for idx1, str1 in enumerate(strs):
            curr_str_ascii = get_aschii_list(str1)
            if curr_str_ascii in done:
                continue

            group = []
            for idx2, str2 in enumerate(strs):
                if curr_str_ascii == get_aschii_list(str2):
                    group.append(str2)

            if len(group) > 0:
                groups.append(group)
                done.append(curr_str_ascii)
        return groups



        