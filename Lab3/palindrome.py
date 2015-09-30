#pal = input()

#if str(pal) == str(pal)[::-1]:
#  print "true"
#else: print "false"

def palindrome(pal):
  if len(pal) <= 1:
    return True
  else:
    if pal[0] != pal[len(pal)-1]:
      return False
    else:
      return palindrome(pal[1:len(pal)-1])

pal = input("Enter a word! ")

print(palindrome(pal))