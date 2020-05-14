class TrieNode:
    def __init__(self):
        self.word=False
        self.children={}
class Trie(object):
    def __init__(self):
        self.root=TrieNode()
    def insert(self, word):
        runner=self.root
        for char in word:
            if char not in runner.children:
                runner.children[char]=TrieNode()
            runner=runner.children[char]
        runner.word=True
    def search(self, word):
        runner=self.root
        for char in word:
            if char not in runner.children:
                return False
            runner=runner.children[char]
        return runner.word
    def startsWith(self, prefix):
        runner=self.root
        for char in prefix:
            if char not in runner.children:
                return False
            runner=runner.children[char]
        return True
    
obj = Trie()
obj.insert("word")
print(obj.search("word"))
print(obj.startsWith("wo"))