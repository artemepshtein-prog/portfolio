
def askPassword(right_password, tries_count):
    for i in range(tries_count):
        print("write the right code")
        test = input()

        if test == right_password:
            print("thets the right password ")
            break
    print("your tries ended")

askPassword("abc123", 3)
askPassword("test", 1)