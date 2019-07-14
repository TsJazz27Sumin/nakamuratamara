$(document).ready(function () {

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

    $("#application").on('click', "#report-save", function(event) {
        
        var form = $('#report-save-form');
        var reportSaveForm = form.serialize();

        $.ajax({
            url  : form[0].action,
            type : "POST",
            data : reportSaveForm,
            dataType : "json",
        }).done(function(json){
            if(json.data.message === "Success"){
                alert(json.data.message);
            }
            if(json.data.message === "Error"){
                alert(json.data.message);
            }
        }).fail(function(jqXHR, textStatus, errorThrown){
            alert("Error");
        });
    });
});