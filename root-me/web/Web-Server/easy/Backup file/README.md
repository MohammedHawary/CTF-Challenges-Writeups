# Backup file

## Challenge Description

No clue.

Challenge Link: http://challenge01.root-me.org/web-serveur/ch11/

# Approach

First, I saw login page and i tried to login with some default credentials but not worked

![Screenshot from 2023-08-31 06-43-53](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/73b1745e-0d03-42c6-8fff-016beaeabb29)

I tried to FUZZ web pages and i found the `/index.php~`

![Screenshot from 2023-08-31 06-52-59](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/3cfbdb38-ec14-441d-88bd-66bf3f447b8b)
after write this file name it's download the php source code file

![Screenshot from 2023-08-31 06-53-24](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/fef49669-6a06-4eb3-8e78-f7365d6a19f0)
after cat the content of this file you can see the username and password i loged in with it and login successfully

![Screenshot from 2023-08-31 06-53-47](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/564b9a3f-fc23-4061-8a6f-77a3ce93c4d7)

![Screenshot from 2023-08-31 06-54-06](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/c2e8775d-b579-4a9d-be91-3e86d4091a3b)

# Password

**OCCY9AcNm1tj**
