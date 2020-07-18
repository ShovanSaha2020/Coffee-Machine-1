string1 = 'Happy birthday Birthday Birthday birthday birthday'
old = 'Birthday'
new = 'deathday'

print(string1.replace(old, new, 1))


whitespace_string = "     hey      "
normal_string = "incomprehensibilitieis"
print(normal_string)

# delete spaces from the left side
whitespace_string.lstrip()  # "hey      "

# delete "i" or "s" or "is" from the left side
normal_string.lstrip("is")  # "ncomprehensibilities"

# delete spaces from the right side
whitespace_string.rstrip()  # "     hey"

# delete "i" or "s" or "is" from the right side
normal_string.rstrip("is")  # "incomprehensibilitie"



# no spaces from both sides
whitespace_string.strip()  # "hey"

# delete trailing "i" or "s" or "is" from both sides
normal_string.strip('is')  # "ncomprehensibilitie"

word = "Mississippi"
print(word.lstrip("ips"))  # "Mississippi"
print(word.rstrip("ips"))  # "M"
print(word.strip("Mips"))  # ""

sentence = "London is the capital of Great Britain."
print(sentence)
sentence = sentence.lower()
print(sentence)
sentence.upper()
print(sentence)
sentence = sentence.replace("a", "x", 2)
print(sentence)
sentence.capitalize()
print(sentence)