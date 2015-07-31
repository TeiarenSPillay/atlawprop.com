jQuery("#rndList li").css({display: "none", top:0, left:0, position: "absolute"});
jQuery("#rndList li:first-child").fadeIn(0).addClass("active");
function myTransition(){
    if(jQuery("#rndList li.active").next("li").length){
        jQuery("#rndList li.active").filter(':not(:animated)').fadeOut(800).removeClass("active").next().filter(':not(:animated)').fadeIn(800).addClass("active");
    }else{
        jQuery("#rndList li.active").filter(':not(:animated)').fadeOut(800).removeClass("active");
        jQuery("#rndList li:first-child").fadeIn(800).addClass("active");
    }
}
function myTransition_prev(){
    if(jQuery("#rndList li.active").prev("li").length){
        jQuery("#rndList li.active").filter(':not(:animated)').fadeOut(800).removeClass("active").prev().filter(':not(:animated)').fadeIn(800).addClass("active");
    }else{
        jQuery("#rndList li.active").filter(':not(:animated)').fadeOut(800).removeClass("active");
        jQuery("#rndList li:last-child").filter(':not(:animated)').fadeIn(800).addClass("active");
    }
}
jQuery(".resizer-next").on("click", function(e){
    e.preventDefault();
    myTransition();
    if(randomSlide){
        clearInterval(randomSlide);
        randomSlide = setInterval(function(){myTransition()}, 8000);
    }
});
jQuery(".resizer-prev").on("click", function(e){
    e.preventDefault();
    myTransition_prev();
    if(randomSlide){
        clearInterval(randomSlide);
        randomSlide = setInterval(function(){myTransition()}, 8000);
    }
});
if( jQuery("#rndList > li").length < 2){
  console.info("Only 1 slide found.");
  $(".resizer .slide-next, .resizer .slide-prev").hide();
  clearInterval(randomSlide);
}else{
  var randomSlide = setInterval(function(){myTransition()}, 8000);
}
