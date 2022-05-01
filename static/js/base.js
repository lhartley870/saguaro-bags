// Wait for the DOM to finish loading before adding interactivity
$(document).ready(function() {
    // Sets the checkout logo to a shopping basket 
    $('.checkout-logo').html('<i class="fa-solid fa-basket-shopping fa-lg"></i>');

    // Changes the checkout logo to a shopping trolley when hovered over or focussed on
    let basketLink = $('.basket-link');
    basketLink.hover(showShoppingTrolley, showShoppingBasket);
    basketLink.focusin(showShoppingTrolley);
    basketLink.focusout(showShoppingBasket);
});

/**
 * The function called when the user hovers over or focusses on the checkout logo,
 * changing the checkout logo from a shopping basket to a trolley.
 */
function showShoppingBasket() {
    $('.checkout-logo').html('<i class="fa-solid fa-basket-shopping fa-lg"></i>');
}

/**
 * The function called when the user stops hovering over or removes focus from the checkout
 * logo, changing the checkout logo from a trolley back to a shopping basket.
 */
function showShoppingTrolley() {
    $('.checkout-logo').html('<i class="fa-solid fa-cart-shopping fa-lg"></i>');
}
