$(document).ready(function() {
    var $temp = $('<input>');
    var $url = $(location).attr('href');
    $(".link").click(function() {
    $("body").append($temp);
    $temp.val($url).select();
    document.execCommand("copy");
    $temp.remove();
    $("p").text("Link Copied!");
    });
});
