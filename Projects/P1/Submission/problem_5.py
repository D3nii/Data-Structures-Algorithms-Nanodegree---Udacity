import hashlib
import datetime

def calc_hash(self):
    sha = hashlib.sha256()

    hash_str = "We are going to encode this string of data!".encode('utf-8')

    sha.update(hash_str)

    return sha.hexdigest()

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.prev = None
        self.hash = self.calc_hash()

    def get_hash (self):
        return self.hash

	def get_data (self):
        return self.data  
      

    def calc_hash (self, val):
        tempStr = val.encode('utf-8')
        sha = hashlib.sha256()
        return sha.update(tempStr)

class BlockChain:

	def __init__ (self):
        self.head = None
        self.size = 0

	def append (self, val):
        if val is None:
            return

        self.size += 1
        node = self.head
	  
        if self.head is None:
            temp = Block(datetime.datetime.now(), value, None)
            self.head = temp
        else:
            while node.next:
                node = node.next
                node.next = Block(datetime.datetime.now(), value, self.head)

    def get_size(self):
        return self.size

    def to_list(self):
        ans = []
        node = self.head
      
        while node:
            out.append([node.data, node.timestamp, node.hash])
            node = node.previous_hash
      
        return ans

# Tests

test_1 = BlockChain()

print('\t Block Chain = BlockChain()')
print('size : ' + test_1.get_size()) # 0
print(blockchain.to_list()) # []

test_2 = BlockChain()

test_2.append('try1')
print('size : ' + test_2.get_size()) # 1
print(blockchain.to_list()) # [['try1', 1564306421.0008988, hash_value]]

test_3 = BlockChain()

test_3.append('try1')
test_3.append('try2')
test_3.append('try3')
test_3.append('try4')
print('size : ' + test_3.get_size()) # 1
print(blockchain.to_list()) # [['try1', 1564306378.6235423, hash_value_try1], ['try2', 1564306378.6235056, hash_value_try2], ['try3', 1564306378.623468, hash_value_try3], ['try4', 1564306378.6234293, hash_value_try4],]

test_4 = BlockChain()

test_4.append(4) # TypeError
test_4.append('') # ValueError
