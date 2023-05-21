from typing import Any, Iterable, Iterator, List


class Sequence:
    """
    Specifies the interface for a sequence abstract data type.
    """

    def __init__(self, iterable: Iterable) -> None:
        """
        :param iterable: The iterable to initialize the sequence with in O(n) time
        :return: None
        """
        self._data: List[int] = list(iterable)
        self._size: int = len(self._data)
        return

    def __len__(self) -> int:
        """
        :return: The length of the sequence in O(1) time
        """
        return self._size

    def __iter__(self) -> Iterator:
        """
        :return: The iterator object in O(1) time
        """
        yield from self._data

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
