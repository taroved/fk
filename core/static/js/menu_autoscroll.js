function top_menu()
{
    var contTop = $("#success_country").offset().top; //get the offset top of the element
    var top_pos = contTop - $(window).scrollTop(); //menu container top

    // menu top offset if it is in bottom of container
    var bottomMenuTop = $("#success_country").offset().top + $("#success_country").height() - $("#success_country .menu").height();
    // positive if we have place for menu in bottom 
    var menu_pos = bottomMenuTop - $(window).scrollTop();
    
    var marginTop = 72
    if (top_pos < -marginTop && menu_pos >= -marginTop) {
        $("#success_country .menu").css({'position': 'fixed', 'top': '0', 'vertical-align': 'baseline'});
        $("#success_country .items").css({'margin-left': (342+5+45)+'px'});
        console.log({type: 1, top_pos: top_pos, menu_pos: menu_pos})
    }
    else if (menu_pos < -marginTop) { 
        $("#success_country .menu").css({
            'position': 'inherit',
            // if we have no place in bottom
            // we position menu to bootm
            'vertical-align': 'bottom'
            });
        $("#success_country .items").css({'margin-left': 45+'px'});
        console.log({type: 2, top_pos: top_pos, menu_pos: menu_pos})
    }
    else {
        $("#success_country .menu").css({'position': 'inherit', 'vertical-align': 'top'});
        $("#success_country .items").css({'margin-left': 45+'px'});
        console.log({type: 3, top_pos: top_pos, menu_pos: menu_pos})
    }
}

$(window).on("load resize scroll",function(e){
    top_menu()
});