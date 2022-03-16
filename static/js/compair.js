
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
      $('#table_data').append(data['data']);
      $('#table_data').css('max-height','200px');
      $('#table_data').css('overflow','scroll');
      },
    });
  });


$('.pagination').jqPagination({
    max_page    : $('.some-container p').length,
        paged        : function(page) {

            // a new 'page' has been requested

            // hide all paragraphs
            $('.some-container p').hide();

            // but show the one we want
            $($('.some-container p')[page - 1]).show();
    }
});
