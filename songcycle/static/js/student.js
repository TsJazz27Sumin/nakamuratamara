$(document).ready(function () {
    $("#report").click(function () {

        //TODO:root urlの判定をどうにかしたい。
        id = this.id;
        targetUrl = "http://127.0.0.1:8000/student/home/" + id;

        $.ajax({
            type: "GET",
            url: targetUrl,
            dataType: "json"
        }).done(function (data) {
            history.pushState('', '', id);
            $('#application').html(data.message);
        });
    });

    $("#access-log").click(function () {

        //TODO:root urlの判定をどうにかしたい。
        id = this.id;
        targetUrl = "http://127.0.0.1:8000/student/home/" + id;

        $.ajax({
            type: "GET",
            url: targetUrl,
            dataType: "json"
        }).done(function (data) {
            history.pushState('', '', id);
            $('#application').html(data.message);
        });
    });

    $("#user-maintenance").click(function () {

        //TODO:root urlの判定をどうにかしたい。
        id = this.id;
        targetUrl = "http://127.0.0.1:8000/student/home/" + id;

        $.ajax({
            type: "GET",
            url: targetUrl,
            dataType: "json"
        }).done(function (data) {
            history.pushState('', '', id);
            $('#application').html(data.message);
        });
    });
});