
$(document).ready(function(){

$('.action_btn').click(function(){

$.ajax({
      type : 'POST',
      url : "/download_scrap",
      data : {'file':$(this).val()},
      success:function(data){
        console.log(data)
        var temp = data.toString().toLowerCase();
        download(temp, $(this).val(), "text/csv");
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
