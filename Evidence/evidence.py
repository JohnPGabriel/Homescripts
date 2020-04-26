import speedtest
import time

def run_the_test():
    # actually do the test and return the results
    
    ev = speedtest.Speedtest()

    ev.get_best_server()

    ev.download()

    ev.upload()

    res = ev.results.dict()

    return res

if __name__ == "__main__":

    while 1 == 1:
        work = run_the_test()

        f = open('evidence.log','a')

        down = " down: " + str(work['download']/1000000)
#    print(down)
        up = " up: " + str(work['upload']/1000000)
#    print(up)
        ping = " ping: "+str(work['ping'])
#    print(ping)
        print(time.ctime() + down + up + ping )
        f.write(time.ctime() + down + up + ping + '\n')

        f.close()
        time.sleep(10800)   # sleep for 3 hours

    

