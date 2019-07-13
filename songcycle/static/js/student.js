$(document).ready(function () {

    //ブラウザ操作の戻る禁止
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

    //CSRF
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    //ここからAjaxのトリガー

    $("#report").click(function () {
        GetHtmlAsync(this.id, this.id, this.href)
        return false;
    });

    //後から動的に追加するとchangeイベントが発火しないことがあるので、
    //あらかじめ読み込んでおく。
    var inputTag = null;
    $("#application").on('click', "#report-create", function () {

        id = this.id;
        group = "report";
        url = this.href;

        $.ajax({
            type: "GET",
            url: url,
            dataType: "html"
        }).done(function (html) {
            history.pushState('', '', id);
            $('#application').html(html);
            $('[name="function-title"]').removeClass("active");
            $('#' + group).find('p').addClass("active");

            var fileUploadUrl = $(html).find('#file-upload-url').attr("href");
            inputTag = createFileInputTag(fileUploadUrl);
        });
        
        return false;
    });

    function createFileInputTag(fileUploadUrl) {
        var input = document.createElement('input');
        input.type = 'file';
        input.accept = '.pdf,.xls,.xlsx,.doc,.docx, text/plain';
        input.onchange = function(event) {
            var file = event.target.files[0]

            if (file.size > 1073741824){
                alert("ファイルサイズが大きすぎます。 > " + file.size + "byte");
                return false;
            }

            var targetFile = file.name + " / " + file.size + " byte";

            var fd = new FormData();
            fd.append('file_source', file);

            $.ajax({
                url  : fileUploadUrl,
                type : "POST",
                data : fd,
                dataType : "json",
                enctype : "multipart/form-data",
                processData : false,
                contentType: false
            }).done(function(json){
                if(json.data.message === "Success"){
                    $("#file-path").val(json.data.filePath);
                    $("#file-name").val(file.name);
                    $("#file-name-label").text(targetFile);
                }
                if(json.data.message === "Error"){
                    $("#file-name-label").text("ファイルアップロードに失敗しました。");
                }
            }).fail(function(jqXHR, textStatus, errorThrown){
                $("#file-name-label").text("ファイルアップロードに失敗しました。");
            });
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

    function GetHtmlAsync(id, group, url){

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