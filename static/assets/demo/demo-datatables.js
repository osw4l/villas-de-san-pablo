// -------------------------------
// Initialize Data Tables
// -------------------------------

$(document).ready(function() {
    $('#example').dataTable({
    	"language": {
    		"lengthMenu": "_MENU_",
			"zeroRecords": "Lo sentimos, no se encontraron registros para mostrar",
            "info": "Mostrando pagina _PAGE_ de _PAGES_",
            "infoEmpty": "Ho hay registros disponibles",
            "infoFiltered": "(filtrado de _MAX_ registros)",
			"paginate": {
    			"previous": "Anterior",
				"next": "Siguiente"
			}
    	},
		"dom": "Bfrtip",
   		"bProcessing": true,
   		"bAutoWidth": false,
   		"responsive": true,
   		"buttons": [
			{ extend: 'copy', text: 'Copiar <i class="fa fa-copy"></i>'},
			{ extend: 'excel', text: 'Exportar a Excel <i class="fa fa-file-excel-o"></i>'},
			{ extend: 'pdf', text: 'Exportar a PDF <i class="fa fa-file-pdf-o"></i>'},
			{ extend: 'colvis', text: 'Columnas Visibles <i class="fa fa-columns"></i>'},
			{ extend: 'print', text: 'Imprimir <i class="fa fa-print"></i>'}
		]
    });


    //DOM Manipulation to move datatable elements integrate to panel
	$('.panel-ctrls').append($('.dataTables_filter').addClass("pull-right")).find("label").addClass("panel-ctrls-center");
	$('.panel-ctrls').append("<i class='separator'></i>");
	$('.panel-ctrls').append($('.dataTables_length').addClass("pull-left")).find("label").addClass("panel-ctrls-center");

	$('.panel-footer').append($(".dataTable+.row"));
	$('.dataTables_paginate>ul.pagination').addClass("pull-right m-n");

});