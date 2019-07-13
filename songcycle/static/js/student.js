document.addEventListener("keydown", function (e) {
 
    if ((e.which || e.keyCode) == 116 ) {
        e.preventDefault();
    }
 
});

$(document).ready(function () {

    $("#report").click(function () {
        GetHtmlAjax(this.id, this.href)
        return false;
    });

    $("#application").on('click', "#report-create", function () {
        GetHtmlAjax(this.id, this.href)
        return false;
    });

    $("#access-log").click(function () {
        GetHtmlAjax(this.id, this.href)
        return false;
    });

    $("#user-maintenance").click(function () {
        GetHtmlAjax(this.id, this.href)
        return false;
    });

    function GetHtmlAjax(id, url){

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