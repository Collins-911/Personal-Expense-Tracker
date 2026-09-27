from datetime import datetime





while True:
    count = 60
    time = datetime.now().strftime("%I:%M:%S:%p")
    time_to_string = str(time)
    print(time_to_string)
    count-=1
