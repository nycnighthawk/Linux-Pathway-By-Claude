# Lab: read a filesystem image (the operations a VFS filesystem implements)

A filesystem driver translates VFS requests (look up a name, list a directory, read a file) into reads of an on-disk format. `setup` builds `tiny.img`, a small image in the made-up TinyFS format described in the docstring of `tfs.py`: a superblock, an inode table, files stored in direct blocks and directories that are files of fixed-size entries.

## Your task

Implement `inode`, `data`, `lookup`, `listdir` and `read` in `tfs.py`. Use the error classes a real filesystem would report: `FileNotFoundError` (ENOENT), `NotADirectoryError` (ENOTDIR) and `IsADirectoryError` (EISDIR). Pay attention to a file that spans several blocks and to the exact size: data past `size` in the last block is not part of the file.

In a kernel filesystem the same code appears as `lookup` in an inode operations table, `iterate_shared` for directories, and `read_iter` or `readahead` for file data, with the page cache between the VFS and the block device. That mapping is the topic of the lesson.
