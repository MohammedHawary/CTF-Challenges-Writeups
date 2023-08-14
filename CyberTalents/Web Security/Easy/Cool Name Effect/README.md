# Cool Name Effect

## Challenge Description

Challenge Link: http://wcamxwl32pue3e6mj0wz0mehw3oendvje7r4be3y-web.cybertalentslabs.com

Webmaster developed a simple script to do cool effects on your name, but his code not filtering the inputs correctly execute javascript alert and prove it.

# Approach

First, show that the input field takes the name and re-displays it after adding effects to your name using JavaScript

![Screenshot from 2023-08-04 21-29-30](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/9a787244-a81a-4694-b32f-d77b75968e62)

Let's try some XSS payload 

```js
<script>alert(1)</script>
```

![Screenshot from 2023-08-04 21-42-53](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/fb141401-16c6-43af-8004-be507df5b9b9)

let's use XSS cheat sheet and fuzzing parameter `name`

[XSS Vectors Cheat Sheet · GitHub](https://gist.github.com/kurobeats/9a613c9ab68914312cbb415134795b45)

![Screenshot from 2023-08-04 21-46-30](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/450769f1-8f54-46e0-9ad5-ca09f916e977)

let's add this payloads in burp intruder and adding `forbiden` word in `Grep - Match` field in burpsuite and start attack and choose any payload the grep mached didn't give it number Like: `"><h1><IFRAME SRC=# onmouseover="alert(document.cookie)"></IFRAME>123</h1>` 

![Screenshot from 2023-08-04 21-53-43](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/3dd27f53-c770-4711-939c-c99531cbe236)

Right click and show response in browser

![Screenshot from 2023-08-04 21-52-02](https://github.com/MohammedHawary/CTF-Challenges-Writeups/assets/94152045/93b65931-eac9-4d14-a9da-87f66331dcbf)

Finally we got the flag

# Flag

**ciyypjz**

# 
