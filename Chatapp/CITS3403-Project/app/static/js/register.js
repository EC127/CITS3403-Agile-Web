$(document).ready(function() {
  $('.register-form button[type="submit"]').on('click', function(event) {
    event.preventDefault();

    var username = $('#username').val().trim();
    var password = $('#password').val().trim();
    var confirm_password = $('#confirm-password').val().trim();
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

    // Check if the passwords match
    if (password !== confirm_password) {
      error = true;
      $('#confirm-password-error').text('Passwords do not match');
    } else {
      $('#confirm-password-error').text('');
    }

    // If there are no errors, submit the form
    if (!error) {
      $.ajax({
        url: '/register',
        type: 'POST',
        data: {
          username: username,
          password: password
        },
        success: function(response) {
          console.log(response);
          if (response.success === true) {
            window.location.href = '/login';
          } 
          else if (response.exist === true) {
            $('#register-error').text('Username already exists');
            setTimeout(function(){
              $('#register-error').text('');
            }, 3000);
          }
        }
      });
    }
    else {
      setTimeout(function(){
        $('#username-error').text('');
        $('#password-error').text('');
        $('#confirm-password-error').text('');
      }, 3000);
    }
  });
});
  