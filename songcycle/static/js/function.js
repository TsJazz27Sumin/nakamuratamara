function overlay(){
    $("#body-area").addClass("overlay");
    $("input").each( function() {
        $(this).attr('disabled',true);
    });
    $("select").each( function() {
        $(this).attr('disabled',true);
    });
    $("button").each( function() {
        $(this).addClass("disable-button");
    });
};

function overlayClear(isDisabledRefresh){
    $("#body-area").removeClass("overlay");

    if (isDisabledRefresh){
        $("input").each( function() {
            $(this).attr('disabled',false);
        });
        $("select").each( function() {
            $(this).attr('disabled',false);
        });
        $("button").each( function() {
            $(this).removeClass("disable-button");
        });
    }
};

function strToBool(value){
    if(value === "true"){
        return true;
    }

    return false;
};

function addSuccessMessage(id){
    $(id).after('<p class="font-weight-bold text-success">Success!!!</p>');
};

function addErrorMessage(errorItem, errorMessage){
    errorItemList = errorItem.split(',');
    errorMessageList = errorMessage.split(',');

    for(let i = 0; i < errorItemList.length; i++){
        $("#" + errorItemList[i]).after('<p name="error-message" class="text-danger">' + errorMessageList[i] + '</p>');
    }
};
