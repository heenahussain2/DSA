# Hash Tables

## Overview
- A hash table is a super fast way to store and find data.
- We can think of a hash table as a special type of list where each item has a unique "address" created by a function called a hash function.
- The main advantage of hash tables over other data structures is speed.
- The access time of an element in a hash table is O(1) on average; therefore look up can be performed very fast.

## Basic Operations of Hash Tables
- **Search** - searches for an element in a hash table
- **Insert** - inserts an element in a hash table
- **Delete** - deletes an element from hash table

## Hash Functions
- Hash function is a way of mapping a key to a memory location.
- There are many different hash functions that can be used. for ex: h(k) = (length of the key) % 5 where h(k) is a hash function.
- The hash value is based only on the key, the value is irrelevant.

### Collisions
- Collision happens when more than one keys have the same hash value or same memory location.
- This can happen even with a well defined hash function.
- There are various approaches for handling collisions. Two of them are described below
    #### Linear Probing
    - This is a form of open addressing. If we can't use the slot given by the hash value or the address is taken, we move to the next available slot.
    #### Separate Chaining
    - With separate chaining we store multiple key-value pairs at the same location, usually with a linked list or an array

### Common methods of Collision Handling
- Closed Hashing (Open Addressing)
    - Linear Probing 
    - Quadratic Probing
    - Double Hashing

- Open Hashing
    - Separate Chaining

- An important consideration for the choice of collision resolution methods is achieving an even distribution of values within the available space.


## Application of Hash Tables
- Very Fast access to records, such as:
    - Bank Details
    - Product codes
    - Driver's licenses

- In Computing
    - Caching
    - Implementing sets
