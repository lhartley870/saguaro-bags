// Wait for the DOM to finish loading before adding interactivity
$(document).ready(function() {
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
    let icon = $('.checkout-logo');
    icon.removeClass('fa-cart-shopping');
    icon.addClass('fa-basket-shopping');
}

/**
 * The function called when the user stops hovering over or removes focus from the checkout
 * logo, changing the checkout logo from a trolley back to a shopping basket.
 */
function showShoppingTrolley() {
    let icon = $('.checkout-logo');
    icon.removeClass('fa-basket-shopping');
    icon.addClass('fa-cart-shopping');
}
