# Encrypted Database

## Challenge Description

Challenge Link: http://wcamxwl32pue3e6mxmdvww5c1v58ndvje7r4be3y-web.cybertalentslabs.com

The company hired an inexperienced developer,

# Approach

Firstly, I saw this page and from page 

![Screenshot from 2023-08-04 22-27-48](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/030a66ee-67bd-475b-b4c6-3b286eadd11b)

and from source code i find the /admin path 

![Screenshot from 2023-08-04 22-31-32](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/0b058cb9-240c-456a-b86d-72432524f546)

or using `dirsearch` to fuzzing directory

![Screenshot from 2023-08-04 22-32-23](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/cecfde5b-f99a-43a7-920b-0909d1240134)

let's show `/admin/index.php`

![Screenshot from 2023-08-04 22-33-32](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/9160b900-e89f-4f52-84f7-d156eae65b2e)

It's Login page ,I tried show defualt credintial but dosen't work ,Let's show source code of this page

![Screenshot from 2023-08-04 22-35-20](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/078f77c4-76ed-4b22-8012-a01cb968e31a)

I find the hidden input field called `db` and has a value `secret-database/db.json` ,Let's show this file and the new path will be `/admin/secret-database/db.json`

![Screenshot from 2023-08-04 22-38-26](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/409c22e4-1686-4dfa-962e-c4d5c613d8ee)

We get the flag but it's encrypted, so let's try decrypt it on [crackstation](https://crackstation.net/)

![Screenshot from 2023-08-04 22-42-26](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/7442f9d0-db20-4f92-9274-1b6e509529b1)

Finally we got the flag

# Flag

**badboy**
