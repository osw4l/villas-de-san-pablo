// -------------------------------
// Initialize Data Tables
// -------------------------------

$(document).ready(function() {
    $('#example').dataTable({
    	"language": {
    		"lengthMenu": "_MENU_",
			"zeroRecords": "Lo sentimos, no se encontraron registros",
            "info": "Mostrando pagina _PAGE_ de _PAGES_",
            "infoEmpty": "Ho hay registros disponibles",
            "infoFiltered": "(filtrado de _MAX_ registros)",
			"paginate": {
    			"previous": "Anterior",
				"next": "Siguiente"
			}
    	}
    });
    $('.dataTables_filter input').attr('placeholder','Buscar...');


    //DOM Manipulation to move datatable elements integrate to panel
	$('.panel-ctrls').append($('.dataTables_filter').addClass("pull-right")).find("label").addClass("panel-ctrls-center");
	$('.panel-ctrls').append("<i class='separator'></i>");
	$('.panel-ctrls').append($('.dataTables_length').addClass("pull-left")).find("label").addClass("panel-ctrls-center");

	$('.panel-footer').append($(".dataTable+.row"));
	$('.dataTables_paginate>ul.pagination').addClass("pull-right m-n");

});