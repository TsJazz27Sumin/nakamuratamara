$(document).ready(function () {

    $("#report").click(function () {
        GetHtmlAsync(this.id, this.href)
        return false;
    });

    $("#application").on('click', "#report-create", function () {
        GetHtmlAsync(this.id, this.href)
        return false;
    });

    $("#access-log").click(function () {
        GetHtmlAsync(this.id, this.href)
        return false;
    });

    $("#user-maintenance").click(function () {
        GetHtmlAsync(this.id, this.href)
        return false;
    });

    function GetHtmlAsync(id, url){

        $.ajax({
            type: "GET",
            url: url,
            dataType: "html"
        }).done(function (html) {
            history.pushState('', '', id);
            $('#application').html(html);
            $('[name="function-title"]').removeClass("active");
            $('#' + id).find('p').addClass("active");
        });
    };
});