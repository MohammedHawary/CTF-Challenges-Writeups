# Admin has the power

### Challenge Description

Challenge Link:[http://wcamxwl32pue3e6m5p6v4ehxzg1rndvje7r4be3y-web.cybertalentslabs.com](http://wcamxwl32pue3e6m5p6v4ehxzg1rndvje7r4be3y-web.cybertalentslabs.com/)

 Administrators only has the power to see the flag, can you be one ?

## Approach

Firstly, I saw the login page and tried to log in with some default web credentials, but it didn't work.

![Screenshot from 2023-08-01 10-52-53](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/96b71b8a-d671-4543-9577-513fa9464a09)

Let's Try To show the Page source Code

I saw the comment with Credential (user:support password:x34245323)

![Screenshot from 2023-08-01 10-53-08](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/8e0bb412-c872-40f7-a900-57fc299acf98)

I logged in with this credential and I saw the message told me that you're a supporter and you need better privileges

![Screenshot from 2023-08-01 10-53-21](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/6a09b137-9734-475e-a885-f3f159541a2f)

Then I show if there are a cookie or note

I found the cookie `role=support` I changed it to `role=admin` and refresh the page

then I get the flag

![Screenshot from 2023-08-01 10-56-24](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/2cb9c2e9-2194-4dee-8a93-e09177ea121a)

## Flag

**hiadminyouhavethepower**
