const $ = window.$;
const a = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.getJSON(a, function (data) {
  $.each(data.results, function (count, movie) {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  });
});
