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
2. Array data structure (i.e) specialized implementation of static sequence interface
3. Asymptotic complexity
	1. Static operations
		1. `__getitem__(index), __setitem__(index, value)` : $O(1)$
	2. Dynamic operations
		1. `insert_first(value), delete_first()` : $O(n)$
		2. `insert_last(value), delete_last()` : $O(n)$
		3. `__setitem__(index, value), __delitem__(index)` : $O(n)$
4. The invariant is that array is full (for consistency).

### Linked List
1. Motivation : Can we make the insert, and delete at front really efficient ?
2. Idea : Use a node (data, and pointer to next node) to build a list. We can manipulate the nodes by re-linking pointers. This data-structure is referred as singly inked list.
3.  Asymptotic complexity of singly linked list
	1. `insert_first(value), delete_first()` : $O(1)$
	2. `insert_last(value), delete_last()` : $O(n)$
	3. `__getitem__(index), __setitem__(index, value), __delitem__(index)` : $O(n)$
4. Can we use the pointer data structures to make insert, and delete at last efficient as well ? Yes, this implementation is referred as doubly linked list data structure.
5. Asymptotic complexity of doubly linked list
	1. `insert_first(value), delete_first()` : $O(1)$
	2. `insert_last(value), delete_last()` : $O(1)$
	3. `__getitem__(index), __setitem__(index, value), __delitem__(index)` : $O(n)$

### Dynamic Array
1. Motivation :
	1. Linked list are really efficient for `insert_first(value), delete_first(), insert_last(value), delete_last()`.
	2. Arrays are really efficient for  `__getitem__(index), __setitem__(index, value)`
	3. Can we have a data-structure that combines the best of both the worlds ?
2. Idea : Allocate extra space heuristically to reduce number of re-allocations.
	1. Fill ratio : Ratio of items to space ($r = \frac{|Items|}{|Sequence|} \in [0,1]$)
	3. When the fill ratio reaches a threshold, allocate $\Theta(n)$ extra space to reduce the fill ratio (i.e.) $r < r_i$. We will have to wait for $\Theta(n)$ items to be filled before threshold is reached again.
3. Cost amortization :
	1. Let us assume that our threshold fill ratio is 1, and we reduce it 0.5 when required (i.e) double the size when the array is full.
	2. We will resize at $1, 2, 4, 8, ...$
	3. A single operation of reallocation will cost $\Theta(n)$ time. $$\text{cost} = \Theta(\sum_{i=0}^{log_{2}(n)} 2^i) = \Theta(2^{log_{2}(n))} = \Theta(n)$$
	4. As we are adding $\Theta(n)$ extra space, a sequence of $\Theta(n)$ operations will also take $\Theta(n)$ time (i.e) each operation take $\Theta(1)$ time "on average"
4. Deletion at last :
	1. When we delete an element from back, it is $\Theta(1)$. However, in such cases the fill ratio will decrease, and space is wasted.
	2. To avoid wastage of space, we can resize when the fill ratio is below a threshold (i.e.) $r < r_d$. The resize done to $r_i: r_d < r_i$
	4. We need $\Theta(n)$ inserts before next resize. Therefore, the cost is amortized.
5. Handling `insert_first(value), delete_first()` :
	1. Idea : Store the items in the middle of an array instead of front. This leaves `n` slots in the beginning and the end of an array.
	2. The cost of rebuilding is $\Omega(n)$ gets amortized as it is in between linear time operations.
6. Asymptotic complexity
	1. Static operations
		1. `__getitem__(index), __setitem__(index, value)` : $O(1)$
	2. Dynamic operations
		1. `insert_first(value), delete_first()` : $O(1_{(a)})$
		2. `insert_last(value), delete_last()` : $O(1_{(a)})$
		3. `__setitem__(index, value), __delitem__(index)` : $O(n)$

## Set Interface
1. Set has an intrinsic order using unique keys.
2. Set interface
```python
from typing import Any, Iterator, Iterable


class SetInterface:
	def __init__(self, iterable: Iterable) -> None:
		"""
		:param iterable: The iterable to be used to initialize the set
		"""
		raise NotImplementedError

	def __len__(self) -> int:
		"""
		:return: The number of elements in the set
		"""
		raise NotImplementedError

	def __getitem__(self, key: Any) -> Any:
		"""
		:param key: The key to be searched in the set
		:return: The value associated with the key
		"""
		raise NotImplementedError

	def __setitem__(self, key: Any, value: Any) -> None:
		"""
		:param key: The key to be inserted in the set
		:param value: The value to be inserted in the set
		"""
		raise NotImplementedError

	def __delitem__(self, key: Any) -> None:
		"""
		:param key: The key to be deleted from the set
		"""
		raise NotImplementedError

	def __iter__(self) -> Iterator:
		"""
		:return: An iterator over the set
		"""
		raise NotImplementedError

	def __sorted__(self) -> Iterator:
		"""
		:return: An iterator over the set in the key order
		"""
		raise NotImplementedError

	def __next__(self) -> Any:
		"""
		:return: The next element in the set
		"""
		raise NotImplementedError

	def __contains__(self, key: Any) -> bool:
		"""
		:param key: The key to be searched in the set
		:return: True if the key is present in the set, False otherwise
		"""
		raise NotImplementedError

	def find_min(self) -> Any:
		"""
		:return: The item corresponding to the minimum key in the set
		"""
		raise NotImplementedError

	def find_max(self) -> Any:
		"""
		:return: The item corresponding to the maximum key in the set
		"""
		raise NotImplementedError

	def find_next(self, key: Any) -> Any:
		"""
		:param key: The key to be searched in the set
		:return: The item with minimal key larger than <key>
		"""
		raise NotImplementedError

	def find_prev(self, key: Any) -> Any:
		"""
		:param key: The key to be searched in the set
		:return: The item with maximal key smaller than <key>
		"""
		raise NotImplementedError

```
3. Special case interfaces: `dictionary` (set without order operations : `find_min, find_max, find_next, find_prev`)

## Resources
1. [Lecture Page](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-2-data-structures-and-dynamic-arrays/)
