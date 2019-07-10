$(document).ready(function () {
    $("#report").click(function () {

        targetUrl = window.location.href + this.id;

        $.ajax({
            type: "GET",
            url: targetUrl,
            dataType: "json"
        }).done(function (data) {
            $('#application').html(data.message);
        });
    });
});