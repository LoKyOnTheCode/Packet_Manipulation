#!/usr/bin/env python3

from scapy.all import *
import random, sys




def console():

	print("""

  __  __       _         __  __
 |  \/  |     (_)       |  \/  |
 | \  / | __ _ _ _ __   | \  / | ___ _ __  _   _
 | |\/| |/ _` | | '_ \  | |\/| |/ _ \ '_ \| | | |
 | |  | | (_| | | | | | | |  | |  __/ | | | |_| |
 |_|  |_|\__,_|_|_| |_| |_|  |_|\___|_| |_|\__,_|


[1] - Generating packets from random ips
[2] - Generating packets from private ips


[0] - Leave console.


""")





	op = int(input("Choose an option : "))

	if op == 0 :
		sys.exit()
	if op == 1:
		rand()
	if op == 2:
		priv()








####### RANDOM ######

def rand():
	how = int(input("How many packets you want to send ? "))
	dist = input("Choose a distant ip : ")
	i = 0
	while i < how :
		r1 = random.randint(1, 255)
		r2 = random.randint(1, 255)
		r3 = random.randint(1, 255)
		r4 = random.randint(1, 255)
		sendp(Ether()/IP(src=f"{r1}.{r2}.{r3}.{r4}", dst=f"{dist}"), iface="eth0")
		i += 1
	print("Done.")
	e = input()



####### PRIVATE ######


def priv():
	print('''
[1] - Random 192.168.X.X
[2] - Random 172.X.X.X
[3] - Random 10.X.X.X
[4] - Use specific IP
''')

	num = int(input("Choose an option : "))
	dist = input("Choose a distant ip : ")
	how = int(input("How many packets you want to send ? "))

	if num == 1 :
		print("Generating addresses...")
		i = 0
		while i < how :
			r1 = random.randint(1, 255)
			r2 = random.randint(1, 255)
			sendp(Ether()/IP(src=f"192.168.{r1}.{r2}", dst=f"{dist}"), iface="eth0")
			i += 1
		e = input()


	if num == 2 :
		print("Generating addresses ...")
		i = 0
		while i < how :
			r1 = random.randint(1, 255)
			r2 = random.randint(1, 255)
			r3 = random.randint(1, 255)
			sendp(Ether()/IP(src=f"172.{r1}.{r2}.{r3}", dst=f"{dist}"), iface="eth0")
			i += 1
		e = input()

	if num == 3 :
		print("Generating addresses ...")
		i = 0
		while i < how :
			r1 = random.randint(1, 255)
			r2 = random.randint(1, 255)
			r3 = random.randint(1, 255)
			sendp(Ether()/IP(src=f"10.{r1}.{r2}.{r3}", dst=f"{dist}"), iface="eth0")
			i += 1
		e = input()

	if num == 4 :
		ip = input("Enter an ip : ")
		i = 0
		while i < how :
			sendp(Ether()/IP(src=f"{ip}", dst=f"{dist}"), iface="eth0")
			i += 1
		e = input()


if __name__ == '__main__' :
	while 1:
		console()
