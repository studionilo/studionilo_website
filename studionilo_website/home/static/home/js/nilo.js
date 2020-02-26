var PAYMENT_ID = ''
const VIDEO_REPORT = 'CST78TAN6SFEE'
const VIDEO_COLLOQUIO = 'TSQ3J3SQZU458'
const MEDIA_MANAGER = VIDEO_COLLOQUIO

function custom_console(msg){
    $('#console').text(msg)
}

function onUpdate() {
    $('.nilo-popup-body').each(place_bottom);
    window.requestAnimationFrame(onUpdate); // update on each frame
}

function checkout_paypal() {
    if(PAYMENT_ID.length > 0){
        $('#nilo-paypal-submit').closest('form').find('input[name="custom"]').val(PAYMENT_ID)
        if (popupTarget == 'popup_pay_1')
            $('#nilo-paypal-submit').closest('form').find('input[name="hosted_button_id"]').val(VIDEO_REPORT)
        else if (popupTarget == 'popup_pay_2')
            $('#nilo-paypal-submit').closest('form').find('input[name="hosted_button_id"]').val(VIDEO_COLLOQUIO)
        else
            $('#nilo-paypal-submit').closest('form').find('input[name="hosted_button_id"]').val(MEDIA_MANAGER)
        $('#nilo-paypal-submit').click()
    }
}

function close_popup() {
    $('#nilo-popup-container').css('display', 'none')
    $('body').css('overflow', 'auto')
}

function open_popup() {
    $('#nilo-popup-container').css('display', 'flex')
    $('body').css('overflow', 'hidden')
}

function show_popup_tab(popupTab, pTarget = 'popup_pay_1') {
    popupTarget = pTarget
    open_popup()
    tabBodySelector(popupTab)
}

function place_bottom() {
    let parent = $(this).parent()
    if (parent.css('display') == 'block') {
        let totalHeight = 0
        parent.children().each(function () {
            totalHeight += $(this).height()
            // console.log($(this), $(this).innerHeight(), $(this).height(), $(this).outerHeight())
        })
        let margin = parent.parent().innerHeight() - totalHeight
        // $(this).css('margin-top', margin)
        $(this).height($(this).height() + margin)
        // console.log(totalHeight, parent.innerHeight(), margin)
    }
}

function set_tab(target) {
    $(`#${target}`).css('display', 'block');
    $('.nilo-tab').each(function () {
        if ($(this).attr('id') !== `${target}`) {
            $(this).css('display', 'none');
        }
    });
}

function in_hover_btn_img() {
    $(this).children('img').attr('data-orig-img', $(this).children('img').attr('src'))
    $(this).children('img').attr('src', $(this).children('img').data('alt-img'))

}

function out_hover_btn_img() {
    $(this).children('img').attr('src', $(this).children('img').data('orig-img'))

}


onUpdate()
$(document).ready(function () {
    $('.nilo-deck').each(function () {
        let count = 0
        $(this).children().filter(".nilo-card").each(function () {
            count++
        })
        let index = 0
        let margin_perc = 1.5
        let margins_perc_tot = ((count - 1) * 2) * margin_perc
        let card_perc_tot = 100.0 - margins_perc_tot
        let card_perc = card_perc_tot / count
        $(this).children().filter(".nilo-card").each(function () {
            $(this).css('width', `${card_perc}%`)
            if (index != 0) {
                $(this).css('margin-left', `${margin_perc}%`)
            }
            if (index != (count - 1)) {
                $(this).css('margin-right', `${margin_perc}%`)
            }
            index++
        })
    })
})
var allPopupTarget = ['popup_pay_1', 'popup_pay_2', 'popup_pay_3']
var popupTarget = allPopupTarget[0]

$(document).on('click', '.nilo-open-popup-button', function (e) {
    open_popup()
    popupTarget = $(this).data('target')
    tabBodySelector('popup_pay_tab_info')
});

function tabBodySelector(nextTab) {
    set_tab(nextTab)
    allPopupTarget.forEach(function (target) {
        $(`#${nextTab} .${target}`).css('display', 'none')
    });
    $(`#${nextTab} .${popupTarget}`).css('display', 'inline')
}

function check_forms() {
    let name = $('#nilo-form-api').find('input[name="name"]').val()
    let email = $('#nilo-form-api').find('input[name="email"]').val();
    let website = $('#nilo-form-api').find('input[name="website"]').val();
    let emailRegex = new RegExp(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);
    let websiteRegex = new RegExp(/[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)/);
    let status = true
    if (name.length == '') {
        $('#nilo-error-name').css('display', 'contents')
        $('#nilo-form-api').find('input[name="name"]').addClass('error')
        status = false
    } else {
        $('#nilo-error-name').css('display', 'none')
        $('#nilo-form-api').find('input[name="name"]').removeClass('error')
    }
    if (!emailRegex.test(email)) {
        $('#nilo-error-email').css('display', 'contents')
        $('#nilo-form-api').find('input[name="email"]').addClass('error')
        status = false
    } else {
        $('#nilo-error-email').css('display', 'none')
        $('#nilo-form-api').find('input[name="email"]').removeClass('error')
    }
    if (!websiteRegex.test(website) && website.length != '') {
        $('#nilo-error-website').css('display', 'contents')
        $('#nilo-form-api').find('input[name="website"]').addClass('error')
        status = false
    } else {
        $('#nilo-error-website').css('display', 'none')
        $('#nilo-form-api').find('input[name="website"]').removeClass('error')
    }
    return status
}

function get_from_values() {
    let obj = {
        name: $('#nilo-form-api').find('input[name="name"]').val(),
        email: $('#nilo-form-api').find('input[name="email"]').val(),
        website: $('#nilo-form-api').find('input[name="website"]').val(),
        sn_facebook: $('#nilo-form-api').find('div[name="sn_facebook"]').hasClass('active'),
        sn_instagram: $('#nilo-form-api').find('div[name="sn_instagram"]').hasClass('active'),
        sn_twitter: $('#nilo-form-api').find('div[name="sn_twitter"]').hasClass('active'),
        sn_tiktok: $('#nilo-form-api').find('div[name="sn_tiktok"]').hasClass('active'),
        sn_linkedin: $('#nilo-form-api').find('div[name="sn_linkedin"]').hasClass('active'),
        sn_snapchat: $('#nilo-form-api').find('div[name="sn_snapchat"]').hasClass('active'),
        sn_pinterest: $('#nilo-form-api').find('div[name="sn_pinterest"]').hasClass('active'),

        user_agent: navigator.userAgent,
        screen_height: Math.max(document.documentElement.clientHeight, window.innerHeight || 0),
        screen_width: Math.max(document.documentElement.clientWidth, window.innerWidth || 0),
        plan: popupTarget,
    }
    return obj
}

function create_payment() {
    $.post("api/create-payment-intent",
        get_from_values(),
        function (data, status) {
            console.log(data);
            if(data['payment_intent_id']){
                PAYMENT_ID = data['payment_intent_id']
            }
            console.log(PAYMENT_ID)
        });
}

$(document).on('click', '.nilo-popup-footer-button', function (e) {
    if ($(this).data('target')) {
        if ($(this).data('pay') && $(this).data('pay') == 'nilo-create-payment-btn') {
            if (check_forms()) {
                create_payment()
                tabBodySelector($(this).data('target'))
            }
        } else {
            tabBodySelector($(this).data('target'))
        }
    }
});


$(document).on('click', '.nilo-pill', function (e) {
    if (!$(this).hasClass('active')) {
        $(this).addClass("active")
    } else {
        $(this).removeClass("active")
    }
})
$(document).on('click', '.nilo-button-pay-method', function (e) {
    let activeBtn = $(this)
    if (!$(this).hasClass("active")) {
        $(this).addClass("active")
        if ($(this).hasClass("carta")) {
            $(this).closest('.nilo-popup-body').find('img').fadeTo(200, 1)
        }
    }
    if ($(this).data('show-txt')) {
        let sections = ['paypal-section', 'card-section']
        sections.forEach(function (section) {
            activeBtn.closest('.nilo-tab').find(`.${section}`).css('display', 'none')
        })
        $(this).closest('.nilo-tab').find(`.${$(this).data('show-txt')}`).css('display', 'block')
    }
    $(this).parent().children('.nilo-button-pay-method').each(function () {
        if ($(this)[0] !== activeBtn[0]) {
            if ($(this).hasClass("active")) {
                $(this).removeClass("active")
                if ($(this).hasClass("carta")) {
                    $(this).closest('.nilo-popup-body').find('img').fadeTo(200, 0)
                }
            }
        }
    })
});

$(document).on('click', '.nilo-read-more-button', function (e) {
    var moreText = $(this).closest('table>tbody').find('span.nilo-more')
    let readButton = $(this).closest('table>tbody').find('.nilo-read-more-button')

    if (moreText.is(':visible')) {
        moreText.slideUp()
        readButton.text(readButton.data('orig-txt'))
    } else {
        moreText.slideDown()
        readButton.text(readButton.data('alt-txt'))
    }
});

$(document).on('click', '#nilo-tailored', function (e) {
    show_popup_tab('popup_pay_tab_tailored')
});
$(document).on('click', '#nilo-contactus', function (e) {
    show_popup_tab('popup_pay_tab_contactus')
});

$(document).mousedown(function (e) {
    var container = $('#nilo-popup-clickable');
    // if the target of the click isn't the container nor a descendant of the container
    if (!container.is(e.target) && container.has(e.target).length === 0) {
        close_popup()
    } else {
    }
});

$(document).on('click', '.nilo-table-collapse-btn', function (e) {
    var targetRow = null
    if ($(this).data('target')) {
        targetRow = $(this).closest('table>tbody')
            .children(`tr#${$(this).data('target')}`)
    } else {
        targetRow = $(this).closest('table>tbody')
            .children('tr.nilo-table-gains')
    }
    var wrappers = targetRow.children('td')
        .children('div.wrapper')
    var arrows = $(this).closest('tr').find('img')
    if (wrappers.is(':visible')) {
        arrows.addClass('deactivated').removeClass('activated')
        wrappers.slideUp()
    } else {
        arrows.addClass('activated').removeClass('deactivated')
        wrappers.slideDown()
    }
});

var prevScrollpos = window.pageYOffset;
window.onscroll = function () {
    if($(window).width() < 1200 && $(window).scrollTop() > 0){
        let currentScrollPos = window.pageYOffset;
        let navHeight = $('.nilo-nav').outerHeight()
        let shift = currentScrollPos - prevScrollpos
        let prevShift = parseInt($('.nilo-nav').css('top'), 10)
        let totalShift = prevShift - shift
        if (-totalShift > navHeight) {
            totalShift = -navHeight
        } else if (totalShift > 0) {
            totalShift = 0
        }
        // console.log(`shift=${shift}\tprevShift=${prevShift}\ttotal=${totalShift}\tnavHeight=${navHeight}`)
        // custom_console(`wp=${$(window).scrollTop()}\tsh=${shift}\tprevSh=${prevShift}\tt=${totalShift}\tnH=${navHeight}`)
        $('.nilo-nav').css('top', `${totalShift}px`)
        prevScrollpos = currentScrollPos;
    } else {
        $('.nilo-nav').css('top', '0px')
    }
}


function constant_log() {
    let = height = window.innerHeight || $(window).height();
    $('.nilo-test-height').css('height', `${height}px`)
    custom_console(`h=${height}`)
    window.requestAnimationFrame(constant_log); // update on each frame
}
constant_log()
