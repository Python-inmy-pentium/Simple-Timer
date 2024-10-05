def timer_2():
    m = int(input("Enter the minutes: "))
    s = int(input("Enter the seconds: "))
    total = (m * 60) + s
    # print(total), for dev's use only
    times = divmod(total, 60)
    print("%02d" % times[0], ":", "%02d" % times[1])
    while True:
        if times[0] == times[1] == 0:
            print("The End!")
            break
        else:
            total -= 1
            sleep(1)
            times = divmod(total, 60)
            print("%02d" % times[0], ":", "%02d" % times[1])


timer_2()
