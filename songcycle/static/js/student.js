$(document).ready(function () {

    $("#report").click(function () {

        id = this.id
        
        $.ajax({
            type: "GET",
            url: this.href,
            dataType: "html"
        }).done(function (html) {
            history.pushState('', '', id);
            $('#application').html(html);
        });

        return false;
    });

    $("#application").on('click', "#report-create", function () {

        id = this.id
        
        $.ajax({
            type: "GET",
            url: this.href,
            dataType: "html"
        }).done(function (html) {
            history.pushState('', '', id);
            $('#application').html(html);
        });

        return false;
    });

    $("#access-log").click(function () {

        id = this.id
        
        $.ajax({
            type: "GET",
            url: this.href,
            dataType: "html"
        }).done(function (html) {
            history.pushState('', '', id);
            $('#application').html(html);
        });

        return false;
    });

    $("#user-maintenance").click(function () {

        id = this.id

        $.ajax({
            type: "GET",
            url: this.href,
            dataType: "html"
        }).done(function (html) {
            history.pushState('', '', id);
            $('#application').html(html);
        });

        return false;
    });
});