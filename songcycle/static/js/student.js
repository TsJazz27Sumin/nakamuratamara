$(document).ready(function () {
    $("#report").click(function () {

        //TODO:root urlの判定をどうにかしたい。
        id = this.id;
        targetUrl = "http://127.0.0.1:8000/student/home/" + id;

        $.ajax({
            type: "GET",
            url: targetUrl,
            dataType: "html"
        }).done(function (html) {
            history.pushState('', '', id);
            $('#application').html(html);
        });
    });

    $("#access-log").click(function () {

        //TODO:root urlの判定をどうにかしたい。
        id = this.id;
        targetUrl = "http://127.0.0.1:8000/student/home/" + id;

        $.ajax({
            type: "GET",
            url: targetUrl,
            dataType: "html"
        }).done(function (html) {
            history.pushState('', '', id);
            $('#application').html(html);
        });
    });

    $("#user-maintenance").click(function () {

        //TODO:root urlの判定をどうにかしたい。
        id = this.id;
        targetUrl = "http://127.0.0.1:8000/student/home/" + id;

        $.ajax({
            type: "GET",
            url: targetUrl,
            dataType: "html"
        }).done(function (html) {
            history.pushState('', '', id);
            $('#application').html(html);
        });
    });
});