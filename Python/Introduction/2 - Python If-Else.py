n = int(input())
odd = n % 2

if odd == 1:
    print("Weird")
elif odd == 0 and n in range(2,5):
    print("Not Weird")
elif odd == 0 and n in range(6,21):
    print("Weird")
elif odd == 0 and n > 20:
    print("Not Weird")
