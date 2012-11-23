

/*____________________________________________________________________*/

$(document).ready(function() {


$('.spud').live('mouseover', function() {

$(this).attr("src","styles/images/upright_potato_eyes.png");
	});

$('.spud').live('mouseout', function() {
	
$(this).attr("src","styles/images/upright_potato.png");
	});



 
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
$("#spud"+key).attr("src","styles/images/upright_potato_surprise.png");


}

function canceldelete(key) {
$("#delete"+key).hide();
$("#spud"+key).attr("src","styles/images/upright_potato_eyes.png");

}