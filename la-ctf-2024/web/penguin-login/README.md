## web/penguin-login

I got tired of people leaking my password from the db so I moved it out of the db. 
[penguin.chall.lac.tf](https://penguin.chall.lac.tf/)

### Solution
> Explanation from https://github.com/uclaacm/lactf-archive/blob/main/2024/web/penguin-login/solve.py

Looking at the app, it allows a sqli using any printable character except for ()%.
It also prevents us from using the word `like` in any case.
Our task is to exfiltrate the value of the `name` column for the flag entry.

The classic way to do this is to inject something along lines of
name LIKE 'prefix%' (which matches against all entries
                     starting with prefix as % is a wildcard)

However, LIKE is banned, so we must find something else.
() is banned so we cannot resort to using clever sql functions.

We notice that our database is postgresql which has special pattern matching
not found in other sql dbs: the SIMILAR TO keyword which behaves like LIKE
(see https://www.postgresql.org/docs/current/functions-matching.html)

Now that we have a pattern matching, we are ready to build our prefix
and get the flag!

We have to first get the length of the flag by brute forcing the amount of _
as none of the full wildcard options are available.

After that, we exfiltrate the flag.
