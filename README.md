# CombineDocuments
Generic Merger for text documents.
Folder used to read/write should be in the same level at 'default' package

	python3 main_merger.py --input <input-folder-location> --output <output--folder-location>

UPDATES:
==========
[2019-02-06]
1. Transforms multiple files into one document per line file
2- Refactor for classes, text parser, command line, etc.

[2018-12-08]
1. Messages for empty line not printed anymore
2. Included function to deal with unwanted binary characters

[2018-12-07]
1. Fixed relative paths
2. output should contain the output-filename as well
3. removed output file name from command line

[2018-10-30]
1. Combines several files in one single file
2. Skips empty text files