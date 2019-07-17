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

    //後から動的に追加するとchangeイベントが発火しないことがあるので、
    //あらかじめ読み込んでおく。
    var inputTag = null;
    $("#application").on('click', "#report-create", function () {

        var id = this.id;
        var group = "report";
        var url = this.href;

        $.ajax({
            type: "GET",
            url: url,
            dataType: "html"
        }).done(function (html) {
            history.pushState('', '', id);
            $('#application').html(html);
            $('[name="function-title"]').removeClass("active");
            $('#' + group).find('p').addClass("active");

            var now = new Date();
            var y = now.getFullYear();

            $('[name="target-years"]').each(function() {
                if($(this).val() == y){
                    $(this).attr("selected","selected");
                }
            });

            var fileUploadUrl = $(html).find('#file-upload-url').attr("href");
            inputTag = createFileInputTag(fileUploadUrl);
        });
        
        return false;
    });

    function createFileInputTag(fileUploadUrl) {
        var input = document.createElement('input');
        input.type = 'file';
        input.accept = '.docx, text/plain';
        input.onchange = function(event) {
            var file = event.target.files[0]

            if (file.size > 10485760){
                addErrorMessage('report-file', 'This file is too big. Limitation is 10MB.');
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

    $("#application").on('click', "#report-save", function(event) {
        
        $('[name="error-message"]').remove();

        var form = $('#report-save-form');
        var reportSaveForm = form.serialize();

        overlay()

        $.ajax({
            url  : form[0].action,
            type : "POST",
            data : reportSaveForm,
            dataType : "json",
        }).done(function(json){

            var data = json.data;

            if(strToBool(data.result)){
                overlayClear(false)
                $("#report-file").prop("disabled", true);
                
                addSuccessMessage("#report-save-area");

                $('#report-save-area').remove();
                $('#seq-report-create').removeClass("continue-to-register-none");
                $('#seq-report-create').addClass("continue-to-register");
            } else {
                overlayClear(true);
                addErrorMessage(data.errorItem, data.errorMessage);
            }

        }).fail(function(jqXHR, textStatus, errorThrown){

            overlayClear(false)

            alert("このエラーが起きた場合は、管理者に問い合わせてください。");
        });
    });

    $("#application").on('click', "#report-delete", function () {

        var group = "report";
        var link = $(this).find('[name="report-delete-link"]')[0];

        var fd = new FormData();
        fd.append('report_id', link.id);

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
            
            $('#search-result').html(html);
            $('[name="function-title"]').removeClass("active");
            $('#' + group).find('p').addClass("active");

        }).fail(function(jqXHR, textStatus, errorThrown){

            overlayClear(false)

            alert("このエラーが起きた場合は、管理者に問い合わせてください。");
        });
        
        return false;
    });

    $("#application").on('click', "#report-download", function () {

        var link = $(this).find('[name="report-download-link"]')[0];

        var a = document.createElement("a");
        a.href = link;
        a.download = "test.docx";
        a.click();

        //ダウンロード数をカウントアップするために遅延実行。
        setTimeout(function(){
            $("#report-search").click();
       },5000);
    });

    $("#application").on('click', "#report-search", function () {

        var reportSearchForm = $(this.form).serialize();
        var group = "report";

        $.ajax({
            type: "POST",
            url: this.form.action,
            data:reportSearchForm,
            dataType: "html"
        }).done(function (html) {
            $('#search-result').html(html);
            $('[name="function-title"]').removeClass("active");
            $('#' + group).find('p').addClass("active");
        });
    });
});