#WAP to check the list is palindrome or not.

list1 = [1,2,3,2,1]
list2 = ['m','m','a','m','m']

copy_list1 = list1.copy()
copy_list1.reverse()

copy_list2 = list2.copy()
copy_list2.reverse()

if (copy_list1 == list1):
    print('palindrome')
else:
    print('Not palindrome')

if (copy_list2 == list2):
    print('palindrome')
else:
    print('Not palindrome')