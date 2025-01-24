---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.jpg')
color: 266089
html: true

---
![bg left:50% 90%](assets/mastrogpt-logo.png)


##### Developing Open LLM applications with

<center>
<img width="90%"src="assets/openserverless-logo.png">
</center>

<center>
<img width="100%"src="assets/mastrogpt.png">
</center>


---

![bg left:50% 80%](assets/starter.png)

https://github.com/mastrogpt/
- Go to `mastrogpt-starter` 
- Launch the codespace

<img width="70%" src="assets/codespaces.png">


---

![bg right:50% 90%](assets/environment.png)

## Environment Ready

- It takes a bit to download images and start...

- Wait until you see the *OpenServerless* **Cloud** icon
  
- Click on the **Cloud** icon

- Click on **Login** and put your credentials


--- 

# Check Lesson, Deployment, Tests

- Click on **Cloud** icon then click on **Deploy**

- Click on **Documents** icon, then open the file `lessons/0-welcome.md` and click on the **Preview** icon

- Click on the **Tests** icon, then run all the tests, ensuring all the tess passes

<center>
<img width="80%" src="assets/icons.png">
</center>

---

## Development Mode

![bg right:50% 70%](assets/devmode.png)

1. Click **Cloud** icon 
1. Click **Devel** button
1. Click on **Antenna** icon
1. Click on  **World** icon
1. Login into Pinocchio with `pinocchio`/`geppetto`
1. Play a bit with the UI

---

![bg 85%](assets/pinocchio.png)

---

# Pinocchio 

![bg right:50% 80%](assets/pinocchio-form.png)

- **Chat** interface to serverless functions (called **actions**)
- **Authentication** with a `login` action
-  **Menu** configurable an `index` action
- **Upload** files in S3 storage
- Customizable **rendering** of content  (`display` action)
- **Form** support

---

## Use the Terminal

- Open the terminal: Menu >> `Terminal` >> `New Terminal`
- Use the terminal to change the password and redeploy the login

```
$ ops ai user update pinocchio
Enter your password: **********
updated /home/msciab/mastrogpt2/starter/packages/mastrogpt/login/users.json
$ ops ide deploy mastrogpt/login
<...omissis...>
ok: updated action mastrogpt/login
```
---
![bg right:50% 70%](1-setup/codespaces.png)

###  Notes on GitHub Codespaces
- Free up to 120 hours
- Recommended: **GitHub** >> **Settings** >> **Codespaces**
- Change: **Default Idle Timout** to 5 minutes
- You can also work locally:
   - wse a local **VScode** 
   - wse a local **Docker** 

---

![bg](https://fakeimg.pl/350x200/ff0000,0/0A6BAC?retina=1&text=Support)

---

![bg](assets/architecture.png)

---

![bg right:50% 70%](assets/mastrogpt-request.png)
#### How to get an account?

Free accounts by Nuvolaris on  `openserverless.dev` 
  - Ask for an account on https://mastrogpt.com
  - Contact us Linkedin, Discord, Email...

#### <!--fit--> https://linkedin.com/in/msciab

You can also self-host it, info: 

##### <!--fit--> https://openserverless.apache.org

---

# <!--fit--> Discord: `bit.ly/openserverless-discord`
<br>
<center>
<img width="80%" src="assets/discord.png">
</center>

---

# <!--fit--> Reddit: `reddit.com/r/openserverless`

<br>
<center>
<img width="80%" src="1-setup/reddit.png">
</center>


---

![bg](https://fakeimg.pl/350x200/ff0000,0/0A6BAC?retina=1&text=What+is+next?)

---
# <!--fit-->  Select a lesson to download

![bg 90%](assets/lessons.png)



