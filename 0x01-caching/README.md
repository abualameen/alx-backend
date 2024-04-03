## Caching System 

### What is a caching system?

A caching system is a mechanism used in computing to store frequently accessed data in a faster and more accessible location than the original source. This improves performance by reducing the time it takes to retrieve data, as the cached data can be accessed quickly without needing to fetch it from the original source every time.

### FIFO

FIFO stands for "First In, First Out." It is a caching algorithm where the first item added to the cache is the first one to be removed when the cache reaches its capacity. This means that the oldest item in the cache is evicted to make room for new items.

### LIFO

LIFO stands for "Last In, First Out." It is a caching algorithm where the most recently added item to the cache is the first one to be removed when the cache reaches its capacity. This means that the newest item in the cache is evicted first.

### LRU

LRU stands for "Least Recently Used." It is a caching algorithm where the least recently accessed item in the cache is the first one to be removed when the cache reaches its capacity. This means that the item that has not been accessed for the longest time is evicted first.

### MRU

MRU stands for "Most Recently Used." It is a caching algorithm where the most recently accessed item in the cache is the first one to be removed when the cache reaches its capacity. This means that the item that has been accessed most recently is evicted first.

### LFU

LFU stands for "Least Frequently Used." It is a caching algorithm where the item that has been accessed the least number of times is the first one to be removed when the cache reaches its capacity. This means that the least frequently accessed item is evicted first.

### Purpose of a caching system

The purpose of a caching system is to improve performance by storing frequently accessed data in a faster and more accessible location. By doing so, it reduces the time it takes to retrieve data, thereby enhancing the overall efficiency and responsiveness of a system or application.

### Limits of a caching system

Caching systems have several limitations, including:

1. **Limited capacity:** Caching systems have a finite capacity, meaning they can only store a certain amount of data. Once the cache reaches its capacity, it must evict existing items to make room for new ones.
  
2. **Cache eviction:** When the cache is full, it must decide which items to evict to make room for new data. This eviction process can be based on various algorithms such as FIFO, LIFO, LRU, MRU, or LFU, each with its own advantages and disadvantages.
  
3. **Cache coherence:** In distributed systems where multiple caches are used, maintaining cache coherence becomes challenging. Ensuring that all caches have consistent data can be complex and resource-intensive.
  
4. **Cache invalidation:** Caches must be kept up-to-date with changes to the underlying data. Cache invalidation mechanisms are needed to ensure that cached data remains accurate and relevant.
