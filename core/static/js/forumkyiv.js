$(document).ready(function () {

    function clorize(element, color1, color2) {
        var c = $(element).attr("class");
        var locationSelector = ".section-location ." + c;
        //var timeSelector = ".section-time ." + c;

        $(locationSelector).css("color", color1);
        //$(timeSelector).css("color",color1);
        $(element).css("color", color2);

        //console.log(selector);
    }


    $(".section-name ul li").mouseover(function () {
        clorize(this, "#0098cf", "#0098cf");
    });

    $(".section-name ul li").mouseout(function () {
        clorize(this, "#989ca2", "#000");
    });
});