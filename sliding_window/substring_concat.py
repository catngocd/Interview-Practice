import copy
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) < 1:
            return []
        window_size = len(words[0])
        num_words = len(words)
        s_len = len(s)

        
        if s_len < num_words * window_size:
            return []
        
        table = dict()
        
        for word in words:
            if word in table:
                table[word] += 1
            else:
                table[word] = 1
                
        reference = copy.deepcopy(table)
        ans = []
        table_size = len(table.keys())

        
        for i in range(window_size):
            begin, end = i, i
            table = copy.deepcopy(reference)
            counter = table_size
            
        
            while end + window_size - 1 < s_len:
                cur_word = s[end:end + window_size]


                if cur_word in table:
                    table[cur_word] -= 1

                    if table[cur_word] == 0:
                        counter -= 1
                if end + window_size - begin == window_size * num_words:
                    if counter == 0:
                        ans.append(begin)

                    begin_word = s[begin:begin+window_size]

                    if begin_word in table:
                        table[begin_word] += 1

                        if table[begin_word] > 0:
                            counter += 1
                    begin += window_size
                
                end += window_size
                
            
                        
        return ans
