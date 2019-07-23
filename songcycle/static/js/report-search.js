$(document).ready(function () {

    $("#report").click(function () {

        const id = this.id;
        const url = this.href;

        $.ajax({
            type: "GET",
            url: url,
            dataType: "html"
        }).done(function (html) {
            history.pushState('', '', url);
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
        const url = this.form.action;

        $.ajax({
            type: "POST",
            url: url,
            data:reportSearchForm,
            dataType: "html"
        }).done(function (html) {
            history.pushState('', '', url);
            afterReportSearch(html, group);
        });
    });

    $("#application").on('click', "#report-search-sp", function () {

        const reportSearchForm = $(this.form).serialize();
        const group = "report";
        const url = this.form.action;

        $.ajax({
            type: "POST",
            url: url,
            data:reportSearchForm,
            dataType: "html"
        }).done(function (html) {
            history.pushState('', '', url);
            $('#search-result').html(html);
            $('[name="function-title"]').removeClass("active");
            $('#' + group).find('p').addClass("active");
        });
    });

    $("#application").on('click', '[name="report-paging"]', function () {
        paging("report", this.id);
        return false;
    });

    $("#application").on('click', '[name="report-sort-item"]', function () {
        sort("report", this.id);
        return false;
    });
});