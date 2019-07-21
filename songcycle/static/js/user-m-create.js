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

    $("#application").on('click', "#user-m-save", function(event) {
        
        $('[name="error-message"]').remove();

        let form = $('#user-m-save-form');
        const reportSaveForm = form.serialize();

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
                $("#report-file").prop("disabled", true);
                
                addSuccessMessage("#report-save-area");

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