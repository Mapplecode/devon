
  $("#files_submit").click(function(){
  $('#table_data').html('')
  var file1 = $('#file_select2').val()
  var file2 = $('#file_select1').val()
  var data = {'file1':file1,'file2':file2}
    $.ajax({
      type : 'POST',
      url : "/compair_files",
      data : data,
      success:function(data){
      $('#table_data').append(data['data']);
      $('#table_data').css('max-height','200px');
      $('#table_data').css('overflow','scroll');
      $('#buttons_row').show();
      },
    });
  });

$('.change-buttons').click(function(){
var text = $(this).text()

$('.actions').css('display','none');
if(text == 'Added'){
$('.added').css('display','table-row');
}
if(text == 'Changed'){
$('.changed').css('display','table-row');
}
if(text == 'Removed'){
$('.removed').css('display','table-row');
}
})

function download_file(){

  $.ajax({
      type : 'GET',
      url : "/download_file",
      data : {},
      success:function(data){
      download(data, "compair.csv", "text/csv");
      },
    });
}

function download(content, filename, contentType)
{
    if(!contentType) contentType = 'application/octet-stream';
        var a = document.createElement('a');
        var blob = new Blob([content], {'type':contentType});
        a.href = window.URL.createObjectURL(blob);
        a.download = filename;
        a.click();
}