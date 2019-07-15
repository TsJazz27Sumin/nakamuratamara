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

function str_to_bool(value){
    if(value === "true"){
        return true;
    }

    return false;
}