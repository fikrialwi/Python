def encryptDecrypt(inpString):
 
    xorKey = 'Q';
 
    for i in range(len(inpString)):
     
        inpString = (inpString[:i] +
             chr(ord(inpString[i])^ord(xorKey)) +
                     inpString[i + 1:])     
    return inpString

print(encryptDecrypt("dzul"))
print(encryptDecrypt(encryptDecrypt("dzul")))