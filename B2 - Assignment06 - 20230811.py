# Assignment 06 - Create a new list by merging two existing list

names = ["Alice", "Bob", "Charlie"]     # iterable
scores = [85, 90, 78]                   # iterable

zipped_list = zip(names, scores)        # combining to two list with zip() to set a iterator

combined_list = list(zipped_list)       # using list() to convert a iterator to list

print(f"Combined list: {combined_list}")