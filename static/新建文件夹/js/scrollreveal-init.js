jQuery(document).ready(function($) {
// Initialise Scroll Reveal
window.sr = ScrollReveal({ reset: false });
    sr.reveal('#wrapper-featured .post .hovereffect', {
        duration: 500,
        delay: 50,
        origin: 'bottom',
        distance: '0px',
        scale: 1,
        easing: 'linear',
        viewFactor: 0.25
    }, 50);
    sr.reveal('.post .hovereffect', {
        duration: 500,
        delay: 50,
        origin: 'bottom',
        distance: '0px',
        scale: 1,
        easing: 'linear',
        viewFactor: 0.25
    });
    sr.reveal('.wpp-list li', {
        duration: 500,
        delay: 50,
        origin: 'bottom',
        distance: '0px',
        scale: 1,
        easing: 'linear',
        viewFactor: 0.25
    });
});