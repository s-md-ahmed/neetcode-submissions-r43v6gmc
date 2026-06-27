class Solution:
    '''
    The star ("*") actually doesn't always stay in the middle! It moves through every single position of the word because of how the loop and slicing work.

Let's look at the exact line doing the magic:

Python



pattern = word[:j] + "*" + word[j+1:]

The variable j loops through every index from 0 to the end of the word (range(len(word))).

Step-by-Step Breakdown with "cat"

If word = "cat", its length is 3, so j will take the values 0, 1, and 2. Here is how the slicing dynamically shifts the star's position:

1. When j = 0 (Star at the beginning)

word[:0] grabs everything before index 0  "" (empty string).

word[1:] grabs everything after index 0  "at".

pattern = "" + "*" + "at"  "*at"

2. When j = 1 (Star in the middle)

word[:1] grabs everything before index 1  "c".

word[2:] grabs everything after index 1  "t".

pattern = "c" + "*" + "t"   "c*t"

3. When j = 2 (Star at the end)

word[:2] grabs everything before index 2 "ca".

word[3:] grabs everything after index 2  "" (empty string).

pattern = "ca" + "*" + "" "ca*"
    '''
    def ladderLength(self,beginWord:str, endWord:str, wordList: List[str])-> int:
        if endWord not in wordList:
            return 0
        nei=collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)
        visited=set([beginWord])
        q=deque([beginWord])
        res=1
        while q:
            for i in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return res
                for j in range(len(word)):
                    pattern=word[:j]+"*"+word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)
            res+=1


        return 0

    