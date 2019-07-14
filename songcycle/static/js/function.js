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

function overlayClear(){
    $("#body-area").removeClass("overlay");
    $("input").each( function() {
        $(this).attr('disabled',false);
    });
    $("select").each( function() {
        $(this).attr('disabled',false);
    });
    $("button").each( function() {
        $(this).removeClass("disable-button");
    });
};