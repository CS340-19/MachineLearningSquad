AutoStories for Twitter
 

*The Machine Learning Squad*
Github: MachineLearningSquad

Members:
Jared Colburn,
Kody Bloodworth,
Tanner Fry,
Austin Oaks

1: Introduction
Our project will be a browser addon that puts links to relevant news articles next to tweets. It will use machine learning technologies to determine if a tweet is related to a current event.

In the age of information, social media has revolutionized how people consume and discuss information. 
However, information often travels faster than people are able to responsibly consume it. 
Social media is a hotbed for misinformation, and it can spread quickly in these environments.
For many people, it can seem overwhelming to keep up to date with accurate information regarding current events.
Our project hopes to alleviate some of the anxieties by helping users stay informed and up-to-date in conversations with their peers.

Our project fills the need to those wishing to keep up with current events through Twitter. Twitter can be a very useful source of this kind of information, but matching the words of other people with relevant information can sometimes be difficult. Our addon aims to cut out the middleman and provide users with this research automatically.


2: Customer Value

Our target market is Twitter users who wish to stay connected and informed. We're aiming for our users to be twenty years of age or older. Due to our product being a tied to the browser landscape, our target audience might tend a little older, as younger users might default to mobile for any Twitter usage. We obviously can't really consider teenagers or the eldery as part of the core market we're trying to reach.

The customers we're trying to reach want to do their own research and come to their own conclusions,
while still being able to communicate with friends and family online. They also want this process to be as seamless as possible. Attempting to keep up with the flurry of online discussion can be exhausting. Often, people will ignore online discussions to avoid having to put in the work to research. We hope to help somewhat alleviate that exhaustion by providing an easy way to find relevant stories on Twitter.

Social media has taken center stage in the past few years, due to it's inability to present users with factual information- it's main goal is to present opinions and reactions, not inform users. Our customers will be very aware of this fact. We want to cater to people who want to understand current events, yet feel they don't have the time to do so. Our solution hopes to merge social media, in this case: Twitter, with relevant and trusted news articles. Our browser add-on will hopefully allow Twitter users access to stories their friends are discussing with only a click. Through natural language processing, we hope to deliver desktop Twitter users relevant information in regards to what people in their network are discussing online. The news stories we display will come from trusted sources curated by the Google News API. We hope to allow users the choice between different sources, as well. This should allow our customer base peace of mind in using our project for their researching purposes.

There's also nothing quite like this available at the moment. In neither the Firefox Extension store, nor the Google Addons Store, there is nothing that helps Twitter users gain easier access to relevant stories. There are some publicly available tweet analyzing projects, such as "AnalyzeWords.com", but most of these projects seem to present themselves as novelties. Our project's goals are significantly different.



3: Proposed Solution & Technology

   Our addon for Firefox will allow Twitter users to find related articles on tweets to get a better understanding of the talked about subject. There will be a lot of moving parts within our addon consisting of JavaScript, Python, HTML, and CSS. HTML and CSS will be used for designing a UI for the addon dropdown window. JavaScript is used to initiate the addon within Firefox, and will be used to communicate with the Twitter API, Google API, and Python scripts hosted on a server. The overall process will start with the user starting our addon on the page of the tweet, the addon will then be using the Twitter API through JavaScript to obtain the text of the tweet, then connect to the server hosting the Python machine learning script to send the tweet data, then the Python script will use machine learning algorithms to estimate keywords from the tweet to search through google to find related information, once the Python script obtains the keywords, the keywords will be sent back to JavaScript which will then pass those keywords to the Google API which will return the top search results from the keywords and return the links and information on the results. We hope to use Pyhton machine learning libraries such as the Natural Language Toolkit and Tensorflow to implement these kids of scripts. Both should be ableto classify text as we require. Lastly, JavaScript will call HTML files for formatting the results, and within the HTML files, CSS files will be called for more formatting of the results. As of right now, we have decided to return the top three returned articles from the Google API in the addon dropdown window, which once clicked will open a new tab of that link. There will also be a feedback system implemented next to the links provided that will be used to determine if the provided links are valid suggestions for the topic expected from the user, and that feedback will loop back to the Python script, so the learning algorithm can adjust.
   
   For testing and debugging our code, the Python scripts will begin being tested separately on a local computer for researching and testing algorithms that provide the best accuracy, and once finished will be uploaded to a created server or a hosting server service that Google provides. For JavaScript, HTML, and CSS debugging and testing will be done within editors (Visual Studio, Atom, etc.) and then pushed to Firefox within their development/debugging menu which will allow us to deploy a temporary addon to test on our browser alone. 
   
   Once all has been implemented, we have two ideas on how the addon will appear for the user. First, the addon could stay in the toolbar, and when the user opens the page of the tweet itself, click the addon, and it will generate and return the links to the articles. Second, the other idea we had is to implement a button that will be attached to tweets that when clicked will activate the addon to begin generating the related story links. Once we get more experience with working with the Twitter API and its limitations, we will be decided which path we want pursue on the initial startup for the addon. If we decide to do an in-browser UI, it will be implemented using publicly available JavaScript graphics and/or UI libraries like React.

5: Project Management

   For project management, we have a few milestones / goals mapped out across the coming months that will be distributed equally across team members to embrace each other’s strengths / interests if possible. Our project has multiple pieces all communicating with each other including JavaScript, HTML, CSS, and Python scripts. Our starting point will be creating an “empty” addon to have a shell to begin working in. After the addon is created, our next goal will be working with the Twitter API for extracting tweets and begin building the logic of the machine learning scripts within Python. After we can read tweets and manually give them to our Python scripts to interpret and return keywords for searching, we will begin working with the Google API for giving it the keywords and finding related articles based on the tweets. After these milestones are met, the last part is to string everything together to communicate on their own, and work on the design of the addon for displaying information to the user. For each milestone, all of us will be working together on each major part but depending on how the tasks can be broken down further within each milestone, some members might work on certain sections on their own to be more efficient. Throughout the entire project, we will all be meeting in and outside of class, as well as communicating through Discord, and using GitHub for managing our filesystem for the project. We have already gotten our addon shell created, tested, and working, so our next steps will be working with the Twitter API, and begin research in machine learning with Python.
