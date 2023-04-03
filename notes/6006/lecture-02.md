# Data Structure

## Sequence Interface
1. The objective is to maintain a sequence of items whose ordering is extrinsic. Example : $\{x_0, x_1, ..., x_{n-1}\}$ is a sequence with $n$ items.
2. Type of sequences :
	1. Static : The length of the sequence doesn't change.
	2. Dynamic : The length of the sequence changes.
3. Static sequence interface :
```python
from typing import Iterable, Iterator, Any

class StaticSequence:
	""" An interface for static sequence """
	
	def __init__(self, iterable : Iterable) -> None:
		"""
		:param iterable: The iterable to initialize the sequence with in O(n) time 
		:return: None
		"""
		raise NotImplementedError
	
	def __len__(self) -> int:
		"""
		:return: The length of the sequence in O(1) time 
		"""
		raise NotImplementedError

	def __iter__(self) -> Iterator:
		""" 
		:return: The iterator object in O(1) time
		"""
		raise NotImplementedError
	
	def __next__(self) -> Any:
		"""  
		:return: The next item in the sequence in O(1) time
		"""
		raise NotImplementedError
	
	def __getitem__(self, index: int) -> Any:
		""" 
		:return: The value at the given index in O(1) time 
		"""
		raise NotImplementedError

	def __setitem__(self, index: int, value: Any) -> None:
		"""
		:param index: The index at which the value is to be set in O(1) time
		:param value: The value to be set 
		"""
		raise NotImplementedError

```
4. Dynamic sequence interface : 
```python
from typing import Iterable, Iterator, Any

class DynamicSequence:
	""" An interface for dynamic sequence """
	
	def __init__(self, iterable : Iterable) -> None:
		"""
		:param iterable: The iterable to initialize the sequence with in O(n) time 
		:return: None
		"""
		raise NotImplementedError
	
	def __len__(self) -> int:
		"""
		:return: The length of the sequence in O(1) time 
		"""
		raise NotImplementedError

	def __iter__(self) -> Iterator:
		""" 
		:return: The iterator object in O(1) time
		"""
		raise NotImplementedError
	
	def __next__(self) -> Any:
		"""  
		:return: The next item in the sequence in O(1) time
		"""
		raise NotImplementedError
	
	def __setitem__(self, key: int, value: Any) -> None:
		"""
		:param key: The index at which the value is to be inserted in O(1) time. For resizing the array needs to relocated which is O(n) time.
		:param value: The value to be inserted 
		"""
		raise NotImplementedError
		
	def __getitem__(self, key: int) -> Any:
		""" 
		:param key: The index of the value to be returned in O(1) time.
		:return: The value at the given index.
		"""
		raise NotImplementedError
		
	def __delitem__(self, key: int) -> None:
		"""
		:param key: The instance to be deleted in O(n) time
		"""
		raise NotImplementedError

	def insert_first(self, value: Any) -> None:
		"""
		:param value: The value to be inserted at the beginning of the sequence in O(n) time
		"""
		raise NotImplementedError

	def delete_first(self, value: Any) -> None:
		"""
		:param value: The value to be deleted from the beginning of the sequence in O(n) time
		"""
		raise NotImplementedError

	def insert_last(self, value: Any) -> None:
		""" 
		:param value: The value to be inserted at the end of the sequence in O(1) time. For resizing the array needs to relocated which is O(n) time.
		"""
		raise NotImplementedError

	def delete_last(self, value: Any) -> None:
		"""
		:param value: The value to be deleted from the end of the sequence in O(1) time. For resizing the array needs to relocated which is O(n) time. 
		"""
		raise NotImplementedError

```
5. Special case interfaces :
   1. Stack : `insert_last` and `delete_last`. Last in first out.
   2. Queue : `insert_last` and `delete_first`. First in first out.

### Array
1. An array is great for static operations but not so good for dynamic operations. This is due to cost of reallocating, and shifting items when array grows in size.
2. Asymptotic complexity
	1. Static operations
		1. `__getitem__(index), __setitem__(index)` : $O(1)$
	2. Dynamic operations 
		1. `insert_first(value), delete_first()` : $O(n)$
		2. `insert_last(value), delete_last()` : $O(n)$
		3. `__setitem__(index, value), __delitem__(index)` : $O(n)$
3. The invariant is that array is full (for consistency). 

### Linked List
1. 

### Dynamic Array
1. 

## Set Interface 
1. 

## Resources
1. [Lecture Page](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-2-data-structures-and-dynamic-arrays/)