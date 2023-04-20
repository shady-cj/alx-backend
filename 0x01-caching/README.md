# 0x01-caching

Understanding important caching concepts

At the end of the projects the following concepts should be fully understood


* What a caching system is
* What FIFO means
* What LIFO means
* What LRU means
* What MRU means
* What LFU means
* What the purpose of a caching system
* What limits a caching system have



## TASKS


### 0. Basic dictionary


Create a class `BasicCache` that inherits from `BaseCaching` and is a caching system:

* You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
* This caching system doesn’t have limit
* `def put(self, key, item)`:
    * Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    * If `key` or `item` is `None`, this method should not do anything.
* `def get(self, key)`:
    * Must return the value in `self.cache_data` linked to `key`.
    * If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.




```
guillaume@ubuntu:~/0x01$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
BasicCache = __import__('0-basic_cache').BasicCache

my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))

guillaume@ubuntu:~/0x01$ ./0-main.py
Current cache:
Current cache:
A: Hello
B: World
C: Holberton
Hello
World
Holberton
None
Current cache:
A: Hello
B: World
C: Holberton
Current cache:
A: Street
B: World
C: Holberton
D: School
E: Battery
Street
guillaume@ubuntu:~/0x01$ 
```


**File**:  `0-basic_cache.py`




### 1. FIFO caching


Create a class `FIFOCache` that inherits from `BaseCaching` and is a caching system:

* You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
* You can overload `def __init__(self)`: but don’t forget to call the parent init: `super().__init__()`
* `def put(self, key, item)`:
    * Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    * If `key` or `item` is `None`, this method should not do anything.
    * If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
        * you must discard the first item put in cache (FIFO algorithm)
        * you must print DISCARD: with the key discarded and following by a new line
* `def get(self, key)`:
    * Must return the value in `self.cache_data` linked to key.
    * If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.



```
guillaume@ubuntu:~/0x01$ cat 1-main.py
#!/usr/bin/python3
""" 1-main """
FIFOCache = __import__('1-fifo_cache').FIFOCache

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./1-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
DISCARD: B
Current cache:
C: Street
D: School
E: Battery
F: Mission
guillaume@ubuntu:~/0x01$ 
```


**File**: `1-fifo_cache.py`