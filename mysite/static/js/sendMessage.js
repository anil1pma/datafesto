function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function sendmessage() {
      var customer_name = $('#customerName').val();
      var customer_mail_id = $('#customerEmail').val();
      var customer_phone = $('#customerPhone').val();
      var customer_message = $('#customerMessage').val();
      data = JSON.stringify({
        'customer_name': customer_name,
        'customer_mail_id': customer_mail_id,
        'customer_phone': customer_phone,
        'customer_message': customer_message,
    });
      $.ajax({
        type: 'POST',
        url: "/polls/savedata/",
        data: data,
        beforeSend: function(request) {
            request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        },
        success: function(response) {
            if (response['message'] == 'SUCCESS') {
                 window.alert("Your query has been sent successfully.")
                 window.location = "/"
            }
        },
        dataType: 'json',
        contentType: 'application/json',
    });

}