$(document).ready(function() {
    $('#upload-form').on('submit', function(event) {
        event.preventDefault();
        var formData = new FormData(this);
        $.ajax({
            url: '/upload/',
            type: 'POST',
            data: formData,
            success: function(data) {
                if (data.error) {
                    alert(data.error);
                } else {
                    $('#image-preview').attr('src', data.image_url);
                    $('#settings-form').show();
                }
            },
            cache: false,
            contentType: false,
            processData: false
        });
    });

    $('#settings-form').on('submit', function(event) {
        event.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            url: '/convert/',
            type: 'POST',
            data: formData,
            success: function(data) {
                if (data.error) {
                    alert(data.error);
                } else {
                    $('#download-link').attr('href', data.pdf_url);
                    $('#download-link').show();
                }
            }
        });
    });
});