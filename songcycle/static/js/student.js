$(document).ready(function () {

    history.pushState(null, null, null);

    $(window).on("popstate", function (event) {
        history.pushState(null, null, null);
        window.alert('画面内のリンク、もしくはボタンを使って操作してください。');
    });

    //POSTの画面でEnterキー操作を制限する。
    $("#application").on('input,textarea[readonly]').not($('input[type="button"],input[type="submit"]')).keypress(function (e) {
        if (!e) var e = window.event;
        if (e.keyCode == 13)
            return false;
    });

    $("#report").click(function () {
        GetHtmlAsync(this.id, this.id, this.href)
        return false;
    });

    //後から動的に追加するとchangeイベントが発火しないことがあるので、
    //あらかじめ読み込んでおく。
    var inputTag = null;
    $("#application").on('click', "#report-create", function () {
        GetHtmlAsync(this.id, "report", this.href)
        inputTag = createFileInputTag();
        return false;
    });

    function createFileInputTag() {
        var input = document.createElement('input');
        input.type = 'file';
        input.accept = '.pdf,.xls,.xlsx,.doc,.docx, text/plain';
        input.onchange = function(event) {
            var file = event.target.files[0];
            var targetFile = file.name + " / " + file.size + " byte";

            //TODO:Ajaxでファイルアップロード。
            alert("ファイルアップロードに成功しました。");
            $("#file-name-label").text(targetFile);
        };

        return input;
    };

    $("#application").on('click', "#report-file", function(event) {
        inputTag.click();
    });

    $("#access-log").click(function () {
        GetHtmlAsync(this.id, this.id, this.href)
        return false;
    });

    $("#user-maintenance").click(function () {
        GetHtmlAsync(this.id, this.id, this.href)
        return false;
    });

    function GetHtmlAsync(id, group,  url){

        $.ajax({
            type: "GET",
            url: url,
            dataType: "html"
        }).done(function (html) {
            history.pushState('', '', id);
            $('#application').html(html);
            $('[name="function-title"]').removeClass("active");
            $('#' + group).find('p').addClass("active");
        });
    };
});