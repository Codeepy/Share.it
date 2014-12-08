# SHARE.IT

The World's First Crowd-Fooding Platform!

http://dumbastic.koding.io/

[![Koding Hackathon](https://raw.githubusercontent.com/Codeepy/hackathon.submit/master/images/badge.png "Koding Hackathon")](https://koding.com/Hackathon)

## Description
This is a web-app named, "SHARE.IT", which is designed to be world's first Crowd-fooding social platform. Is 'Crowd-fooding' unknown to you? Well, it is a new term used by our team, Codeepy, in order to deal with the challenges of food waste and food scarcity in developing countries.
Share.it is the true Crowd-fooding platform which enables any person (termed as 'Volunteer' in the app) to collaborate with any other person (other volunteers) and food banks to lead the movement of "Food For Everyone".
Using Share.it you can share food (any food even your good leftovers) with people who might need it or share food with other volunteers, who may know people in need of food. The app just does not enable you to share but also allow you to seek food near your location if you need any.
The whole idea behind the app is to create awareness of food waste and its consequence, and provide a novel solution to reduce the food waste by creating simple socialising concept.

**MOTO: "FOOD FOR EVERYONE"**
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
* Collaborate with food banks to support and spread the awareness through the built-in 'Share.it Network'
* You can also request for any food from volunteers and food banks if you need so....

All the things which you can do in Share.it, make it the world's first true Crowd-Fooding platform!

## Screenshots
**Different Features of Share.it**
<br>
![Homepage](http://i.imgur.com/jruVXP5.png "Homepage")
Share.it Homepage

![About](http://i.imgur.com/TuDynUo.png "About")
Share.it About

![Share.it Network](http://i.imgur.com/2YRn5Am.png "Share.it Network")
Bird's view of 'Share.it Network', which is the main feature of the app and enables the user (volunteers &/ food banks) to collaborate and share food

![Share.it Network in Action](http://i.imgur.com/cIgIjnH.png "Share.it Network in Action")
Shows the Share.it network in action where a user (volunteer) can share his/her food with a neighbouring volunteer or food bank...

![More pictures of Share.it Network](http://i.imgur.com/Xffo0Ax.png "More pictures of Share.it Network")
More picture of the features of Share.it Network

![Direction to Food Bank or Volunteer](http://i.imgur.com/iQZWGLh.png "Direction to Food Bank or Volunteer")
The pic shows the feature where the user can see the directions to the nearest/chosen food bank or volunteer with whom he/she wants to share.it

![All Volunteers and Food Banks together](http://i.imgur.com/BRtEOZ8.png "All Volunteers and Food Banks together")
Pic shows the volunteers, food banks and other activities related to Share.it, which are near to you, on the map of Share.it Network

![Getting the nutritional values](http://i.imgur.com/cukxaLG.png "Getting the nutritional values")
This pic shows the feature where the user can check the nutritional benefits/values of the food, which they are sharing or which they want to get

![BuyIn & Donation Page](http://i.imgur.com/xW1UwLL.png "BuyIn & Donation Page")
This pic shows the feature BuyIn & Donation, which actually enables the user to buy different featured products or services (this is open for future possibilities) or can donate an amount of money.
75% of all the revenue generated from this activity will be provided or used to support 'Soup Run' activities in different cities in order to help the needy and homeless.

![User Profile Info](http://i.imgur.com/K3SJcrM.png "User Profile Info")
This pic shows the basic details that the users have to provide in order to be able to use the app and all its features. There are many different verification process in the backend of this page in order to check security and privacy issues, which can arise due to location based services.
Share.it has pretty much everything covered.

We are using NginX web server to serve Share.it web application. The back-end system is based-on Django web framework with SQLite database.

![git](http://i.imgur.com/vdSYlz5.png "git")
Development process with git


![nginx](http://i.imgur.com/YgT10Q1.png "nginx")
Nginx running on Koding VM


## APIs used

API | URL | Description
--- | --- | ---
Google Map Javascript API | https://developers.google.com/maps/documentation/javascript/ | We use this API to display Food Banks, Volunteers, and Food Broadcast's locations
PubNub | http://www.pubnub.com/developers/ | We use this API to provide real-time chat and food broadcast
JustGiving <br>(from 3Scale) | https://apimanagement.justgiving.com/ | We use this API to provide donation payment service
Disqus <br>(from APItools) | https://www.apitools.com/apis/disqus | We use this API to facilitate commenting in Contact page
Share.It <br>(deployed in Mashape) | https://www.mashape.com/codeepy/share-it | We developed this API to serve and retrieve the Volunteers' locations
NutritionIx | http://www.nutritionix.com/api | We used this API to provide nutritional information for shared foods
