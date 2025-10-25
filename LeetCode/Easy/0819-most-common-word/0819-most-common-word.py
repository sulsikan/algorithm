class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Data Cleansing
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph.lower()).split() if word not in banned]
        '''
        words = []
        paragraph = re.sub('[^a-z]', ' ', paragraph.lower())
        for i in paragraph.split():
            if i not in banned:
                words.append(i)
        '''

        counts = collections.Counter(words)
        #return max(counts, key=counts.get)
        return counts.most_common(1)[0][0]
