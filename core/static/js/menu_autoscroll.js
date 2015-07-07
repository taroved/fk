function top_menu()
{
    var eTop = $("#success_country").offset().top; //get the offset top of the element
    var pos = eTop - $(window).scrollTop();
    if (pos < -72) {
        $("#success_country .menu").css({'position': 'fixed', 'top': '0'});
        $("#success_country .items").css({'margin-left': (342+5+45)+'px'});
    }
    else {
        $("#success_country .menu").css({'position': 'inherit', 'top': '0'});
        $("#success_country .items").css({'margin-left': 45+'px'});
    }
}

$(window).on("load resize scroll",function(e){
    top_menu()
});