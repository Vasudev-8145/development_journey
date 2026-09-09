# palindrome programme without slicing

class Palindrome:

    def solution(self,word):

        org_word = word
        org_word = list(org_word)

        left = 0
        right = len(word)-1

        word = list(word)

        while(left<right):

            word[left],word[right] = word[right],word[left]

            left+=1
            right-=1

        if word == org_word:
            return True

        else:
            return False

pal_instance = Palindrome()

print(pal_instance.solution("madam"))
print(pal_instance.solution("night"))






        