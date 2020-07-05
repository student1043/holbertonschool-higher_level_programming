const $ = window.$;
$('DIV#toggle_header').click(function () {
  if ($('header').hasClass('red')) {
    $('header').toggleClass('green').removeClass('red');
  } else {
    $('header').toggleClass('red').removeClass('green');
  }
});
