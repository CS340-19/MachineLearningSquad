*TENTATIVE*
 

*Machine Learning Squad*

Memebers:
Jared Colburn,
Kody Bloodworth,
Tanner Fry,
Austin Oaks

1: Introduction
(In the age of information, social media has revolutionized how people consume and discuss information. 
However, often, information travels faster than people are able to consume it. 
Often times, users are left "out of the loop," unsure what others are discussing. 

Worse, misinformation can easily spread through social media. In these environments,
doing your own research becomes exhaustive. Our project hopes to aleviate some of these anxieties. 
Our project will allow users to do their own research and stay up-to-date in conversations with their peers,
specifically through Twitter.) -This might make for a good introduction? Wrote it for the customer value section 
before actually reading the proposal guideline.


2: Customer Value

Our target market is Twitter users who wish to stay connected and informed. We're aiming for our users to be between twenty years or older. Due to our product being a tied to the browser landscape, our target audience might tend a little older, as younger users might default to mobile for any Twitter usage. We obviously can't really consider teenagers or the eldery as part of the core market we're trying to reach.
The customers we're trying to reach want to do their own research and come to their own conclusions,
while still being able to communicate with friends and family online. They also want this process to be as seamless as possible. Social media has taken center stage in the past few years, due to it's inability to present users with factual information- it's main goal is to present opinions and reactions, not inform users. Our customers will be very aware of this fact. We want to cater to people who want to understand current events, yet feel they don't have the time to do so.

Furthermore, attempting to keep up with the flurry of online discussion can be exhausting. Often, people will ignore online discussions to avoid having to put in the work to research. We hope to help alleviate that exhaustion, at least a small amount, by providing an easy way to find relevant stories on Twitter. 

Our solution hopes to merge social media, in this case: Twitter, with relevant news articles. Our browser add-on will hopefully allow Twitter users access to stories their friends are discussing with only a click. Through natural language processing, we hope to deliver desktop Twitter users relevant information in regards to what people in their network are discussing online.

There's also nothing quite like this available at the moment. In neither the Firefox Extension store, nore the Google Addons Store, there is nothing that helps Twitter users have easier access to relevant stories. There are some publicly available tweet analyzing projects, such as "Tweet Analyzer", but most of these projects seem to present themselves as novelties. Our project's goals are significantly different.

These stories will come from trusted sources curated by the Google News API, and will allows users choices between different sources. This should allow our customer base peace of mind in using our project for their researching purposes.


3: Proposed Solution & Technology

	*BRAINSTORM* 

 From our point of view, this addon is able to use the
 information stored inside the tweet (through a Twitter API)
 and return results (with a Google API). Specifically, JavaScript
 will be used to call to our Python with prompts to a server returning
 keywords to the JavaScript, those keywords will be pushed to a Google
 API (which will hopefully return the top 3 searches). A provide
 relevant information to an audience that isn't informed about the
 context. The "minimal" system that would be of use to our customer 
 would be our usage of a search engine. What makes ours unique? 
 Simple - convenience. With our implementation you can reach the 
 relevant information through a click/interaction with the addon 
 rather than use several actions/resources to reach the same result.
 Firefox has a debugging tool where we can directly test and interact 
 with our intermediate creation. 

The search results provided to the customer.
Provided background information to inform the customer.
Directly test the addon through Firefox. (about:debugging)

Build - text editor, servers able to send and recieve information. (Google Engine)
Tools - Google News API, Google APP Engine (Instances), Google Natural Language Library, Twitter Developer Tools, Python Server

4: Team

5: Project Management

For project management, we have a few milestones / goals mapped out across the coming months that will be distributed equally across team members to embrace each other’s strengths / interests if possible. Our project has multiple pieces all communicating with each other including JavaScript, HTML, CSS, and Python scripts. Our starting point will be creating an “empty” addon to have a shell to begin working in. After the addon is created, our next goal will be working with the Twitter API for extracting tweets and begin building the logic of the machine learning scripts within Python. After we can read tweets and manually give them to our Python scripts to interpret and return keywords for searching, we will begin working with the Google API for giving it the keywords and finding related articles based on the tweets. After these milestones are met, the last part is to string everything together to communicate on their own, and work on the design of the addon for displaying information to the user. For each milestone, all of us will be working together on each major part but depending on how the tasks can be broken down further within each milestone, some members might work on certain sections on their own to be more efficient. Throughout the entire project, we will all be meeting in and outside of class, as well as communicating through Discord, and using GitHub for managing our filesystem for the project. We have already gotten our addon shell created, tested, and working, so our next steps will be working with the Twitter API, and begin research in machine learning with Python.
