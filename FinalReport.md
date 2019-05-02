<h1>AutoStories for Twitter</h1>

MachineLearningSquad
Team Number: 4

Github: MachineLearningSquad

Members: Jared Colburn, Kody Bloodworth, Tanner Fry, Austin Oaks
</br></br>
<h2>Introduction</h2>
Our project was a browser add-on that provides the user relevant Google search links to a given tweet. It was 
intended to use machine learning technoloigies to determine if a tweet is related to a current event. Our motivation
has been consistent throughout the project: To provide people a quick reference to information neeeded. We approached
this project with the usage of various API to extract and produce the information needed to provide for our add-on.
As we continued development there were no major changes to requirements, design, or development plans. With the limited
time we had, we managed to complete a functional add-on that accomplished our original goal with limitations. At the
surface level we completed our project's goals, but there is always room for improvement.

</br></br>
<h2>Customer Value</h2>

No changes. We still believe that our customers will value quick access to information about the stories their friends are discussing. 

</br></br>
<h2>Technology</h2>

Our addon for Firefox will allow Twitter users to find related articles on tweets to get a better understanding of the talked
about subject. There will be a lot of moving parts within our addon consisting of JavaScript, Python, HTML, and CSS. HTML and
CSS will be used for designing a UI for the addon dropdown window. JavaScript is used to initiate the addon within Firefox,
and will be used to communicate with the Twitter API, Google API, and Python scripts hosted on a server. The overall process
will begin when the user interacts with our addon on the page of the tweet, the addon will then be using the Twitter API
through JavaScript to obtain the text of the tweet, connect to the server hosting the Python machine learning script to send
the tweet data, then the Python script will use machine learning algorithms to estimate keywords from the tweet to search
through Google to find related information, once the Python script obtains the keywords, they will be sent back to JavaScript
and be passed to the Google API which will return the top search results from the keywords and return the links and
information on the results.

After completing our minimum viable system of "Tweet-to-GoogleSearch" program, we set out the goal to transition it to our
Firefox add-on. Once the user clicks on our icon, which is just the same Direct Message icon but on the far right, 
relevant Google links are provided as shown:
![working](https://cdn.discordapp.com/attachments/535828386912927752/572499205210243073/working.png)

However, it isn't perfect. Our add-on rarely succeeds on tweets with images and sometimes it just fails. This example
shows our add-on providing the link back to itself.
![notworking](https://cdn.discordapp.com/attachments/535828386912927752/572499062960554056/notworking.png)

The consistency of our add-on is not clean either. On occassion our add-on doesn't even appear and requires the whole
page to be refreshed.

Before Refresh:

![notrefresh](https://cdn.discordapp.com/attachments/535828386912927752/572499094644457477/notworkingtillrefresh.png)

After Refresh:

![refresh](https://cdn.discordapp.com/attachments/535828386912927752/572499154916343829/workingonrefresh.png)

We have tested for various tweets and results to find our programs flaws and errors. Various Twitter accounts, types of
tweets, what words the tweets have, what media is on the tweet. As previously mentioned, our add-on once visible only
consistently succeeds on text-only tweets. 


</br></br>
<h2>Team</h2>

The overall work that each team member was assigned to applied to that team members strengths / interests, and was evenly distributed
as much as possible. There was no specific roles that each team member held throughout the project because each week we broke down
what we needed into different parts and each person was assigned to those issues accordingly. Below are the tasks / issues that each
team member worked on. 

- Jared Colburn: Project Manager, updated the GitHub repository setting due dates, outside-of-class meetings, checking up
on each member. Researched how to communicate with the Twitter API, Google API and provided background assistance with 
each members' roles/assignments.

- Austin Oaks: Implemented the Firefox addon that read our server API and inserted the Google Search links below the corresponding tweet. The addon was written in JavaScript and used content scripts and AJAX requests to communicate with the server and display each link. 

- Kody Bloodworth: Researched extensively into various machine learning concepts that could be used for our project, developed the backend code structure, implemented the Google Custom Search API, wrote the backend server with Flask, developed the basic structure for how the data would be sent to the client, and created a testing applet to debug our server implementation before our Javascript interface was fully developed. 

- Tanner Fry: Worked on researching how to communicate with the Twitter API, Google API, and how to use RAKE. Implemented a very bare
bones Firefox addon and python script for communicating with the Twitter API(tweepy), the Google API, and basic usage of RAKE. My
simplistic structures was then elaborated and built upon by the other members for a more detailed design, and desired implementation
setup needed for the addon to be fully functional.

Each member was assigned their own research and implementations so roles were static for the production. GitHub was rarely
used as we mostly communicated and shared through Discord.

</br></br>
<h2>Project Management</h2>
Unfortunately, we did not complete all of our goal for the product, especially not on schedule. For example research
phase, we did complete it but it was a continuous process, once we needed new techniques or skills we had to spend more 
time investing ourselves into learning consuming much more time. As a whole, we faced various time delays. The main
reasons we did not meet our goals involved miscommunication, lack of communication, and time conflicts. The first
two points involve our communication skills in our group, our primary tool was Discord and not all of us used it as much
compared to others so response times would vary between persons. Some instances of miscommunication involve code - if it
wasn't commented or obvious to "decipher," time would be spent either figuring it out or debugging due to improper
understanding of what was provided. Most meetings, even ones in class, not all members would be present due to other
urgent needs dwindling down the small amount of time we spend as a group. Even with all of these obstacles we still
managed to find opportunities to gather and create our product. Above all this, our lack of familiarity with the technologies we were using meant that what time we had was spent with research and experimentation. While this yielded new skills, it also meant that our original assumptions regarding scheduling were futher distorted.


</br></br>
<h2>Reflection</h2>
For this iteration and throughout the project, we actually managed to create a functioning add-on for our presentation
date. Our quick understanding of what we needed to do and our decision making throughout the project were our best
aspects. Unfortunately, we knew what we needed to do, but not how to do it. Some roadblocks caused coding to backtrack
or be completely abandoned. Our lack of proper documentation was a disaster as well, if only one person knew/worked on
something and went "MIA" the rest of the group with be completely clueless on that part. Development went in jumps, we
had time periods where nothing was done then some when a lot of things would be completed. Our testing phase was brief,
but we did manage to find our program's flaws and weaknesses. In future projects, we intend to learn from our mistakes, and more appropriately handle communication and time management. Team management was proper, meetings were created when
needed and everyone was followed-up with, updates for each part were provided at the earliest convenience, either through
class time or Discord. In conclusion, we consider this project to be a success, although it isn't "complete" we all
walked in wanting an experience to broaden our knowledge/skills of the Computer Science field, we can all agree
that we learned a lot from this project and can showoff this add-on. 
