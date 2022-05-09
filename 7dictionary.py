from ipaddress import ip_address


d1 = { }
print(type(d1))
d2 = { "ashish":"burgur","rohan":"fish","skillf":"roti","ritik":{"b":"maggie","c":"tikki","l":"paties"}}
print("1",d2)
print("2",d2["ashish"])
print("3",d2["ritik"])
print("4",d2["ritik"]["b"] )
d2["ankit"] = "junk food"
print("5",d2)
d2[420] = "kabab"
print("6",d2)
del d2[420]
print("7",d2)
d3=d2
#del d3["ashish"]
print("8",d2)#d2 m se bhi delete ho jayega content isliye copy krke delete krenge
d3=d2.copy()
del d3["ashish"]
print("9",d3)
print("10",d3.get("ashish"))
d2.update({"leena":"toffee"})
print("11",d2)
print("12",d2.keys())
print("12",d2.items())








if __name__ == '__main__':
    term = int(input())
    dec={}
    for i in range (term):
        name = input()
        mark1= int(input())
        mark2= int(input())
        mark3= int(input())
        marks = [mark1,mark2,mark3]
        avg = sum(marks)/3
        # dec.add({name:avg})
        dec[name]=round(avg,2)

    ans = input()
    print(format(dec[ans],".2f"))