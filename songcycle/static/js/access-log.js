$(document).ready(function () {

    $("#access-log").click(function () {

        const group = this.id;
        const url = this.href;

        $.ajax({
            type: "GET",
            url: url,
            dataType: "html"
        }).done(function (html) {
            history.pushState('', '', url);
            $('#application').html(html);
            $('[name="function-title"]').removeClass("active");
            $('#' + group).find('p').addClass("active");
        });

        return false;
    });

    $("#application").on('click', "#access-log-download", function () {

        const link = $(this).find('[name="access-log-download-link"]')[0];

        let a = document.createElement("a");
        a.href = link;
        a.download = "test.csv";
        a.click();
    });
});