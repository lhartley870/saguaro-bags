// Wait for the DOM to finish loading before adding interactivity
$(document).ready(function() {
    // Changes the checkout logo to a shopping trolley when hovered over or focussed on
    let basketLink = $('.basket-link');
    basketLink.hover(showShoppingTrolley, showShoppingBasket);
    basketLink.focusin(showShoppingTrolley);
    basketLink.focusout(showShoppingBasket);

    /*
    Code for utilising media queries in JavaScript taken from this CSS Tricks article
    entitled 'Working with JavaScript Media Queries' by Marko Ilic dated 7 September 2020
    (and updated on 12 May 2021) -
    https://css-tricks.com/working-with-javascript-media-queries/
    */
    // Condition that targets viewports between 768 and 991px wide (medium screens)
    let mediumScreen = window.matchMedia('(min-width: 768px) and (max-width: 991px)');
    // Add an event listener to check if the medium screen condition changes
    mediumScreen.addEventListener("change", addTitleLogoMediumScreens);
    /* 
    Initial check to check whether the mediumScreen condition is true and so 
    whether the addTitleLogoMediumScreens function if statement should be run
    to add the 'Saguaro Bags' navbar title logo.
    */
    addTitleLogoMediumScreens(mediumScreen);
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

/**
 * The function called when the DOM first loads to check whether the viewport is between
 * 768px and 991px wide (medium screen). If so, the if condition is run which adds the 
 * 'Saguaro Bags' title logo to the navbar. If not, the evaluateTitleLogoRemoval function is run.
 * This function is also called if the viewport changes from being a medium screen size to not 
 * being a medium screen size and vice versa. 
 */
function addTitleLogoMediumScreens(e) {
    if (e.matches) {
        $('.navbar-toggler').after(`
        <li class="list-inline-item">
            <a href="{% url 'home' %}" class="nav-link">
                <h2 class="title-logo-link pt-1">Saguaro Bags</h2>
            </a>
        </li>`);
    } else {
        evaluateTitleLogoRemoval();
    }
}

/**
 * The function called by the addTitleLogoMediumScreens function if the current viewport
 * is not between 768px and 991px wide. This function checks whether there are two elements
 * with a class of 'title-logo-link'. 
 * If there are, this means that the title logo in the top header (which is always there but only 
 * displays on large screens) and the navbar title logo added by the addTitleLogoMediumScreens function
 * are both present in the DOM. As the screen viewport is no longer a medium screen, the navbar title 
 * logo should be removed and the removeTitleLogo function is called. 
 * If only one element is present with the class of 'title-logo-link' this means that only the top header
 * title logo is present and the navbar title logo has not been added by the addTitleLogoMediumScreens function
 * so there is no navbar title to be removed. 
 */
function evaluateTitleLogoRemoval() {
    if ($('.title-logo-link').length === 2) {
        removeTitleLogo();
    };
}

/**
 * The function called by the evaluateTitleLogoRemoval function if the current viewport is not
 * between 768px and 991px wide and the navbar title logo has been added by the addTitleLogoMediumScreens
 * function and so needs to be removed.
 */
function removeTitleLogo() {
    $('.navbar-toggler').next().remove();
}
