function byId(id){ return document.getElementById(id); }

var actions=['splash',
			 'add-curator', 
			 'edit-curator',
			 'remove-curator',
			 'add-resource',
			 'edit-resource',
			 'remove-resource'];

function displayAction(action){
	var act = byId(action);
	act.style.display = 'block';
	for (var i = 0; i < actions.length; ++i){
		if (act != byId(actions[i])){
			byId(actions[i]).style.display = 'none';
		}
	}
}