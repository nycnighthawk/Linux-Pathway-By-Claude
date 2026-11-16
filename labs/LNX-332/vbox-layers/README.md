# Lab: check include direction between source layers

A large code base stays maintainable when lower layers never include higher ones. `setup` writes `layers.py` with a simplified table of VirtualBox source directories and their rank. Implement `layer_of` (longest matching prefix) and `violations` (an include that points up the stack).

The table is a teaching model of `src/VBox`; real dependencies are looser and the directory names change between versions (to verify). To explore the real tree, fetch the OSE source from the project's download page and list `src/VBox`.
