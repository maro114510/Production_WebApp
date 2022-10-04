# Youtube Diff Checker

---

It is an application that displays the songs in the playlist registered in Youtube that have disappeared.
In principle, this is an application to be used by registered users
Some functions can be used without user registration

![img](src/st_server/public/streamlit1/img/linkedin_banner_image_1.png)

## URL

---

* https://

---

### Usage

| Img | Usage |
| :---: | :---: |
| <img src="src/st_server/public/streamlit1/img/sample2.png" width="500"> | home |
|  <img src="src/st_server/public/streamlit1/img/sample1.png" width="500"> | User login |
|  <img src="src/st_server/public/streamlit1/img/sample3.png" width="500"> | User register |
|  <img src="src/st_server/public/streamlit1/img/sample4.png" width="500"> | Your Playlist Info |

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