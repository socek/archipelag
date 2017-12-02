$(document).ready(function() {

    	$(".modal_button").on('click', function()
	{
		let market_id=$(this).data('id');
		console.log(market_id)
       	openModal(market_id);

    });

});

function openModal(market_id){
    $("#modalInfo").modal();
    $('.modal-body').html("");
}