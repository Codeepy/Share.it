# SHARE.IT

The World's First Crowd-Fooding Platform!

http://dumbastic.koding.io/

[![Koding Hackathon](https://raw.githubusercontent.com/Codeepy/hackathon.submit/master/images/badge.png "Koding Hackathon")](https://koding.com/Hackathon)

## Description

**"FOOD FOR EVERYONE"**
* Every day about 21,000 people die of hunger or hunger-related causes
* Every year approximately one third of the food produced in the world, which weighs around 1.3 billion tonnes, are either wasted or get lost
* Poor nutrition causes nearly 45% of deaths in children under five and approximately 3.1 million children die each year
* Around 805 million people in the world do not have adequate food to lead a healthy life
* Every year approximately one third of the food produced in the world, which weighs around 1.3 billion tonnes and costs $165 billion (including production cost) approximately, are either wasted or gets lost

**What is Share.it and it's use?**
<br>
Share.it is a web application, which enables any person to engage and lead the "Food For Everyone" movement. <br>Using Share.it you can:
* Share food or leftovers with people who may need them
* Find the nearest food banks and get directions to them
* Find other volunteers just like you and collaborate with them to lead your own movement
* Collaborate with food banks to support and create the awareness
* You can also request for any food from volunteers and food banks if you need so....

All the things which you can do in Share.it, make it the world's first true Crowd-Fooding platform!

## Screenshots

We are using NginX web server to serve Share.it web application. The back-end system is based-on Django web framework with SQLite database.

![git](http://i.imgur.com/vdSYlz5.png "git")
Development process with git


![nginx](http://i.imgur.com/YgT10Q1.png "nginx")
Nginx running on Koding VM


![Homepage](http://i.imgur.com/jruVXP5.png "Homepage")
Share.it homepage


## APIs used

API | URL | Description
--- | --- | ---
Google Map Javascript API | https://developers.google.com/maps/documentation/javascript/ | We use this API to display Food Banks, Volunteers, and Food Broadcast's locations
PubNub | http://www.pubnub.com/developers/ | We use this API to provide real-time chat and food broadcast
JustGiving <br>(from 3Scale) | https://apimanagement.justgiving.com/ | We use this API to provide donation payment service
Disqus <br>(from APItools) | https://www.apitools.com/apis/disqus | We use this API to facilitate commenting in Contact page
Share.It <br>(deployed in Mashape) | https://www.mashape.com/codeepy/share-it | We developed this API to serve and retrieve the Volunteers' locations
NutritionIx | http://www.nutritionix.com/api | We used this API to provide nutritional information for shared foods
