# Youtube Diff Checker

<!-- [![LICENSE](https://img.shields.io/github/license/maro114510/Production_WebApp.svg?style=flat-square)](https://github.com/maro114510/Production_WebApp/blob/main/LICENSE)-->

[![Docker Pulls](https://img.shields.io/docker/pulls/stelzen/youtube.svg?style=flat-square&logo=docker)](https://hub.docker.com/r/stelzen/youtube)
![](https://img.shields.io/github/issues/maro114510/Production_Webapp)
![](https://img.shields.io/github/issues-pr/maro114510/Production_Webapp)
![](https://img.shields.io/github/languages/code-size/maro114510/Production_Webapp)
![](https://img.shields.io/docker/image-size/stelzen/youtube)
![](https://img.shields.io/github/directory-file-count/maro114510/Production_Webapp)
<!-- [![Build Status](https://img.shields.io/github/workflow/status/maro114510/Production_WebApp/Build?logo=github&style=flat-square)](https://github.com/maro114510/Production_WebApp/actions) -->


---

It is an application that displays the songs in the playlist registered in Youtube that have disappeared.
In principle, this is an application to be used by registered users
Some functions can be used without user registration

## URL

---

* The site closed on January 16, 2023.

---

<!-- ### Usage

| Img | Usage |
| :---: | :---: |
| <img src="src/st_server/public/streamlit1/img/sample2.png" width="500"> | home |
|  <img src="src/st_server/public/streamlit1/img/sample1.png" width="500"> | User login |
|  <img src="src/st_server/public/streamlit1/img/sample3.png" width="500"> | User register |
|  <img src="src/st_server/public/streamlit1/img/sample4.png" width="500"> | Your Playlist Info | -->

### Usage Technology and Library

* Python 3.9
* FastAPI 0.85
* uvicorn
* Docker
* Streamlit
* Nginx
* YoutubeAPI
* VPS
* GithubActions

### System overview

![](https://storage.googleapis.com/zenn-user-upload/84bf99affa2c-20230114.png)

### GithubActions

* The lint test is executed when you push to the main branch on Github.
* This is done when a pull request for the main branch has been approved.

### List of Functions

* User registration and login Functions
* Playlist registration Function
* Deleted video display Function
* Automatic Notification Function
* Automatic collection Function

#### Test

* Unit test
  * by pytest

---
