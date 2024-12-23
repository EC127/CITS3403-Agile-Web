$(document).ready(function() {
  $('.login-form button[type="submit"]').on('click', function(event) {
    event.preventDefault();
    
    var username = $('#username').val().trim();
    var password = $('#password').val().trim();
    var error = false;

    // Check if the username is empty
    if (username === '') {
      error = true;
      $('#username-error').text('Username cannot be empty');
    } else {
      $('#username-error').text('');
    }

    // Check if the password is empty
    if (password === '') {
      error = true;
      $('#password-error').text('Password cannot be empty');
    } else {
      $('#password-error').text('');
    }

    // If there are no errors, submit the form
    if (!error) {
      $.ajax({
        url: '/login',
        type: 'POST',
        data: {
          username: username,
          password: password
        },
        success: function(response) {
          console.log(response);
          if (response.success === true) {
            window.location.href = '/chat';
          } 
          else if (response.invalid === true) {
            $('#login-error').text('Invalid username or password');
            setTimeout(function(){
              $('#login-error').text('');
            }, 3000);          
          }
        }
      });
    } 
    else {
        setTimeout(function(){
          $('#username-error').text('');
          $('#password-error').text('');
        }, 3000);
    }
  });  
});

