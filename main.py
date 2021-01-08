from trie import *

my_trie = insert(insert(empty_trie, 16, 99), 0, 121)

print(fetch(my_trie, 0)) # 121
print(fetch(my_trie, 16)) # 99

my_trie_without_0 = remove(my_trie, 0)
print(fetch(my_trie_without_0, 0)) # None