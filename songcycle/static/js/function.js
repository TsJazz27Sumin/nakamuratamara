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
    if(value.toLowerCase() === "true"){
        return true;
    }

    return false;
};

function BoolToUpperStr(value){
    if(value === true){
        return "True";
    }

    return "False";
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

function createPagingComponent(resultListCountId, currentPageId, limitId, paginationId){

    const resultListCount = $('#' + resultListCountId).val();
    const currentPage = $('#' + currentPageId).val();
    const limit = $('#' + limitId).val();
    let $pagination = $('#' + paginationId);

    let totalPage = Math.ceil(resultListCount / limit);

    if (totalPage > 1){
        $pagination.append('<li class="page-item ' + (currentPage == 1 ? 'disabled':'') + '">' + (currentPage == 1 ? '<span class="page-link" >Previous</span>':'<a id="previous" name="paging" class="page-link" href="#" tabindex="-1">Previous</a>') + '</li>');
        
        for (let i = 1; i <= totalPage; i++){
            $pagination.append('<li class="page-item ' + (currentPage == i ? 'active':'') + '"><a id="' + i + '" name="paging" class="page-link" href="#">' + i + '</a></li>');
        }
        
        $pagination.append('<li class="page-item ' + (currentPage == totalPage ? 'disabled':'') + '">' + (currentPage == totalPage ? '<span class="page-link" >Next</span>':'<a id="next" name="paging" class="page-link" href="#">Next</a>') + '</li>');
    }
};

function setOrderIcon(currentSortItem, currentDescendingOrder){
    $currentSortItemSpan = $('#' + currentSortItem).find('span');
    currentDescendingOrder = currentDescendingOrder;
    
    if(strToBool(currentDescendingOrder)){
        $currentSortItemSpan.addClass('glyphicon glyphicon-arrow-up');
    } else {
        $currentSortItemSpan.addClass('glyphicon glyphicon-arrow-down');
    }
}
