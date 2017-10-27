var aSBool = 0;

// Shorthand
function byId(id){	return document.getElementById(id);	};

// Dispaying Sidebar Dropdown Menu
function showAdvancedSearch(){
	if (aSBool == 0){	
		byId('as-options').style.display = "block";
		aSBool = 1;
	}
	else {	
		byId('as-options').style.display = "none";
		aSBool = 0;
	}
	
};

function showMap(){
	var initState = {
		center:new google.maps.LatLng(51.508742,-0.120850),
		zoom:5,
	};
	var map = new google.maps.Map(byId('googleMap'),initState);
};

function setRightWidth(){
	var ww = $(window).width();
	var lw = $('#left').width();
	$('#right').css('width', ww-lw);
	
}

function setHeights(){
	var wh = $(window).height();
	var hh = $('#nav-override').height();
	// Setting Content Width
	$('#left').css('height', wh-hh);
	$('sideBar').css('height', wh-hh);
	// Setting Content Height
	$('#right').css('height', wh-hh);
	$('#googleMap').css('height', wh-hh);
}