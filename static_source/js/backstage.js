/**
 * Created by michael on 2/28/16.
 */

function sizeImages() {
    img = $('.sized-image');
    width = img.width();
    img.css({'height': width + 'px'})
}

function centerImages() {
    $('.centered-image').each(function() {
        if ($(this).height() > $(this).width()) {
            $(this).addClass('taller');
        } else {
            console.log(this, ' is taller')
            $(this).addClass('fatter');
        }
    });
}

$(document).ready(function() {
    centerImages()
    sizeImages();
});

$(window).resize(function() {
    centerImages()
    sizeImages();
});
