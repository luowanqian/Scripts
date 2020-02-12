# 1. Collection

集合相关接口实现

- [1. Collection](#1-collection)
  - [1.1. 迭代器](#11-迭代器)
  - [1.2. 索引](#12-索引)

## 1.1. 迭代器

实现一个简单可迭代集合，见 [iterator.py](./iterator.py)

## 1.2. 索引

要实现 `Numpy` 那种索引方式，需要根据数据维度大小对 `Slice` 对象进行转换

已知矩阵 `A` 的大小 `shape=(4, 5)`，`__getitem__` 得到的 `Slice` 对象经过函数 `normalize_index` (源码见 [slicing.py](./slicing.py)) 转换后可得

| 表达式 | Key of `__getitem__` | `normalize_index(key)` |
| ---- | ---- | ---- |
| `A[2, 3]` | `(2, 3)` | `(2, 3)` |
| `A[1:3, 2]` | `(slice(1, 3, None), 2)` | `(slice(1, 3, 1), 2)` |
| `A[1:3]` | `slice(1, 3, None)` | `(slice(1, 3, 1), slice(0, 5, 1))` |
| `A[1:, 2]` | `(slice(1, None, None), 2)` | `(slice(1, 4, 1), 2)` |
| `A[:3, 2]` | `(slice(None, 3, None), 2)` | `(slice(0, 3, 1), 2)` |
| `A[:, 2]` | `(slice(None, None, None), 2)` | `(slice(0, 4, 1), 2)` |

Example:

```python
from slicing import normalize_index


class Matrix:
    def __init__(self, shape):
        self._shape = shape

    def __getitem__(self, key):
        return key


shape = (4, 5)
A = Matrix(shape)
key = A[1:3, 2]
nkey = normalize_index(key, shape)
print(f"Original key: {key}")
print(f"Normalized key: {nkey}")
```

output:

```
Original key: (slice(1, 3, None), 2)
Normalized key: (slice(1, 3, 1), 2)
```