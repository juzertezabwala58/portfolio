# 📚 Data Structures: Stacks and Queues

## 📌 Overview
Clean, Object-Oriented Python implementations of fundamental linear data structures: **Stack (LIFO)**, **Queue (FIFO)**, and **Circular Queue**.

---

## 🛠️ Data Structures Implemented

### 1. **Stack (Last-In-First-Out)**
- `push(item)`: Inserts element to top of stack with overflow protection.
- `pop()`: Removes and returns top element with underflow handling.
- `peek()`: Inspects top element without removing.
- `is_empty()` & `is_full()`: State validation helpers.

### 2. **Queue (First-In-First-Out)**
- `enqueue(item)`: Appends element to rear of queue.
- `dequeue()`: Extracts element from front of queue.
- `peek()`: Returns front element.

### 3. **Circular Queue (Ring Buffer)**
- Uses modular pointer arithmetic:
  $$\text{rear} = (\text{rear} + 1) \pmod{\text{capacity}}$$
  $$\text{front} = (\text{front} + 1) \pmod{\text{capacity}}$$
- Efficient space utilization without element shifting.

---

## ⚡ How to Run
```bash
python stack_and_queue.py
```
