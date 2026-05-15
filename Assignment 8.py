def replace(s, old, new):
    parts = s.split(old)
    answer = new.join(parts)
    return answer


print(replace("Mississippi", "i", "I"))

sentence = "I love spom! Spom is my favorite food. Spom, spom, yum!"

print(replace(sentence, "om", "am"))
print(replace(sentence, "o", "a"))
