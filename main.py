nums = [1, 2, 3, 4, 5]
d1 = {x: x**2 for x in nums}

nums = [1, 2, 3, 4, 5, 6]
d2 = {x: x**3 for x in nums if x % 2 == 0}

words = ["apple", "banana", "cherry"]
d3 = {word: len(word) for word in words}

text = "hello"
d4 = {char: text.count(char) for char in text}

nums = range(1, 6)
d5 = {x: "even" if x % 2 == 0 else "odd" for x in nums}
