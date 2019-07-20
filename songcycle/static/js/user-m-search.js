$(document).ready(function () {

    $("#user-m").click(function () {

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
            $("#user-m-search").click();
        });

        return false;
    });

    $("#application").on('click', "#user-m-delete", function () {
        deleteData("user-m", $(this), "user_id");      
        return false;
    });

    $("#application").on('click', "#user-m-search", function () {

        const userSearchForm = $(this.form).serialize();
        const group = "user-m";

        $.ajax({
            type: "POST",
            url: this.form.action,
            data:userSearchForm,
            dataType: "html"
        }).done(function (html) {
            afterReportSearch(html, group);
        });
    });

    $("#application").on('click', '[name="user-m-paging"]', function () {
        paging("user-m", this.id);
        return false;
    });

    $("#application").on('click', '[name="user-m-sort-item"]', function () {
        sort("user-m", this.id);
        return false;
    });
});