"""
Implement an autocomplete system. That is, given a query string s and a set of all 
possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], 
return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient 
data structure to speed up queries.
"""

class AutoComplete:
    def __init__(self, dictionary):
        self.dictionary = sorted(dictionary)

    def get_first_index(self, prefix, include_startswith=True):
        """return index of first string in dictionary starting with prefix"""
    
        def comp(a, b):
            if include_startswith:
                return b >= a
            else:
                return b > a and not b.startswith(a)

        left, right = 0, len(self.dictionary) - 1
        while right > left+1:
            idx = (left + right) // 2
            if comp(prefix, self.dictionary[idx]):
                right = idx
            else:
                left = idx

        if not include_startswith:
            left, right = right, left

        if self.dictionary[left].startswith(prefix):
            return left
        if self.dictionary[right].startswith(prefix):
            return right
        return None

    def complete(self, prefix):
        """return a list of all strings that start with prefix"""

        idx1 = self.get_first_index(prefix, include_startswith=True)
        idx2 = self.get_first_index(prefix, include_startswith=False)
        print(idx1,idx2)

        if idx1 is None or idx2 is None:
            return []
        return self.dictionary[idx1:idx2+1]

if __name__ == "__main__":
    ac = AutoComplete(['car','dog', 'deer', 'deal'])
    print(ac.dictionary)
    print(ac.complete('d'))



