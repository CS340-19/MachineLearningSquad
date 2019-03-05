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
                // TODO: make request to server here
                var link = document.createElement("div");
                link.innerHTML = "<br />link would go here";
                // Inserting link after everything else in element
                // TODO: my eyes
                event.target.parentElement.parentElement.parentElement.parentElement.insertBefore(link, null);
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
})r

var xhr = new XMLHttpRequest()
xhr.onload = function () {
    // TODO: Change a global link variable?
}
function send_request(xhr) {
    // TODO: Get the id here
    xhr.open("GET", "http://localhost:9000/?id=" + id, true);
    xhr.send();
}
