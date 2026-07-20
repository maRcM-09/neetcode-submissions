class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        # define a hash map using the similarity pairs
        if len(sentence1) != len(sentence2):
            return False
        h = defaultdict(set)
        for word1 , word2 in similarPairs:
            h[word1].add(word2)
            h[word2].add(word1)
        
        for i in range(len(sentence1)):
            if not (sentence1[i] == sentence2[i] or sentence2[i] in h[sentence1[i]]):
                return False
        return True
                
