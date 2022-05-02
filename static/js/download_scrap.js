
$(document).ready(function(){


$.ajax({
      type : 'POST',
      url : "/get_scrap_files",
      data : {},
      success:function(data){
      $('#table_data_downloads').append(data['data']);
      $('#table_data').css('max-height','200px');
      $('#table_data').css('overflow','scroll');
      $('#buttons_row').show();
      },
    });


$(".action_btn").on('click',function () {
alert('hi')
})



})


//function delete_file(file_name){
//
//$.ajax({
//      type : 'GET',
//      url : "/delete_scrap_files",
//      data : {'file_name':file_name},
//      success:function(data){
//     location.reload();
//      },
//    });
//
//
//}