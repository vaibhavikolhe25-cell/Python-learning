def main():
    try:
        a = int(input("heyyy, enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("heyy i am inside finally")

main()        