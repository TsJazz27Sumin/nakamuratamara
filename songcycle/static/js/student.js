$(document).ready(function () {

    //TODO:js側のライブラリ管理ツール導入

    //ブラウザ操作の戻る禁止
    history.pushState(null, null, null);

    $(window).on("popstate", function (event) {
        history.pushState(null, null, null);
        window.alert('画面内のリンク、もしくはボタンを使って操作してください。');
    });

    //POSTの画面でEnterキー操作を制限する。
    $("#application").on('input,textarea[readonly]').not($('input[type="button"],input[type="submit"]')).keypress(function (e) {
        if (!e) var e = window.event;
        if (e.keyCode == 13)
            return false;
    });

    //CSRF
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                let cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    let csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});