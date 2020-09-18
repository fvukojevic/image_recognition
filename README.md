# Image Recognition

This is a simple app that takes the image url from the internet and using
**TensorFlow** inception trained model tries to recognize image and what's on it

The app works best with simple things. Animals, fruits, etc. Also the more things
on the image, the harder it is to recognize what's on it. So having a clear image
with white background would usually get a better result.

The app can not recognize things like famous people, club logos, etc. The 
model I am using is not that advanced and it is public on TensorFlow website

## Project Screenshots

### Example 1

![alt text](https://github.com/fvukojevic/image_recognition/blob/master/project_imgs/example.png?raw=true)

### Example 2

![alt text](https://github.com/fvukojevic/image_recognition/blob/master/project_imgs/example2.png?raw=true)

## Project setup

This app is very easy to install. It is using dockers so they are a prerequisite

Docker for MAC: 
- Install docker [Link](https://docs.docker.com/docker-for-mac/install/) 

Docker for Windows:
- Install docker for Windows [Link]([https://hub.docker.com/editions/community/docker-ce-desktop-windows/]) 

After you successfully downloaded docker click on the whale icon, open Preferences, 
Resources, File Sharing. With + button add project folder to Docker Resource, and press 
Apply & Restart. 

(I am on Mac so if this process is slightly different on Windows/Linux I apologies)

After that go inside your project inside terminal and simply run these two commands:

```
    docker-compose build 
    docker-compose up
```

For clarification, build will create images and up will run them, but this isn't really a 
docker guide.


## Reflection

The reason I decided to create this project is because I was investigating Flask in Python.
I already created few api's and I wanted to demonstrate a very simple app that connects to Flask API
and then shows some data in browser.

App is very simple and only created for fun.
