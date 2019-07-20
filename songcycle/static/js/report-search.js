$(document).ready(function () {

    $("#report").click(function () {

        $.ajax({
            type: "GET",
            url: this.href,
            dataType: "html"
        }).done(function (html) {
            history.pushState('', '', this.id);
            $('#application').html(html);
            $('[name="function-title"]').removeClass("active");
            $('#' + this.id).find('p').addClass("active");

            //初期検索をclickイベント発火させて実現しているが、もっと良い方法がありそうな気がする。
            $("#report-search").click();
        });

        return false;
    });

    $("#application").on('click', "#report-delete", function () {

        const group = "report";
        const link = $(this).find('[name="report-delete-link"]')[0];

        let fd = new FormData();
        fd.append('report_id', link.id);
        fd.append('current_page', $('#current-page')[0].value);

        overlay()
        $.ajax({
            type: "POST",
            url: link.href,
            data:fd,
            dataType: "html",
            processData : false,
            contentType: false
        }).done(function (html) {
            overlayClear(true)
            afterReportSearch(html, group);

        }).fail(function(jqXHR, textStatus, errorThrown){

            overlayClear(false)

            alert("このエラーが起きた場合は、管理者に問い合わせてください。");
        });
        
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

        const group = "report";
        const link = $('#paging-url')[0].href;

        let fd = new FormData();
        fd.append('current_page', $('#current-page')[0].value);

        if(this.id === "previous"){
            fd.append('previous', true);
        } else if(this.id === "next"){
            fd.append('next', true);
        } else {
            fd.append('target_page', this.id);
        }

        $.ajax({
            type: "POST",
            url: link,
            data:fd,
            dataType: "html",
            processData : false,
            contentType: false
        }).done(function (html) {
            afterReportSearch(html, group);
        });

        return false;
    });

    $("#application").on('click', '[name="sort-item"]', function () {
        const targetSortItem = this.id;
        const currentSortItem = $('#current-sort-item').val();
        const currentDescendingOrder = $('#current-descending-order').val();

        let target_descending_order = true;
        if(targetSortItem === currentSortItem){
            target_descending_order = (strToBool(currentDescendingOrder) == false);
        }

        let fd = new FormData();
        fd.append('target_sort_item', targetSortItem);
        fd.append('target_descending_order', BoolToUpperStr(target_descending_order));

        const group = "report";
        const link = $('#sort-url')[0].href;

        $.ajax({
            type: "POST",
            url: link,
            data:fd,
            dataType: "html",
            processData : false,
            contentType: false
        }).done(function (html) {
            afterReportSearch(html, group);
        });

        return false;
    });

    function afterReportSearch(html, group){

        $('#search-result').html(html);
        $('[name="function-title"]').removeClass("active");
        $('#' + group).find('p').addClass("active");

        var currentSortItem = $('#current-sort-item').val();
        var currentDescendingOrder = $('#current-descending-order').val();

        createPagingComponent('result-list-count', 'current-page', 'limit', 'report-pagination-area');
        setOrderIcon(currentSortItem, currentDescendingOrder);
    };
});