#Count no of strings whose length is 2
#
def match_words(words):
	  ctr = 0	
for word in words:
	  if len(word) > 1 and word[0] == word[-1]:
8	      ctr += 1
7	      return ctr
8	
print(match_words(['abc', 'xyz', 'aba', '1221']))