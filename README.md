# Trie

## Implementation of a Trie using Functional Programming Techniques

## Table of Contents
1. [Introduction](#introduction)
2. [List of Functions](#list-of-functions)
3. [Example](#example)
4. [Description of Functions](#description-of-functions)

## Introduction

A trie where pairs of natural numbers may be stored. These functions adhere to the following Functional Programming techniques:
* Immutability
* Pure functions
* No side-effects

This implementation of a trie can be used to implement other abstract data types (ADT) such as a RAM which can be found here:
[Implementation of RAM](https://github.com/tansonlee/ram)

## List of Functions
* empty_trie
* insert(trie, address, value)
* remove(trie, address)
* fetch(trie, address)

## Example

```python
my_trie = insert(insert(empty_trie, 16, 99), 0, 121)

print(fetch(my_trie, 0)) # 121
print(fetch(my_trie, 16)) # 99

my_trie_without_0 = remove(my_trie, 0)
print(fetch(my_trie_without_0, 0)) # None
```

The output is:
```python
121
99
None
```

## Description of Functions

**empty_trie**
* O(1) time
* returns the empty_trie

**insert(trie, address, value)**
* O(log(n)) where n = address
* takes a trie, natural number address, and natural number value
* returns a new trie with all the elements of trie and value at address

**remove(trie, address)**
* O(log(n)) where n = address
* takes a trie and natural number address
* returns a new trie without an element at address

**fetch(trie, address)**
* O(log(n)) where n = address
* takes a trie and address
* returns the value stored at address; None if there is no value stored there
