Read me
=======
# eAuction
A web platform that brings traditional auctioning to a modern online system, coupled with tools that’s necessary for the auctioning process.

## Getting Started 
Follow these steps to get this project to run on you local machine for development and testing purposes. 
### Prerequisites
* [Django](https://www.djangoproject.com/) (2.0 or higher)
* [Python](https://www.python.org/downloads/) (3.4 or higher)
   You can also check the `requirements.txt` to see the list of dependencies.

### Installation
1. Clone the repository
   - `git clone https://github.com/channelfix/eAuction`
2. Move to `/eAuction` directory and enter these on the terminal
   ```
   npm install
   ```
   This command installs everything inside the file called package.json


## Running the System
### Build the JS Files
To do so, open a terminal, move to the `/eAuction` directory, and run:
```
npm run build:watch
```
You should see something like this on your terminal: 
```
Your application is running here: http://localhost:8080
Hash: 131574fce3d22a9c1c11
Version: webpack 3.11.0
Time: 175ms
                               Asset       Size  Chunks                    Chunk Names
2b508b4101069ddb6c94.hot-update.json   44 bytes          [emitted]         
                              app.js    4.33 MB       0  [emitted]  [big]  app
0.8964bee5534b387a6d3a.hot-update.js    3.64 kB       0  [emitted]         app
8964bee5534b387a6d3a.hot-update.json   43 bytes          [emitted]         
             ../templates/index.html  331 bytes          [emitted]         
[./src/assets/js/Request.js] ./src/assets/js/Request.js 837 bytes {0} [built]
    + 63 hidden modules
Child html-webpack-plugin for "../templates/index.html":
                                   Asset      Size  Chunks             Chunk Names
    2b508b4101069ddb6c94.hot-update.json  44 bytes          [emitted]  
     + 1 hidden asset
       4 modules
```

### Run the server
**In a virtual environment**, open a **NEW** terminal, move to the `/eAuction` directory where you can find the `manage.py` file.
(Note: Yes a **new** terminal relative to the previously opened terminal for builging the JS Files. It is important to run this inside a virtual environment so that this project's dependencies and packages won't interfere with your machine's packages and vice versa.)
```
python3 manage.py runserver
```

You should see something like this on your terminal:
```
System check identified no issues (0 silenced).
May 09, 2018 - 03:40:34
Django version 2.0.4, using settings 'auction.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Access the website
Open your browser and copy this URL on the address bar or [click here](http://localhost:8000/login/):
```
http://localhost:8000/login/
```

## Contribution
After making the server run, you may have some suggestions, bug fixes, etc. To have it incorporated in the system, we follow a git flow that ensures proper documentation of appends/amends in the system.

### Git flow
Assuming you've finished following the steps above, the git flow is as follows:
1. **Create a branch** from the `development` branch.
   - Branches are to be named as: <action-type>/<descriptive-task> on kebab-case (e.g. feature/authentication)
   - Action-types are as follows:
     - bugfix
     - fixture
     - chore
     - refactor
2. After finishing a task, **push request** to `development` branch
3. This will then be reviewed, and would be pushed to the `master` branch
