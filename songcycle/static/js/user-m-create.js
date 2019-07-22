$(document).ready(function () {

    $("#application").on('click', "#user-m-create", function () {

        const id = this.id;
        const group = "user-m";
        const url = this.href;

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
        
        return false;
    });

    $("#application").on('click', '[name="user-m-update-link"]', function () {

        const id = this.id;
        const group = "user-m";
        const url = this.href;

        let fd = new FormData();
        fd.append('user_id', id);

        $.ajax({
            type: "POST",
            url: url,
            data:fd,
            dataType: "html",
            processData : false,
            contentType: false
        }).done(function (html) {
            $('#application').html(html);
            $('[name="function-title"]').removeClass("active");
            $('#' + group).find('p').addClass("active");
        });
        
        return false;
    });

    $("#application").on('click', "#user-m-save", function(event) {
        
        $('[name="error-message"]').remove();

        let form = $('#user-m-save-form');
        const userSaveForm = form.serialize();

        overlay()

        $.ajax({
            url  : form[0].action,
            type : "POST",
            data : userSaveForm,
            dataType : "json",
        }).done(function(json){

            const data = json.data;

            if(strToBool(data.result)){
                overlayClear(false)
                
                addSuccessMessage("#user-m-save-area");

                $('#user-m-save-area').remove();
                $('#seq-user-m-create').removeClass("continue-to-register-none");
                $('#seq-user-m-create').addClass("continue-to-register");
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