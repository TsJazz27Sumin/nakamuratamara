$(document).ready(function () {

    //POSTの画面でEnterキー操作を制限する。
    $("#application").on('input,textarea[readonly]').not($('input[type="button"],input[type="submit"]')).keypress(function (e) {
        if (!e) var e = window.event;
        if (e.keyCode == 13)
            return false;
    });

    $("#report").click(function () {
        GetHtmlAsync(this.id, this.id, this.href)
        return false;
    });

    $("#application").on('click', "#report-create", function () {
        GetHtmlAsync(this.id, "report", this.href)
        return false;
    });

    $("#access-log").click(function () {
        GetHtmlAsync(this.id, this.id, this.href)
        return false;
    });

    $("#user-maintenance").click(function () {
        GetHtmlAsync(this.id, this.id, this.href)
        return false;
    });

    function GetHtmlAsync(id, group,  url){

        $.ajax({
            type: "GET",
            url: url,
            dataType: "html"
        }).done(function (html) {
            history.pushState('', '', id);
            $('#application').html(html);
            $('[name="function-title"]').removeClass("active");
            $('#' + group).find('p').addClass("active");
        });
    };
});