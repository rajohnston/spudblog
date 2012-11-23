

/*____________________________________________________________________*/

$(document).ready(function() {






 
});

/*_______________________________________________________________________*/

function change_spud_divider(divider) {
	$url = '/?';
	$url = $url + "divider="+divider;
	window.location.href = $url;
}

function viewpost(key) {
	$url = '/?';
	$url = $url + "divider="+divider;
	window.location.href = $url;
}

function deletepost(key) {
$("#delete"+key).fadeIn(300);

}

function canceldelete(key) {
$("#delete"+key).hide();
}