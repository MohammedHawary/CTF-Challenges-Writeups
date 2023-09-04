# HTTP - Headers

## Challenge Description

HTTP response give informations

Get an administrator access to the webpage.

Challenge Link: https://www.root-me.org/en/Challenges/Web-Server/HTTP-Headers

# Approach

First, I saw a web page containing this text.  <u>Content is not the only part of an HTTP response!</u> Let's capture this request with burp

![Screenshot from 2023-09-04 02-06-48](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/94c74640-e87b-4f95-a669-ee910e45edb0)
As we can see, the server response contains header called

 `Header-RootMe-Admin: none`

![Screenshot from 2023-09-04 02-38-21](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/0e5e2f80-2c8a-4427-9787-8182477ac000)
Let's Add this header in our GET request and change `none` to `true` and see what will happen

 `Header-RootMe-Admin: true`

![Screenshot from 2023-09-04 02-39-23](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/cf5942eb-7194-4f53-81e9-2b55fa5fde0c)
The challenge solved and we got the password

![Screenshot from 2023-09-04 02-39-41](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/f19d820b-250f-4601-af62-f3cf333511be)

# Password

**HeadersMayBeUseful**
