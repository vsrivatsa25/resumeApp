$(document).ready(function(){
    $("html, body").animate({ scrollTop: 0 }, "slow");
    $('.loadingbar').delay(500).animate({left: '0'}, 2000);
    $('.loadingBox').delay(0).animate({opacity: '1'}, 500);
    $('.splashScreen').delay(2500).animate({top: '-100%'}, 1500);
    $('.splashBehind').delay(4000).animate({opacity: '1'}, 1000);
	$('body').addClass("visibleSplash");
});

quoteLoader = function(img){
    $('.splashLogo').src(img)
}