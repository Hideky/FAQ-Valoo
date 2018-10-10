$(document).ready(function(){
	// Edit Question answer
    $('#accordion').find('button[name=edit]').click(function(){
		var button = $(this);
		button.prop('disabled', true);
		$.ajax({
			headers: {
				'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
			},
			type: "PATCH",
			url: "/api/questions/"+button.attr('id')+"/",
			data: {
				answer: button.parent().parent().parent().find('textarea').val(),
			},
			success: function(data){
				console.log("Success");
			},
			error: function(){
				console.log('Error');
			},
			complete: function(){
				console.log('Complete');
				button.prop('disabled', false);
			}
		});
	});

    // Hide Question
    $('#accordion').find('button[name=hide]').click(function(){
		var button = $(this);
		if (button.html().includes('Cacher'))
			hidden = true;
		else
			hidden = false;
		button.prop('disabled', true);
		$.ajax({
			headers: {
				'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
			},
			type: "PATCH",
			url: "/api/questions/"+button.attr('id')+"/",
			data: {
				csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
				hidden: hidden,
			},
			success: function(data){
				if (hidden)
					button.html('Montrer');
				else
					button.html('Cacher');
			},
			error: function(){
				console.log('Error');
			},
			complete: function(){
				console.log('Complete');
				button.prop('disabled', false);
			}
		});
	});

	// Delete Question
    $('#accordion').find('button[name=delete]').click(function(){
		var button = $(this);
		button.prop('disabled', true);
		$.ajax({
			headers: {
				'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
			},
			type: 'DELETE',
			contentType: 'application/json',
			url: "/api/questions/"+button.attr('id')+"/",
			success: function(data){
				button.parent().parent().parent().remove()
			},
			error: function(){
				button.prop('disabled', false);
				console.log('Error');
			},
		});
	});
});