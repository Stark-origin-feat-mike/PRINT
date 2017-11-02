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
	var nll = new google.maps.LatLng(id[0], id[1]);
	map.panTo(nll);
}

// Dispaying Sidebar Dropdown Menu
function expand(id){
	var cmpss = ['ken-options', 'sta-options', 'gea-options', 'ash-options', 'sal-options',
	'eli-options', 'tru-options', 'tus-options'];
	var current = byId(id);

	if (current.style.display == "block"){
		current.style.display = "none";
	}
	else {
		current.style.display = "block";
		for(var i = 0; i < cmpss.length; ++i){
			if (byId(cmpss[i]) != current){
				byId(cmpss[i]).style.display = 'none';
			}
		}
	}

	if (current != byId('campus-options')) moveToLoc(campusLocs[id]);
};

// Initilizing Google Map
var map;
function showMap(){
	var initState = {
		center: new google.maps.LatLng(41.149467, -81.347666),
		zoom: 17,
	};
	map = new google.maps.Map(byId('googleMap'), initState);

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