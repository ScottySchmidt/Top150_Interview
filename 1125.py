"""
1255. Maximum Score Words Formed by Letters
HARD Level:  https://leetcode.com/problems/maximum-score-words-formed-by-letters/

Given a list of words, list of  single letters (might be repeating) and score of every character.
Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).
It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.
"""

# My first attempt using a for loop will not recognize if a letter does not have many of the same letter remaining.
# Specifically, the word Dad. This algo below will not have two d's left.
class Solution(object):
    def maxScoreWords(self, words, letters, score):
        abcList=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
        'q', 'r', 's', 't', 'u', 'v',   'w', 'x', 'y', 'z']
        scoreDic=dict(zip(abcList, score))
        totalScore = 0

        newLetters=[]
        for l in letters:
            #print(newLetters.count(l), " count")
            if newLetters.count(l) < 3:
                newLetters.append(l[0])
                #print(newLetters)
        
        newLetters=[str(x) for x in newLetters] #print(newLetters, " new letters", type(newLetters))

        for word in words:
            wordScore = 0
            check = all(let in newLetters for let in word) #print(check, " check")
            if check:
                print(word)
                for w in word:
                    if w not in newLetters:
                        pass
                    else:
                        s = scoreDic.get(w)
                        wordScore = wordScore + int(s)
                        print(w)
                        #newLetters.remove(w)
        return totalScore
