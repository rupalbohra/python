S = set()
S.add(20)
S.add(20.0)  # 20 and 20.0 will be counted as one entity
S.add("20")
print(len(S))