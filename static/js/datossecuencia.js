$(function(){
	$('#button').click(function(){
        var seq = $('#secuenciausuario').val();
        $.ajax({
			url: '/resultados',
			data: $('form').serialize(),
			type: 'POST',
			success: function(data){
                $( '#datossecuencia' ).html(data);
			},
			error: function(error){
				console.log(error);
			}
		});
    });
});
