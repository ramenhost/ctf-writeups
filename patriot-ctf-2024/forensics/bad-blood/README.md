## forensics/bad-blood

Nothing is more dangerous than a bad guy that used to be a good guy. Something's going on... please talk with our incident response team.  
`nc chal.competitivecyber.club 10001`

**Given:** `suspicious.evtx`

## Solution

We can open the `suspicious.evtx` file in `Event Viewer` and look for the event logs. The event logs contain the answers to the questions asked by the challenge. We can answer the questions and get the flag.

The first three answers are directly found in the event logs. The fourth answer is found by analyzing the `Invoke-UrbanBishop.ps1` script in VirusTotal.

Answers:
```
Invoke-P0wnedshell.ps1
Invoke-UrbanBishop.ps1
WinRM
Covenant
```

## Flag
```
ramenhost@ctf:~$ nc chal.competitivecyber.club 10001
Welcome analyst.
We recently had to terminate an employee due to a department-cut.
One of our most dramatic terminations was that of a C-suite executive, Jack Stoneturf.
We believe he may have maliciously infected his workstation to maintain persistence on the corporate network.
Please view the provided event logs and help us conduct our investigation.


Answer the following questions for the flag:
Q1. Forensics found post exploitation activity present on system, network and security event logs. What post-exploitation script did the attacker run to conduct this activity?
        Example answer: PowerView.ps1
>> Invoke-P0wnedshell.ps1
That makes sense.

Q2. Forensics could not find any malicious processes on the system. However, network traffic indicates a callback was still made from his system to a device outside the network. We believe jack used process injection to facilitate this. What script helped him accomplish this?
        Example answer: Inject.ps1
>> Invoke-UrbanBishop.ps1
That makes sense.

Q3. We believe Jack attempted to establish multiple methods of persistence. What windows protocol did Jack attempt to abuse to create persistence?
        Example answer: ProtoName
>> WinRM
That makes sense.

Q4. Network evidence suggest Jack established connection to a C2 server. What C2 framework is jack using?
        Example answer: C2Name
>> Covenant
That makes sense.

That'll do. Thanks for your help, here's a flag for your troubles.
pctf{3v3nt_l0gs_reve4l_al1_a981eb}
```
