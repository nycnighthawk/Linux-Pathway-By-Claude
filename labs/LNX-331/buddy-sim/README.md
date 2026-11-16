# Lab: write a buddy allocator

The kernel's page allocator hands out blocks of `2**order` pages and keeps one free list per order. When a small block is needed and only a bigger one is free, the bigger one is **split** into two *buddies*; when both buddies of a block are free again they are **merged**. This keeps large contiguous blocks available as long as possible.

`buddy.py` models a 64-page zone. Implement `alloc(order)` and `free_block(pfn, order)`:

- `alloc`: take the smallest free block that fits (lowest start page if several), split it down to the requested order, keeping the lower half and putting each upper half onto the next lower free list; return the start page, or `None` if nothing fits;
- `free_block`: the buddy of a block at page `p` of order `k` starts at `p ^ (1 << k)`; merge while the buddy is free at the same order, then add the result to its list.

`check` replays a 16-step script of allocations and frees and compares your free lists with a reference after every step. Notice what happens to the largest block after a few small allocations and frees: this is how fragmentation starts.
