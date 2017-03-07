import requests
import json
import subprocess

def gotoLine1():
        subprocess.Popen(["bw_tool", "-a", "82", "-w", "11:0"])
def gotoLine2():
        subprocess.Popen(["bw_tool", "-a", "82", "-w", "11:20"])
def gotoLine3():
        subprocess.Popen(["bw_tool", "-a", "82", "-w", "11:14"])
def gotoLine4():
        subprocess.Popen(["bw_tool", "-a", "82", "-w", "11:34"])

def write(text):
        subprocess.Popen(["bw_tool", "-a", "82", "-t", text])

def clearScreen():
        subprocess.Popen(["bw_tool", "-a", "82", "-w", "10:0"])

r = requests.get("http://localhost/admin/api.php?summary")
#print r.json()

program = "bw_tool"
argument = "-a 82 -t 'aaaa'"

clearScreen()

gotoLine1()
write("Blocked today: %s" % r.json()["ads_blocked_today"])
gotoLine2()
write("Queries today: %s" % r.json()["dns_queries_today"])
gotoLine3()
write("%% blocked: %s" % r.json()["ads_percentage_today"])
gotoLine4()
write("Blocked: %s" % r.json()["domains_being_blocked"])

