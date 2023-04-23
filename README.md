# Mastodon Social Graphs
## Creating a social graph for mastodon instances
This repository contains code that allows you to create social graphs for mastodon instances such as this one:
<img width="691" alt="Снимок экрана 2023-04-23 в 23 46 36" src="https://user-images.githubusercontent.com/91324982/233857558-e86fc742-f562-4613-aec5-2ba3a5235d22.png">

# Step 0: Setting Up
First you need to clone this repository on your computer.

Also to download all the necessary libraries for your Python environment, run:
```
pip install -r requirements.txt
```
> You may want to create a separate virtual environment for that.

# Step 1: Create an application
Also, in order to use the API for Mastodon servers, you first need to register and then create an application for working with the API.
Once you have registered on one of the servers. Find the app.py file in the scripts folder and fill in the relevant data such as the name of your application (can be anything), a link to the server and the file where your key will be saved. Then run: 
```
python scripts/app.py
```
> Application should be created once.

# Step 2: Creating a graph

Now you need to go to the scripts/main.py file and change the data that I indicated at the very beginning to those that advise you (mail, password, etc.).
Finally to generate the graph, call:
```
python scripts/main.py
```

# Step 3: Enjoy!
After completing the step 2, you should get three types of files: a matrix representation of the graph (plot.png), a table with connections, and finally an html file that will contain a beautiful representation of your graph.

# Limitations
Since I was not the instance admin, I could not get a list of all server members at once. Therefore, I used a depth-first graph traversal algorithm to collect all users, which is very slow for servers with a large number of people. However, if you are an admin or have found a way to quickly get the names of all users, then this will reduce the time and allow you to get large graph sizes.
