$(document).ready(function () {

    history.pushState(null, null, null);

    $(window).on("popstate", function (event) {
        history.pushState(null, null, null);
        window.alert('画面内のリンク、もしくはボタンを使って操作してください。');
    });

    const showOpenFileDialog = () => {
        return new Promise(resolve => {
            const input = document.createElement('input');
            input.type = 'file';
            input.accept = '.txt, text/plain';
            input.onchange = event => { resolve(event.target.files[0]); };
            input.click();
        });
    };
    
    const readAsText = file => {
        return new Promise(resolve => {
            const reader = new FileReader();
            reader.readAsText(file);
            reader.onload = () => { resolve(reader.result); };
        });
    };
    
    (async () => {
        const file = await showOpenFileDialog();
        const content = await readAsText(file);
        alert(content);
    })();


    $("#application").on('click', "#report-file", function(event) {
        showOpenFileDialog();
    });

    //POSTの画面でEnterキー操作を制限する。
    $("#application").on('input,textarea[readonly]').not($('input[type="button"],input[type="submit"]')).keypress(function (e) {
        if (!e) var e = window.event;
        if (e.keyCode == 13)
            return false;
    });

    $("#report").click(function () {
        GetHtmlAsync(this.id, this.id, this.href)
        return false;
    });

    $("#application").on('click', "#report-create", function () {
        GetHtmlAsync(this.id, "report", this.href)
        return false;
    });

    $("#access-log").click(function () {
        GetHtmlAsync(this.id, this.id, this.href)
        return false;
    });

    $("#user-maintenance").click(function () {
        GetHtmlAsync(this.id, this.id, this.href)
        return false;
    });

    function GetHtmlAsync(id, group,  url){

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
    };
});