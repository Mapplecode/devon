
$(document).ready(function(){

$('.action_btn').click(function(){

$.ajax({
      type : 'POST',
      url : "/download_scrap",
      data : {'file':$(this).val()},
      success:function(data){

      },
    });




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