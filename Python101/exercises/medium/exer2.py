from collections import Counter
text = input("write any text you like:")
word_dict={}
def word (prompt):
    words = text.lower().replace('.', '').split()
    word_dict = dict(Counter(words))
    return word_dict

result = word(text)
print(f"the word count of the text entered is : {result}")

            