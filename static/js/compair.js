
  $("#files_submit").click(function(){
  var file1 = $('#file_select1').val()
  var file2 = $('#file_select2').val()
  var data = {'file1':file1,'file2':file2}
    $.ajax({
      type : 'POST',
      url : "/compair_files",
      data : data,
      success:function(data){
      console.log(data)
      },
    });
  });
