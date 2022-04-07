import tarfile
#Task 1: Extract all files inside a tar archive

# tar = tarfile.open("sample_tar.tgz")
# tar.extractall()
# tar.close()

#Task 2: Create tar archive
# tar = tarfile.open("sample_2.tar", "w")
# for name in ["file6.py", "file7.py", "oops.txt"]:
#     tar.add(name)
# tar.close()

#Task 3: Same as above but create a gzipped tar
with tarfile.open("sample_2.tar.gz", "w|gz") as tar:
    for name in ["file6.py", "file7.py", "oops.txt"]:
        tar.add(name)
