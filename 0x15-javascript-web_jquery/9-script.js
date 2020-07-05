const $ = window.$;
$(document).ready(function () {
  const a = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.getJSON(a, function (data) {
    $('DIV#hello').html(data.hello);
  });
});
