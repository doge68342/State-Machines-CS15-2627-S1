state = "still"
feeling = ""
while True:
    if state == "still":
        print("standing still")
        while True:
            feeling = input("What to do [run, jump, stop] - ")

            if feeling == "run":
                state = "running"
            elif feeling == "jump":
                state = "falling"
            else:
                state = "still"  
            break

    elif state == "running":
        print("running")
        while True:
            feeling = input("What to do [stop, jump, continue] - ")

            if feeling == "stop":
                state = "still"
            elif feeling == "jump":
                state = "falling"
            else:
                state = "running"
            break
            
    elif state == "falling":
        print("falling")
        while True:
            feeling = input("What to do [land, run, keep falling... ?] - ")

            if feeling == "land":
                state = "still"
            elif feeling == "run":
                state = "fell over"
            else:
                state = "falling"
            break

    elif state == "fell over":
        print("fell over")
        while True:
            feeling = input("What to do [get up, panic, accept fate] - ")

            if feeling == "get up":
                state = "still"
            elif feeling == "panic":
                state = "running"
            else:
                state = "fell over"
            break
            
    