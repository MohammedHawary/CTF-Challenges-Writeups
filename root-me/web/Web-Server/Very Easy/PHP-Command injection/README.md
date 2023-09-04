# PHP - Command injection

## Challenge Description

Ping service v1

challenge Link: https://www.root-me.org/en/Challenges/Web-Server/PHP-Command-injection

## Statement

Find a vulnerabilty in this service and exploit it.

The flag is on the index.php file.

# Approach

First I saw the page contain the ping services

![Screenshot from 2023-08-03 14-50-10](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/d46fd258-b6a4-4b53-af67-a0125a6bdc61)

It's may be vulnerable with OS Injection let's try this command `;ls`

![Screenshot from 2023-08-03 14-51-42](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/6eeae2ad-c979-49de-b22a-ce9522609cee)

Good that it really contains an OS Injection ,If You cat the `index.php` file the php code will be executed but we need to read the php code 

![Screenshot from 2023-08-03 14-52-39](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/a688dbf9-5d52-4525-9721-3fa40f36fa92)

Let's cat this file and turn the code to base64 encoding using this command

`;cat index.php|base64`

![Screenshot from 2023-08-03 14-55-35](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/79eb907a-279b-41c5-87cd-cad0053a7f05)

Let's Decode it and show the php code

![Screenshot from 2023-08-03 14-56-59](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/8dc77a87-f1f5-4902-a266-76d7c90dbe7a)

From php code the flag stored in a hidden file called `.passwd` Let's cat it with this command `;cat .passwd`

![Screenshot from 2023-08-03 14-58-55](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/82b358a7-20da-43ed-b369-b4224091abc5)

and Finally we get the challenge password

# Password

**S3rv1ceP1n9Sup3rS3cure**
