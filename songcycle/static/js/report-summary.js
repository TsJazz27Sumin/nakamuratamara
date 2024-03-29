$(window).on('load', function () {

    const form = $('#report-summary-form');
    const targetYearForm = form.serialize();
    const url = form[0].action;

    $.ajax({
        type: "POST",
        url: url,
        data: targetYearForm,
        dataType: "html"
    }).done(function (html) {
        $('#search-result').html(html);
    });
});

$(document).ready(function () {

    $('#target-year').change(function () {

        const targetYearForm = $(this.form).serialize();
        const url = this.form.action;

        $.ajax({
            type: "POST",
            url: url,
            data: targetYearForm,
            dataType: "html"
        }).done(function (html) {
            $('#search-result').html(html);
        });
    });

    $("#search-result").on('click', "#report-download", function () {

        const link = $(this).find('[name="report-download-link"]')[0];

        let a = document.createElement("a");
        a.href = link;
        a.download = "test.docx";
        a.click();
    });
});