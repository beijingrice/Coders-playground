from subprocess import call
while True:
    try:
        text = input(">>> ")
        if text == "EXIT":
            break
        if text != "EXIT":
            call(["say",text])
    except KeyboardInterrupt:
        break