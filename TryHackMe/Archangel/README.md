# Archangel

Challenge Link: [TryHackMe | Archangel](https://tryhackme.com/room/archangel)

### Task1 : Deploy Machine

1. Connect to openvpn and deploy the machine 
   
       No answer needed

### Task 2 : Get a shell

1. Find a different hostname 
   
   After Nmap there are webserver work on port `80`
   
   ![Screenshot from 2023-09-28 11-24-00](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/864956a1-3ba4-460b-beeb-c5d14e727308)
   
   After access this webserver the hostname is
   
   ![Screenshot from 2023-09-28 11-33-46](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/a4573e28-35d7-473e-9368-be7401a089cb)
   
       mafialive.thm

2. Find flag 1 
   
   Add this host with his IP in `/etc/hosts`
   
   ![Screenshot from 2023-09-28 12-40-21](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/1955bfe4-ee5d-4360-80e1-32f4d9f98088)
   
   And access this website with this domain
   
   ![Screenshot from 2023-09-28 13-32-32](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/440e1063-b709-4ecd-985c-a26d2a5099ba)
   
       thm{f0und_th3_r1ght_h0st_n4m3}

3. Look for a page under development
   
   Fuzzing this website
   
   ![Screenshot from 2023-09-28 13-27-15](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/191f41d1-b721-4a29-82ff-82b5595029e1)
   
   Access `robots.txt`
   
   ![Screenshot from 2023-09-28 13-33-02](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/beff2560-272a-4ec7-a128-7e64c5d114a2)
   
   ```
   test.php
   ```

4. Find flag 2
   
   There are page called `test.php` and in this page there are button after press it there are parameter called `view` and it's take path `/var/www/html/development_testing/mrrobot.php` to display it
   
   ![Screenshot from 20230928 133347](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/c341c4fc-c134-4447-8519-fcfba84fac37)
   
   With this `LFI` payload can i access files in server like `/etc/passwd` with this payload : `/var/www/html/development_testing/..//..//..//..//etc/passwd`
   
   ![Screenshot from 20230928 135650](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/706a8478-194c-43e7-a415-f623bac9abc9)
   
   Let's try to access `access.log` file, This file recording data for all requests processed by the Apache server
   
   ![Screenshot from 20230928 135906](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/ac753160-12e6-4e02-bf80-fe79e98253d5)
   
   We can access it, Then let's send our payload in `User-Agent` header and send it to server
   
   ![Screenshot from 20230928 140224](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/0d53f80f-12e0-4300-a6db-c77be9ceed2e)
   
   Then add in the last of our payload this parameter with command to run on server `&c=id`
   
   ![Screenshot from 20230928 140434](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/a1c09ba2-eda8-49e4-99dd-9be87f052bf3)
   
   Command work
   
   ![Screenshot from 20230928 140516](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/4cc43ba5-f06c-40f4-8c78-97842f65ad1f)
   
   Then let's gain RCE from LFI
   
   ![Screenshot from 20230928 145004](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/7c0b3dea-6a6f-4667-adea-97cd5d0ed742)
   
   And do url encoding for this payload
   
   ![Screenshot from 20230928 145043](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/24ae5e69-b95c-4101-8c71-c10f648af60f)
   
   Then let try to gain RCE
   
   ![Screenshot from 20230928 145147](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/b8ce57d4-22ee-4d96-bcac-28ac36030f32)
   
   It's work
   
   ![Screenshot from 20230928 145209](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/c2ae1df0-5d23-43e8-b57a-2228d05b1f3a)
   
   Then search in `test.php` about flag
   
   ![Screenshot from 2023-09-28 15-01-34](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/d222f120-74fa-45a2-811a-d660863218ea)
   
       thm{explo1t1ng_lf1}

5. Get a shell and find the user flag
   
   ![Screenshot from 2023-09-28 14-54-15](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/5a33bb75-9411-47d6-8cfe-26513ea9bac8)
   
       thm{lf1_t0_rc3_1s_tr1cky}

### Task 3 : Root the machine

1. Get User 2 flag  
   
   Get `linpeas.sh` in `/tmp` and add `+x` and run it
   
   ![Screenshot from 2023-09-28 15-32-10](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/39c2339f-8b44-41e5-998a-d1ef4a3b8fb4)
   
   There are file in `/opt/helloworld.sh` run every minuite with `archangel` permtion and we can write on it
   
   ![Screenshot from 2023-09-28 15-33-44](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/36a98605-5dee-4e9e-8b02-9dc2abebdbae)
   
   let's try to test it
   
   ![Screenshot from 2023-09-28 15-34-31](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/d55ddbc4-8514-4b01-8138-d1ee42d1acc6)
   
   it's work
   
   ![Screenshot from 2023-09-28 15-35-40](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/fde2c503-a740-475b-b5a5-785c74e03a83)
   
   Then let's make `secret` directory accessable for everyone
   
   ![Screenshot from 2023-09-28 15-35-25](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/2ac9787c-8de5-47a4-bc74-ae8418b92071)
   
   Done
   
   ![Screenshot from 2023-09-28 15-37-04](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/9194b94c-6741-490c-9c25-431a7d9d4e33)
   
   ![Screenshot from 2023-09-28 15-37-42](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/dad172b9-3c16-4e18-ba97-033fb5da0dac)
   
       thm{h0r1zont4l_pr1v1l3g3_2sc4ll4t10n_us1ng_cr0n}

2. Root the machine and find the root flag
   
   there are `backup` file we can run it as a root
   
   ![Screenshot from 20230928 155005](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/fe42855a-6a1c-4f51-9e0b-818201020081)
   
   ![Screenshot from 20230928 155016](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/eb3898c3-670c-4cb7-970d-5e6b15866550)
   
   ![Screenshot from 20230928 155031](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/9319e158-2be4-4880-8f15-ae0806d4adba)
   
   ![Screenshot from 2023-09-28 15-52-36](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/6a99fef5-cdb4-42b9-bcf8-8363f818fecb)
   
       thm{p4th_v4r1abl3_expl01tat1ion_f0r_v3rt1c4l_pr1v1l3g3_3sc4ll4t10n}

![Screenshot from 2023-09-28 15-52-53](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/ddcf787c-871d-4394-bb93-2f96675450c9)

![Screenshot from 2023-09-28 16-02-00](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/653b2550-803f-4a31-9de2-940eb3021836)
![Screenshot from 2023-09-28 16-09-00](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/ab14ec57-dbba-40c1-8a9e-148e67be037a)
![Screenshot from 2023-09-28 16-12-03](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/fc377f0b-ea8c-4d05-9c32-4e423c6fc3fa)
![Screenshot from 2023-09-28 16-12-52](https://github.com/MohammedHawary/Web-Penetration/assets/94152045/e549b578-dc87-4ed4-b0bb-f4d4c7f41881)
