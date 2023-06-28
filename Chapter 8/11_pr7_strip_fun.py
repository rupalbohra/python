def remove(string, word):
    n_str = string.replace(word, "")
    return n_str.strip()

this = "    Harry is good    "
n = remove(this, "Harry")
print(n)

