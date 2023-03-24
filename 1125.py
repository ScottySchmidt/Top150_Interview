"""
1255. Maximum Score Words Formed by Letters
HARD Level:  https://leetcode.com/problems/maximum-score-words-formed-by-letters/

Given a list of words, list of  single letters (might be repeating) and score of every character.
Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).
It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

Example 1:
Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
Output: 23
Explanation:
Score  a=1, c=9, d=5, g=3, o=2
Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
Words "dad" and "dog" only get a score of 21.

Example 2:
Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
Output: 27
Explanation:
Score  a=4, b=4, c=4, x=5, z=10
Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
Word "xxxz" only get a score of 25.
"""


# Second draft will correctly analyze a total score from the words given. However, how do you find the max poossible score? And do it dynamically?
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
                newLetters.append(l)   #print(newLetters)
        
        newLetters=[str(x) for x in newLetters] #print(newLetters, " new letters", type(newLetters))

        for word in words:
            for w in word:
                valid = True
                wordScore = 0
                if w not in newLetters:
                    valid = False
                else:
                    s = scoreDic.get(w)
                    wordScore = wordScore + int(s)
            if valid:
                totalScore = totalScore + wordScore
                newLetters = [l for l in newLetters if l not in list(word)]

        return totalScore


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
