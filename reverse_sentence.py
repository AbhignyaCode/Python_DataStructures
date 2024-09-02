string = 'hello my name is aadil'
words = string.split()
print(words)
reversed_words = [word[::-1] for word in words]
print(reversed_words)
reversed_string = ' '.join(reversed_words)

print(reversed_string)
