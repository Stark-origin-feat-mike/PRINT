var testStuff = [{"name": "interior", "location": {"lat": 41.147488, "lng": -81.343053}, "type": "makerSpace"}, 
				 {"name": "crocodile", "location": {"lat": 41.147, "lng": -81.343}, "type": "Movie Theater"}];

// Shorthand
function byId(id){	return document.getElementById(id);	};

var campusLocs = {};
campusLocs['ken-options'] = [41.147488, -81.343053];
campusLocs['sta-options'] = [40.867854, -81.437213];
campusLocs['gea-options'] = [41.483896, -81.143170];
campusLocs['ash-options'] = [41.888643, -80.832334];
campusLocs['sal-options'] = [40.864161, -80.835618];
campusLocs['eli-options'] = [40.616960, -80.576650];
campusLocs['tru-options'] = [41.278921, -80.837273];
campusLocs['tus-options'] = [40.467633, -81.407134];

// Moving Map Center
function moveToLoc(id){
	var nll = new google.maps.LatLng(campusLocs[id][0], campusLocs[id][1]);
	map.panTo(nll);
}

// Dispaying Sidebar Dropdown Menu
function expand(id){
	var cmpss = ['ken-options', 'sta-options', 'gea-options', 'ash-options', 'sal-options',
	'eli-options', 'tru-options', 'tus-options', 'campus-options'];
	var current = byId(id);

	if (current.style.display == "block"){
		current.style.display = "none";
	}
	else {
		current.style.display = "block";
	}

	if (current != byId('campus-options')) moveToLoc(id);
};

// Initilizing Google Map
var map;
function showMap(){
	var initState = {
		center: new google.maps.LatLng(41.149467, -81.347666),
		zoom: 17,
		mapTypeId: google.maps.MapTypeId.SATELLITE
	};
	map = new google.maps.Map(byId('googleMap'), initState);

	for (var i = 0; i < testStuff.length; ++i){
		var marker = new google.maps.Marker({
	      position: testStuff[i]["location"],
	      map: map,
	      title: testStuff[i]["name"]
	  	});
	}

	google.maps.event.addListenerOnce(map, 'idle', function() {
    	google.maps.event.trigger(map, 'resize');
	});
};

//Getting Width of Google Map
function setRightWidth(){
	var ww = $(window).width();
	var lw = $('#left').width();
	$('#right').css('width', ww-lw);	
}

// Setting height of Google Map and Nav Bar
function setHeights(){
	var wh = $(window).height();
	var hh = $('#nav-override').height();
	$('#left').css('height', wh-hh);
	$('sideBar').css('height', wh-hh);
	$('#right').css('height', wh-hh);
	$('#googleMap').css('height', wh-hh);
}



function dListClick(name) {
	var lat;
	var long;
	for (var i = 0; i < testStuff.length; ++i){
		if (testStuff[i]["name"] == name){
			lat = testStuff[i]["location"]["lat"];
			long = testStuff[i]["location"]["lng"];
			break;
		}
	}
	var nll = new google.maps.LatLng(lat, long);
	map.panTo(nll);
}

$(document).ready(function(){
	$("#get-search").on('keyup', function (e){
	    if (e.keyCode == 13) {
	        var searchedFor = logValue();
	        search(searchedFor);
	    }
	})
});

function logValue(){
	var x = byId('get-search').value;
	return x;
}

function search(sstring){
	// Clearing Nav Bar List
	$('#listing').empty();
	for (var i = 0; i < testStuff.length; ++i){
		if (testStuff[i]["name"] == sstring){
			makeListElement(testStuff[i]);
		}
	}
}

function makeListElement(resource){
	//for (var i = 0; i < testStuff.length; ++i){
		var container = byId('listing');
		var node = document.createElement('li');
		node.innerHTML = "<div class=\"dList\" onclick=\"dListClick(\'" + resource["name"] + "\')\"><p class=\"dPAttr\">Name: " 
		+ resource["name"] + "</p><p>Type: " + resource["type"] + "</p></div>";
		container.appendChild(node);
	//}
}
