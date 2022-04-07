#Task 1: File existence
# >>> import os
# >>> os.path.exists('oops.txt')
# True
# >>> os.path.exists('./oops.txt')
# True
# >>> os.path.exists('waffles')
# False
# >>> os.path.exists('.')
# True
# >>> os.path.exists('..')
# True

#Task 2: Is object
# >>> name = 'oops.txt'
# >>> os.path.isfile(name)
# True

# >>> os.path.isdir(name)
# False

# os.path.isdir('.')

# #Task 3: Absolute/Relative pathname
# >>> os.path.isabs(name)
# False
# >>> os.path.isabs('/big/fake/name')
# True
# >>> os.path.isabs('big/fake/name/without/a/leading/slash')
# False

#Task 4: copy with shutil module
# import shutil
# shutil.copy('oops.txt', 'ohno.txt')
#shutil.move('ohno.txt','oops.txt')

#Task 5: Rename
# import os
# os.rename('ohno.txt', 'ohwell.txt')

#Task 6: Links / check file/link
# import os
# os.link('oops.txt', 'yikes.txt') #Creates a hard-link
# print(os.path.isfile('yikes.txt'))
# print(os.path.islink('yikes.txt'))


#Task 7: Create symlinks
import os
os.symlink('oops.txt', 'jeepers.txt')
print(os.path.islink('jeepers.txt'))
print(os.path.abspath('oops.txt'))
os.path.realpath('jeepers.txt')

#Task 8: Change Permissions
# import os
# os.chmod('oops.txt', 0o400)

#Task 9: Change ownership with chown()
# import os
# uid = 1000 
# gid = 1000
# os.chown('oops.txt', uid, gid)

#Task 10: Delete a file
# import os
# os.remove('oops.txt')
# print(os.path.exists('oops.txt'))
