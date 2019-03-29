function GetTweetStories(){
	if(window.location.href.match(/twitter.com/g) != null){
		var path = window.location.pathname;
		var 
		
	}
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if(this.readyState == 4 && thiis.status == 200){
			var stories = this.responseText;
			var objs = JSON.parse(stories);
			document.getElementById("story-1").innerHTML = objs[0].title;
		}else{
			document.getElementById("story-1").innerHTML = "Not a Valid Page! Sorry!";
		}
	};
	xhttp.open("GET", 

}

document.addEventListener("click", function (e) {
    if (!e.target.classList.contains("page-choice")) {
        return;
    }

    var chosenPage = "https://" + e.target.textContent;
    browser.tabs.create({
        url: chosenPage
    });

});
