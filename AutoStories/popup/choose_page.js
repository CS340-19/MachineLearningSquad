function GetTweetStories(){
	if(window.location.href.match(/twitter.com/g) != null){
		var path = window.location.pathname;
		var n = path.lastIndexOf("/");
		var id = path.substr(n+1);
		console.log(id);	
	}else{
		document.getElementById("story-1").innerHTML = "Not a Valild Page! Sorry!";
	}
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if(this.readyState == 4 && this.status == 200){
			//var stories = this.responseText;
			//var objs = JSON.parse(stories);
			//console.log(objs[0].title);
			document.getElementById("story-1").innerHTML = "hey";//objs[0].title;
		}else{
			console.log("failed server");
			document.getElementById("story-1").innerHTML = "Not a Valid Page! Sorry!";
		}
	};
	xhttp.open("GET", "url.txt", true); 
	xhttp.send();
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
