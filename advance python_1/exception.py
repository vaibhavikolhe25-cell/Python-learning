try:
    a = int(input("hey,enter a number: "))
    print(a)
except ValueError as v:
    print("heyyyy")
    print(v)

except Exception as e:
     print(e)

print("thank you")

