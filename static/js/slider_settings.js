
    jQuery(document).ready(function() {
        var owl = jQuery('.owl-carousel');
        owl.owlCarousel({
            items:1,
            loop: true,
            autoplay:true,
            autoplayTimeout:(verb_lite_slider_variables.timeout),
            animateOut: 'fadeOut',
            animateIn: 'fadeIn',
            nav: true,
            dots: true,
            autoplayHoverPause:true,
            margin:0,
            autoHeight:true
        });

        jQuery('.play').on('click',function(){
            owl.trigger('autoplay.play.owl',[1000])
        });
        jQuery('.stop').on('click',function(){
            owl.trigger('autoplay.stop.owl')
        });
    });
