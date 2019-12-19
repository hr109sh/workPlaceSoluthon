	$("#searchText").keyup(function(){
    var selectedSearchField = $('#searchDropdown').val();
    var inputValue = $('#searchText').val();
    if (inputValue != ""){
    	$.ajax({
        	url: '../requested_search/',
        	data: {
          		'inputValue': inputValue,
          		'selectedSearchField':selectedSearchField
        	},
        	dataType: 'json',
        	success: function (data) {
        		var response_data = JSON.parse(data).output_data;
          		if (data) {
          			$('#table-body').html("")
          			for (index = 0; index < response_data.length; index++) { 
    					$('#table-body').append("<tr><td>"+response_data[index][0]+"</td><td>"+response_data[index][1]+"</td><td>"+
    					response_data[index][2]+"</td><td>"+response_data[index][3]+"</td><td>"
    					);
					} 
          			$('#table-row').css('display','block');
          		}
          		else{

          		}
        	}
      });
    }
    else{
  		$('#table-row').css('display','none');
  	}
    
});