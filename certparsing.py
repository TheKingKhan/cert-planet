import subprocess

print "start"
command0 = './ssl-cert-info.sh --host '
command1 = ' --end >> certinfo.txt'
subprocess.call("python pcap-url.py example.pcap > urls.txt", shell=True)
file = open("urls.txt","r")
for line in file:
	line = line[:-2]
	#command = command0 + line + command1
	#print command
	subprocess.call('./ssl-cert-info.sh --host %s --issuer >> certinfo.txt' % line, shell=True)
	#subprocess.call('./ssl-cert-info.sh --host %s --subject >> certinfo.txt' % line, shell=True)
	#subprocess.call('./ssl-cert-info.sh --host %s --options -dates >> certinfo.txt' % line, shell=True)

 
print "end"
