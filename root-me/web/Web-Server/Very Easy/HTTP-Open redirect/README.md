# HTTP - Open redirect

### Challenge Description

Internet is so big

Challenge Link: [HTTP - Open redirect (root-me.org)](http://challenge01.root-me.org/web-serveur/ch52/)

## Statement

Find a way to make a redirection to a domain other than those showed on the web page.

# Approach

First I saw the page has some social media links, if you press any button from this page it will redirect you to another website![Screenshot from 2023-08-02 10-22-00](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/fce801f0-7e6d-49ee-a056-2c9089acb282)

let's try to capture this with burpsuite![Screenshot from 2023-08-02 10-27-58](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/7949a621-2eb4-4ee5-98c5-1addeb94c9be)

I saw the two parameter, first parameter called `url` and second parameter called `h`

I think that the `h` parameter is short for `hash` let's try to know the hash type and decrypt this hash

 [crackstation](https://crackstation.net/)

![Screenshot from 2023-08-02 10-39-35](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/29bbd16e-8058-4932-8822-0cbc961264d9)

The website didn't know the hash type or hash value, let's try to know the hash type in another website 

[Hash Type Identifier](https://hashes.com/en/tools/hash_identifier)

![Screenshot from 2023-08-02 10-41-23](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/607b5003-310f-45b1-a7ec-6daf70eaa090)

the type of hash is MD5 hash, I think that the `h` parameter is the hash of `url` parameter let's check if this guess correct or not

[md5 Hash Generator](https://www.miraclesalad.com/webtools/md5.php)

![Screenshot from 2023-08-02 10-48-49](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/ffe5a84d-10e2-49a1-881f-e47d5de6381b)

Just like we expected, let's add any `url` and any md5 hash of this `url` in the `h` parameter

![Screenshot from 2023-08-02 10-52-29](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/9feadcc4-21c1-46c2-a788-e0e4e0275f9a)

Let's adding this changes in the request![Screenshot from 2023-08-02 10-53-57](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/ba8243d3-7d90-44f0-933d-d63964b27ed7)

and finally we captured the flag

# Flag

**e6f8a530811d5a479812d7b82fc1a5c5**
