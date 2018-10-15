$(document).ready(function() {
    $(".sidenav").sidenav();
    $(".parallax").parallax();

    $(window).scroll(function() {
        if ($(window).scrollTop() > 10) {
            $("nav").css("backgroundColor", "white");
            $(".change-color").css("color", "black");
        } else {
            $("nav").css("backgroundColor", "transparent");
            $(".change-color").css("color", "white");
        }
    });
});
