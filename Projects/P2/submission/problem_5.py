## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.word = False

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root

        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]

        node.word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root

        for i in prefix:
            if i not in node.children:
                return None
            node = node.children[i]

        return node


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.word = False

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, prefix=""):
        temp = self.recur(prefix)

        return ",".join(temp)

    def recur(self, prefix):
        if self.word:
            yield prefix

        for char, node in self.children.items():
            yield from node.recur(prefix + char)

MyTrie = Trie()

wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    MyTrie.insert(word)

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


interact(f, prefix='')


print(MyTrie.find("ant").suffixes())  # hology, agonist, onym
print(MyTrie.find("f").suffixes())  # un, unction, actory
print(MyTrie.find("lol").suffixes())  # lol not found
print(MyTrie.find("t").suffixes())  # rie, rigger, rigonometry, ripod
print(MyTrie.find("trig").suffixes())  # ger, onometry