s = set()
print(type(s))
s_from_list= set([1,2,3,4])
print("1",s_from_list)


l=[6,7,8,9]
s_list=set(l)
print("2",s_list)


s.add(1)
print("3", s)
s.add(2)
print("4", s)
s.union({1, 6})
print("5", s)
s.add(2)
print("6", s)
s1 = s.intersection({1, 2, 4, 5, 6})
print("7", s, s1)
print("8", len(s))
print("9", min(s))
print("10", max(s))
s1 = {4, 6}
print("11", s.isdisjoint(s1))
s.remove(2)
print("12", s)
