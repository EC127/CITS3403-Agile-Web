$(document).ready(function () {
  const resultDiv = $('.search-result');
  const searchBtn = $('.search_form button[type="submit"]');

  searchBtn.on('click', function (event) {
    const search_check = $('#keyword').val().trim();
   
    event.preventDefault(); // stop form from submitting

    //disable search button
    searchBtn.prop('disabled', true);

    var searchValue = $('#keyword').val().trim();

    $.ajax({
      url: '/search',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({query: searchValue}),
      dataType: 'json',
      success: function(data){
        $('#keyword').val(''); // empty search bar
        console.log(data);
        resultDiv.empty(); // empty search result
        if (data.results.length > 0) {
          for (let i = 0; i < data.results.length; i++) {
            const content = data.results[i].content;
            const timestamp = data.results[i].timestamp;
            const sender = data.results[i].sender;
            // create new list element
            const listItem = $('<div>').addClass('search-result-item').text(content);
            const timestampItem = $('<span>').addClass('timestamp').text(timestamp);
            const senderItem = $('<span>').addClass('sender').text(sender);
            resultDiv.append(listItem).append(timestampItem).append(senderItem);
          }
        }
        else {
          resultDiv.addClass('warning');
          resultDiv.text('No results found.');
        }
      },
      error: function(xhr, status, error) {
        console.error(xhr.responseText);
        resultDiv.text('Search failed. Please try again later.');
      },
      complete: function() {
        //enable search button
        searchBtn.prop('disabled', false);
      }
    });
  });
});
