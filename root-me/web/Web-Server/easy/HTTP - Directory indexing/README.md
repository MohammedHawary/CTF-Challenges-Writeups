# HTTP - Directory indexing

## Challenge Description

CTRL+U...

challnge Link: https://www.root-me.org/en/Challenges/Web-Server/HTTP-Directory-indexing

## Approach

First, I saw empty page, Let saw the page source![Screenshot from 2023-09-02 18-31-33](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/bce18f02-715b-4809-abfc-ab5033b42645)
There are HTML comment includes the `admin/pass.html` path

![Screenshot from 2023-09-02 18-41-35](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/097dbb99-648a-42c1-af6e-ccdfbc294057)

Let's access this path

![Screenshot from 2023-09-02 18-44-15](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/2a41d983-201e-4919-b8a9-3d27dd889a53)

Let's translate this lang

![Screenshot from 2023-09-02 18-37-40](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/fabfb557-bd0b-4113-964f-d5d1f100b021)

After translating this language, we were told that this is not the last `/` just search then let's use `dirsearch` for FUZZ content and hidden pages

![Screenshot from 2023-09-02 18-37-08](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/43318ab1-314c-4a8b-b098-045719576ee1)

There are directory called `/admin`  let's access it

![Screenshot from 2023-09-02 18-36-50](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/42f0cef4-f57f-43f6-9b6e-ce6ca454bfbd)

After accessing `/admin`, there is a `/backup` directory and the previous html file whose content we have translated, then let's access the `/backup` directory

![Screenshot from 2023-09-02 18-36-20](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/e7af3ac5-6782-4699-9aa3-b1902a752f09)
There are file called `admin.txt` lets access it

![Screenshot from 2023-09-02 18-36-34](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/e69025ee-a1ba-4550-8c38-9ec3b060ff75)
And I found the password of this challenge
![Screenshot from 2023-09-02 18-38-48](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/5e069d38-c201-4e41-82c9-3d750261d52d)

# Password

**LINUX**
