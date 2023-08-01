# Admin has the power

### Challenge Description

Challenge Link:[http://wcamxwl32pue3e6m5p6v4ehxzg1rndvje7r4be3y-web.cybertalentslabs.com](http://wcamxwl32pue3e6m5p6v4ehxzg1rndvje7r4be3y-web.cybertalentslabs.com/)

 Administrators only has the power to see the flag, can you be one ?

## Approach

Firstly, I saw the login page and tried to log in with some default web credentials, but it didn't work.

IMG her

Let's Try To show the Page source Code

I saw the comment with Credential (user:support password:x34245323)

IMG her

I logged in with this credential and I saw the message told me that you're a supporter and you need better privileges

IMG her

Then I show if there are a cookie or note

I found the cookie `role=support` I changed it to `role=admin` and refresh the page

then I get the flag

IMG her

## Flag

**hiadminyouhavethepower**
