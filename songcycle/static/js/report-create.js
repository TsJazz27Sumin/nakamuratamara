$(document).ready(function () {

    //後から動的に追加するとchangeイベントが発火しないことがあるので、
    //あらかじめ読み込んでおく。
    let inputTag = null;
    $("#application").on('click', "#report-create", function () {

        const group = "report";
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

            const now = new Date();
            const y = now.getFullYear();

            $('[name="target-years"]').each(function() {
                if($(this).val() == y){
                    $(this).attr("selected","selected");
                }
            });

            const fileUploadUrl = $(html).find('#file-upload-url').attr("href");
            inputTag = createFileInputTag(fileUploadUrl);
        });
        
        return false;
    });

    function createFileInputTag(fileUploadUrl) {
        let input = document.createElement('input');
        input.type = 'file';
        input.accept = '.docx, text/plain';
        input.onchange = function(event) {
            const file = event.target.files[0]

            if (file.size > 10485760){
                addErrorMessage('report-file', 'This file is too big. Limitation is 10MB.');
                return false;
            }

            const targetFile = file.name + " / " + file.size + " byte";

            let fd = new FormData();
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

        let form = $('#report-save-form');
        const reportSaveForm = form.serialize();
        const url = form[0].action;

        overlay()

        $.ajax({
            url  : form[0].action,
            type : "POST",
            data : reportSaveForm,
            dataType : "json",
        }).done(function(json){

            const data = json.data;

            if(strToBool(data.result)){
                overlayClear(false)
                history.pushState('', '', url);
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
});