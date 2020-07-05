const $ = window.$;
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const language = $('INPUT#language_code').val();
    const link = 'https://www.fourtonfish.com/hellosalut/?lang=' + language;
    $.getJSON(link, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
