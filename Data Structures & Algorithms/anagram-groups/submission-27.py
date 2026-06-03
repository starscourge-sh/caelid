class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_aschii_list(s: str) -> [List]:
            ascii_list = []
            for char in s:
                ascii_list.append(str(ord(char)))

            ascii_list.sort()
            return ascii_list
        
        groups = []
        done = []
        for _ , str1 in enumerate(strs):
            curr_str_ascii = get_aschii_list(str1)
            if curr_str_ascii in done:
                continue

            group = []
            for _, str2 in enumerate(strs):
                if curr_str_ascii == get_aschii_list(str2):
                    group.append(str2)

            groups.append(group)
            done.append(curr_str_ascii)
        return groups



        