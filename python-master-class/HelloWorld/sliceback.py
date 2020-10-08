letters = "abcdefghijklmnopqrstuvwxyz"
#  0123456789     15   20
backwards = letters[::-1]
print(backwards)

qpo = letters[16:13:-1]
print(qpo)

edcba = letters[4::-1]
print(edcba)

lasteight = letters[25:25 - 8:-1]
# or letters[:-9:-1]
print(lasteight)

# returns end of sequence
print(letters[-4:])
#last item
print(letters[-1:])
#first item, does not give error if empty
print(letters[:1])
#first item, but throws error if empty
print(letters[0])
