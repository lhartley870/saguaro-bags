/*
    Core logic/payment flow for this comes from https://stripe.com/docs/payments/quickstart
    and the Code Institute Boutique Ado project.

    CSS adapted from the Stripe styled element example: 
    https://stripe.com/docs/js/appendix/style
*/

const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
const clientSecret = $('#id_client_secret').text().slice(1, -1);
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();
const style = {
    base: {
        iconColor: '#6C6EC4',
        color: '#6C6EC4',
        fontWeight: '500',
        fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
        fontSize: '16px',
        fontSmoothing: 'antialiased',
        '::placeholder': {
            color: '#00855D',
        },
        ':focus': {
            color: '#6C6EC4',
        },
        invalid: {
            iconColor: '#dc3545',
            color: '#dc3545',
        },
    },
};

const card = elements.create('card', {style: style});
card.mount('#card-element');

/* 
Runs the changeCardFontSize function on page load
and every time the window is resized.
*/
changeCardFontSize();
window.addEventListener('resize', changeCardFontSize)

/**
 * Checks the window's inner width and changes the
 * card element's font size accordingly.
 */
function changeCardFontSize() {
    /* 
    Code for dynamically changing the styles of an element
    adapted from the Stripe documentation - 
    https://stripe.com/docs/js/element/other_methods/update?type=card
    */
    if (window.innerWidth >= 1400 && window.innerWidth < 2500) {
        card.update({style: {base: {fontSize: '19.2px'}}});
    } else if (window.innerWidth >= 2500) {
        card.update({style: {base: {fontSize: '24px'}}});
    } else {
        card.update({style: {base: {fontSize: '16px'}}});
    }
};

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    let errorDiv = document.getElementById('card-errors');
    if (event.error) {
        let html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});
