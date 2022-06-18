version_string = input().split('.')
version_int = int(''.join(version_string))
version_int += 1
version_new_string = str(version_int)
result = '.'.join(x for x in version_new_string)
print(result)