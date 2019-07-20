$(document).ready(function () {

    $("#report").click(function () {

        id = this.id;

        $.ajax({
            type: "GET",
            url: this.href,
            dataType: "html"
        }).done(function (html) {
            history.pushState('', '', id);
            $('#application').html(html);
            $('[name="function-title"]').removeClass("active");
            $('#' + id).find('p').addClass("active");

            //初期検索をclickイベント発火させて実現しているが、もっと良い方法がありそうな気がする。
            $("#report-search").click();
        });

        return false;
    });

    $("#application").on('click', "#report-delete", function () {
        deleteData("report", $(this), "report_id");      
        return false;
    });

    $("#application").on('click', "#report-download", function () {

        const link = $(this).find('[name="report-download-link"]')[0];

        let a = document.createElement("a");
        a.href = link;
        a.download = "test.docx";
        a.click();

        //ダウンロード数をカウントアップするために遅延実行。
        setTimeout(function(){
            $("#report-search").click();
       },5000);
    });

    $("#application").on('click', "#report-search", function () {

        const reportSearchForm = $(this.form).serialize();
        const group = "report";

        $.ajax({
            type: "POST",
            url: this.form.action,
            data:reportSearchForm,
            dataType: "html"
        }).done(function (html) {
            afterReportSearch(html, group);
        });
    });

    $("#application").on('click', '[name="paging"]', function () {
        paging("report", this.id);
        return false;
    });

    $("#application").on('click', '[name="sort-item"]', function () {
        sort("report", this.id);
        return false;
    });
});