
$(document).ready(function(){

$('.action_btn').click(function(){

$.ajax({
      type : 'POST',
      url : "/download_scrap",
      data : {'file':$(this).val()},
      success:function(data){
        download(data, $(this).val(), "text/csv");
      },
    });

})
function download(content, filename, contentType)
{
    if(!contentType) contentType = 'application/octet-stream';
        var a = document.createElement('a');
        var blob = new Blob([content], {'type':contentType});
        a.href = window.URL.createObjectURL(blob);
        a.download = filename;
        a.click();
}
})

function download_file_scrap(path){

window.location.href = path;


}