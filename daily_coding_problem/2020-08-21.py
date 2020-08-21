"""
Write an algorithm to justify text. Given a sequence of words and an integer line length k, 
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be 
at least one space between each word. Pad extra spaces when necessary so that each line has 
exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, 
if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words 
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] 
and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
 "fox  jumps  over", # 2 extra spaces distributed evenly
 "the   lazy   dog"] # 4 extra spaces distributed evenly
"""

def justify(words, k):

    lines = []
    istart = 0
    while istart < len(words):
        iend = istart
        totlen = -1
        while iend < len(words) and totlen <= k:
            totlen += 1 + len(words[iend])
            iend += 1

        if totlen > k:
            # we've exceeded line length, so back up one word
            totlen -= 1 + len(words[iend-1])
            iend -= 1

        if iend == istart:
            raise Exception("Word {0} is longer than allowed line length {1}".format(words[istart], k))

        if iend == istart+1:
            # the case with only a single word
            line = words[istart] + ' '*(k-len(words[istart]))
        else:
            gaps = [1] * (iend-istart-1)
            i = 0
            for j in range(k - totlen):
                gaps[i] += 1
                i = (i+1)%(len(gaps))
                
            line = words[istart]
            for gaplength, word in zip(gaps, words[istart+1:iend]):
                line += ' '*gaplength + word

        lines.append(line)
        istart = iend

    return lines
        


    
if __name__ == "__main__":
    # for line in justify(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16):
    for line in justify(["the", "quick", "brown", "fox", "jumps", "over", "01234567890123", "the", "lazy", "dog", "aaaaaaaaaaaaaaaa"], 16):
        print(line.__repr__())

