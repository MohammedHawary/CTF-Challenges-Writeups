# HTTP - IP restriction bypass

## Challenge Description

Only local users will be able to access the page

Challenge Link: https://www.root-me.org/en/Challenges/Web-Server/HTTP-IP-restriction-bypass

## Statement

Dear colleagues,

We’re now managing connections to the intranet using private IP addresses, so it’s no longer necessary to login with a username / password when you are already connected to the internal company network.

Regards,

The network admin

## Approach

From Statement and Challenge Name the Aurther want from us join to the local Network access this page without UuserName and password 

![Screenshot from 2023-08-01 20-05-20](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/a96e3539-7a16-4185-af19-b3196c2031b1)

and he print our IP then I searched about Header to know IP 

![Screenshot from 2023-08-01 20-07-02](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/7c96bbaa-f072-458f-82da-a05e955edb83)

And I search about local network IPs range

![Screenshot from 2023-08-01 20-08-09](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/65297e53-80da-4c9d-9f2a-bb5a5f827c82)

Choose any IP address in any range of any local network

Then I Added the header with local IP `X-Forwarded-For: 10.0.0.1`

and i get the Password

![Screenshot from 2023-08-01 20-11-15](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/a75c98a0-f641-4cad-a1ed-90c6df8c76aa)

# Password

**Ip_$po0Fing**
