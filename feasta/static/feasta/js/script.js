$(document).ready(function(){
	$('#user-settings-burger').hide();
	$('#show-user-settings').click(function(){
		$('#user-settings-burger').toggle();		
	});
	$('#user-settings-burger-non').hide();
	$('#show-user-settings').click(function(){
		$('#user-settings-burger-non').toggle();		
	});
	var h_feastacontent = $('.feasta-content').css('height');
	$('.content-wrapper').css('height',h_feastacontent);
});


