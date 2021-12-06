from collections import defaultdict

input_value = ["eat", "tea", "tan", "ate", "nat", "bat"]

def solutions(words):
    answer = defaultdict(list)
    for word in words:
        temp = "".join(sorted(word))
        answer[temp].append(word)
    return answer.values()
        

print(solutions(input_value))