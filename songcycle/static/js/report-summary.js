$(document).ready(function () {

    $('#target-year').change(function() {

        const targetYearForm = $(this.form).serialize();
        const url = this.form.action;

        $.ajax({
            type: "POST",
            url: url,
            data:targetYearForm,
            dataType: "html"
        }).done(function (html) {
            $('#search-result').html(html);
        });
      });
});