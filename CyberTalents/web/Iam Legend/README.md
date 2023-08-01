# Iam Legend

### Challenge Description

Challenge Link: http://wcamxwl32pue3e6mxwl32epheze6ndvje7r4be3y-web.cybertalentslabs.com

If I am a legend, then why am I so lonely?

Flag Format : FLAG{}

# Approach

Firstly, I saw the login page and tried to log in with some default web credentials, but it didn't work.

![Screenshot from 2023-08-01 12-30-15](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/d2927c11-29ea-4ad4-9dda-245fbb88f1f6)

Let's Try To show the Page source Code

I saw the strange javascript code

![Screenshot from 2023-08-01 12-31-10](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/d5e4a7d5-9844-4a98-a202-29f6e3dcfed0)

Let's use chatGTP to know what is this js code 

![GPT](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/8628aba5-d13b-4e75-9962-e1f8bcc41185)

He said that is the JavaScript technique called JS obfuscation where code is written using non-alphanumeric characters to make it more difficult to read and understand.

After I search about tool to decrypt this code i found tool called [poisonjs]([GitHub - filipemgs/poisonjs: PoisonJS - De-obfuscate eval-based JavaScript obfuscation with monkey-patched eval(-like) functions.](https://github.com/filipemgs/poisonjs)) on GitHub 

![Screenshot from 2023-08-01 12-53-22](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/b6f8dd55-b7a3-4d47-884f-8ede100b1cdb)

After Copy it and use [Beautify JavaScript](https://beautifier.io/) to make this js code Beautifull to read

We get the `username = Cyber` and `password = Talent` and we get the flag also

![Screenshot from 2023-08-01 12-57-28](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/12836dec-9a34-4d50-a7c8-ceb34d3de482)

![Screenshot from 2023-08-01 12-58-05](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/e09fe4e7-4e49-4db2-8b3c-a12076a5c2ec)

# Flag

**flag{J4V4_Scr1Pt_1S_S0_D4MN_FUN}**
