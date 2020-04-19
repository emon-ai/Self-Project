def door_lock():
    attemp = input("What is your password?\n>>")
    if attemp==password:
        print("Welcome!")
    else:
        print("Access Denied!")
        for i in range(3):
            em_key=input("What is your emergency code?\n>>")
            if em_key==emergency:
                print("Welcome!")
                break
            elif i==2:
                print("Ring Alarms")
            else:
                print("Try again!")


password="mdemon21"
emergency="1234"
door_lock()