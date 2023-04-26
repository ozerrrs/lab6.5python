def commonElements(list1, list2):
    value = []
    for i in list1:
        if i in list2 and i not in value:
            value.append(i)
    return value
def eratosthenes(lst):
    _prime = [True] * (max(lst) + 1)

    _prime[0] = _prime[1] = False

    for i in range(2, int(max(lst) ** 0.5) + 1):
        if _prime[i]:
            for j in range(i * i, max(lst) + 1, i):
                _prime[j] = False
    prime_list = [x for x in lst if _prime[x]]
    return prime_list

def palindrome(str):
    palindrome_array = []
    for string in str:
        if string == string[::-1]:
            palindrome_array.append(string)
    return palindrome_array

def anagrams(word, word_list):
    sorted_word = sorted(word.lower().replace(" ", ""))
    return [w for w in word_list if sorted(w.lower().replace(" ", "")) == sorted_word]

list1= [1,2,3,4,5]
list2 = [3, 4, 5, 6, 7]
common = commonElements(list1, list2)
print(common)
lst = ["level", "deified", "python", "madam", "racecar"]
result = palindrome(lst)
print(result)
lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
primes = eratosthenes(lst)
print(primes)
def anagrams(word, word_list):
    sorted_word = sorted(word.lower().replace(" ", ""))
    return [w for w in word_list if sorted(w.lower().replace(" ", "")) == sorted_word]

word = "listen"
word_list = ["enlist", "google", "inlets", "banana"]
anagram_list = anagrams(word, word_list)
print(anagram_list)