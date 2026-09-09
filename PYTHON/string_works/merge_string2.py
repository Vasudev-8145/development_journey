"""
function unequall merge
"""

def unequall_merge(word1,word2):

   merge_str = ""
   small_str = min(word1,word2,key=len)
   large_str = max(word1,word2,key=len)

   for i in range(0,len(small_str)):

      merge_str += word1[i] + word2[i]

   balance = large_str[len(small_str):]

   merge_str += balance

   print(merge_str)

unequall_merge("pqrst","abc")
unequall_merge("leo","messi")