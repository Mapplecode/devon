
  $("#files_submit").click(function(){
  $('#table_data').html('')
  var file1 = $('#file_select1').val()
  var file2 = $('#file_select2').val()
  var data = {'file1':file1,'file2':file2}
    $.ajax({
      type : 'POST',
      url : "/compair_files",
      data : data,
      success:function(data){
      console.log(data['data'])
      $('#table_data').html(data['data'])
      },
    });
  });
