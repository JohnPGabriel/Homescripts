import subprocess
import time


a = 0
while 1 == 1:
	f = open(time.strftime('%B%d%H%M') + ' ping log.log','w+')
	m = open('Summary ping errors.log','a')

	while a < 2880:		# 24 hours of 30 second interval pings
		output = subprocess.run(['ping','www.telstra.com'],capture_output=True)
		try:
			print(time.ctime() + ' = ' + output.stdout.decode().splitlines()[2])
			f.write(time.ctime() + ' = ' + output.stdout.decode().splitlines()[2] + '\n')
		except Exception:
			print(time.ctime() + ' = ' + output.stdout.decode())
			f.write(time.ctime() + ' = ' + output.stdout.decode())
			m.write(time.ctime() + ' = ' + output.stdout.decode())
			
		a+=1
		time.sleep(30)
	# close the files and reopen
	f.close()
	m.close()
	a=0
	
# need to do a loop that makes a new file each day with the appropriate timestamp - for detailed logs?
# or maybe have two logs - one that just has the dead ones for summary and the other that has details of both
# should use time stamping on the file names

f.close()
m.close()