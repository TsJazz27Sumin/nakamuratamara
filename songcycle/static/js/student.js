document.addEventListener("keydown", function (e) {
 
    if ((e.which || e.keyCode) == 116 ) {
        e.preventDefault();
    }
 
});

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
            $('[name="function-title"]').removeClass("active");
            $('#' + id).find('p').addClass("active");
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
            $('[name="function-title"]').removeClass("active");
            $('#' + id).find('p').addClass("active");
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
            $('[name="function-title"]').removeClass("active");
            $('#' + id).find('p').addClass("active");
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
            $('[name="function-title"]').removeClass("active");
            $('#' + id).find('p').addClass("active");
        });

        return false;
    });
});