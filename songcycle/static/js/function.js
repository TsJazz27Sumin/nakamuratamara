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

function createPagingComponent(resultListCountId, currentPageId, limitId, paginationId, group){

    const resultListCount = $('#' + resultListCountId).val();
    const currentPage = $('#' + currentPageId).val();
    const limit = $('#' + limitId).val();
    let $pagination = $('#' + paginationId);

    let totalPage = Math.ceil(resultListCount / limit);

    if (totalPage > 1){
        $pagination.append('<li class="page-item ' + (currentPage == 1 ? 'disabled':'') + '">' + (currentPage == 1 ? '<span class="page-link" >Previous</span>':'<a id="previous" name="' + group + '-paging" class="page-link" href="#" tabindex="-1">Previous</a>') + '</li>');
        
        for (let i = 1; i <= totalPage; i++){
            $pagination.append('<li class="page-item ' + (currentPage == i ? 'active':'') + '"><a id="' + i + '" name="' + group + '-paging" class="page-link" href="#">' + i + '</a></li>');
        }
        
        $pagination.append('<li class="page-item ' + (currentPage == totalPage ? 'disabled':'') + '">' + (currentPage == totalPage ? '<span class="page-link" >Next</span>':'<a id="next" name="' + group + '-paging" class="page-link" href="#">Next</a>') + '</li>');
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
};

function afterReportSearch(html, group){

    $('#search-result').html(html);
    $('[name="function-title"]').removeClass("active");
    $('#' + group).find('p').addClass("active");

    var currentSortItem = $('#current-sort-item').val();
    var currentDescendingOrder = $('#current-descending-order').val();

    createPagingComponent('result-list-count', 'current-page', 'limit', 'pagination-area', group);
    setOrderIcon(currentSortItem, currentDescendingOrder);
};

function sort(group, id){
    const targetSortItem = id;
    const currentSortItem = $('#current-sort-item').val();
    const currentDescendingOrder = $('#current-descending-order').val();

    let target_descending_order = true;
    if(targetSortItem === currentSortItem){
        target_descending_order = (strToBool(currentDescendingOrder) == false);
    }

    let fd = new FormData();
    fd.append('target_sort_item', targetSortItem);
    fd.append('target_descending_order', BoolToUpperStr(target_descending_order));

    const link = $('#sort-url')[0].href;

    $.ajax({
        type: "POST",
        url: link,
        data:fd,
        dataType: "html",
        processData : false,
        contentType: false
    }).done(function (html) {
        history.pushState('', '', link);
        afterReportSearch(html, group);
    });
};

function paging(group, id){
    const url = $('#paging-url')[0].href;

    let fd = new FormData();
    fd.append('current_page', $('#current-page')[0].value);

    if(id === "previous"){
        fd.append('previous', true);
    } else if(id === "next"){
        fd.append('next', true);
    } else {
        fd.append('target_page', id);
    }

    $.ajax({
        type: "POST",
        url: url,
        data:fd,
        dataType: "html",
        processData : false,
        contentType: false
    }).done(function (html) {
        history.pushState('', '', url);
        afterReportSearch(html, group);
    });
};

function deleteData(group, target, idName) {

    const link = target.find('[name="' + group + '-delete-link"]')[0];
    const url = link.href;

    let fd = new FormData();
    fd.append(idName, link.id);
    fd.append('current_page', $('#current-page')[0].value);

    overlay()
    $.ajax({
        type: "POST",
        url: url,
        data:fd,
        dataType: "html",
        processData : false,
        contentType: false
    }).done(function (html) {
        overlayClear(true)
        history.pushState('', '', url);
        afterReportSearch(html, group);

    }).fail(function(jqXHR, textStatus, errorThrown){

        overlayClear(false)

        alert("このエラーが起きた場合は、管理者に問い合わせてください。");
    });
};