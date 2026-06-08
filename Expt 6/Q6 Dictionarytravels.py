my_marks={"python":50,"ct":60,"se":50}
sums=0
for i in my_marks.values():
    sums+=i

print(sums)
print(sum(my_marks.values()))
print(max(my_marks.values()))
