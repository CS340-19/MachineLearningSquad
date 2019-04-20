function send_request(xhr, id) {
    // TODO: Get the id here
    return xhr;
}
// res is an object
// res[0] is the tweetid
// the rest are 3 links: link, description, title
function insertLinks(res) {
    console.log(res);
    console.log(res[0]);
    console.log(res[1].link);
    var id = res[0];
    var link = document.createElement("div");
    link.innerHTML += '<div><a href="' + res[1]['link'] + '">' +  res[1]['title'] + '</a></div>';
    link.innerHTML += '<div><a href="' + res[2]['link'] + '">' +  res[2]['title'] + '</a></div>';
    link.innerHTML += '<div><a href="' + res[3]['link'] + '">' +  res[3]['title'] + '</a></div>';
    // Find tweet through tweet id and insert link after everything else
    tweet = document.querySelector('div[data-item-id="'+ id +'"]');
    tweet.appendChild(link);
}

function addbutton(tweets) {
    for(var i = 0; i < tweets.length; i++) {
        if(tweets[i].tagName == "LI") {
            // The copy the "DM" button
            var copy = tweets[i].getElementsByClassName("ProfileTweet-actionList")[0].childNodes[7].cloneNode(true);
            // Add it after the "DM" button
            tweets[i].getElementsByClassName("ProfileTweet-actionList")[0].appendChild(copy);
            // Deleting a class so that the button does not work as the "DM" button anymore
            copy.childNodes[1].setAttribute("class", "ProfileTweet-actionButton u-textUserColorHover js-actionButton");
            copy.childNodes[1].addEventListener("click", function(event) {
                var id = event.target.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.dataset.itemId;
                var xhr = new XMLHttpRequest();
                xhr.responseType = "json";
                xhr.onload = function() {
                    res = xhr.response;
                    console.log(res);
                    insertLinks(res);
                }
                xhr.open("GET", "http://107.161.31.193:5000/?tweetid=" + id);
                xhr.send();
                //xhr = send_request(xhr, id);
               // var link = document.createElement("div");
                //link.innerHTML = "<br />link would go here";
                // Inserting link after everything else in element
                //event.target.parentElement.parentElement.parentElement.parentElement.parentElement.insertBefore(link, null);
            });

        }
    }   
}
document.addEventListener("DOMContentLoaded", function(event) {
    // When DOM is loaded set up observer
    var config = { childList: true };
    var callback = function(mutationsList, observer) {
        for(var mutation of mutationsList) {
            if (mutation.type == 'childList') {
                addbutton(mutation.addedNodes);
            }
        }
    };
    var observer = new MutationObserver(callback);

    // Add the button to each tweet
    var tweetslist = document.getElementById("stream-items-id");
    addbutton(tweetslist.childNodes);

    // Start observing immediately after adding initial buttons
    observer.observe(tweetslist, config);
});

