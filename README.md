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

### Attention

* **⚠See the documentation folder `Document` for detailed specifications.⚠**
* **Currently under refactoring.....**

---

It is an application that displays the songs in the playlist registered in Youtube that have disappeared.
In principle, this is an application to be used by registered users
Some functions can be used without user registration

![img](src/st_server/public/streamlit1/img/linkedin_banner_image_1.png)

## URL

---

* http://www.youtube-diff-checker.com:8503/
  * SSL conversion to be done at a later date

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
* SQLAlchemy 1.4
* Docker
* MySQL
* Streamlit
* Nginx
* YoutubeAPI
* VPS
* GithubActions

### System overview

![img](src/st_server/public/streamlit1/img/sample.png)

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
