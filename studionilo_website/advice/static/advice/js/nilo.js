var PAYMENT_ID = ''
const VIDEO_REPORT = 'CST78TAN6SFEE'
const VIDEO_COLLOQUIO = 'TSQ3J3SQZU458'
const MEDIA_MANAGER = VIDEO_COLLOQUIO

function custom_console(msg) {
    $('#console').text(msg)
}

function onUpdate() {
    $('.nilo-popup-body').each(place_bottom);
    window.requestAnimationFrame(onUpdate); // update on each frame
}

function checkout_paypal(item) {
    if (PAYMENT_ID.length > 0) {
        $('#nilo-paypal-submit').closest('form').find('input[name="custom"]').val(PAYMENT_ID)
        if (item == 'videocall')
            $('#nilo-paypal-submit').closest('form').find('input[name="hosted_button_id"]').val(VIDEO_COLLOQUIO)
        $('#nilo-paypal-submit').click()
    }
}

function close_popup() {
    $('#nilo-popup-container').css('display', 'none')
    $('body').css('overflow', 'auto')
    // document.documentElement.classList.remove('no-scroll');
    // disableBodyScroll(false, '.nilo-popup');
}

function open_popup() {
    $('#nilo-popup-container').css('display', 'flex')
    $('body').css('overflow', 'hidden')
    // document.documentElement.classList.add('no-scroll');
    // disableBodyScroll(true, '.nilo-popup');
}

// function stopBodyScrolling(bool) {
//     if (bool === true) {
//         document.body.addEventListener("touchmove", freezeVp, false);
//     } else {
//         document.body.removeEventListener("touchmove", freezeVp, false);
//     }
// }

// var freezeVp = function (e) {
//     e.preventDefault();
// };

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


// onUpdate()
$(document).ready(function () {
    for (let i = 1; i <= 2; i++) {
        let maxHeight = 0;

        $(`.nilo-same-h-0${i}`).each(function () {
            if ($(this).height() > maxHeight) { maxHeight = $(this).height(); }
        });

        $(`.nilo-same-h-0${i}`).height(maxHeight);
    }
})

$(document).ready(function () {
    $('.nilo-projects').slick({
        centerMode: true,
        centerPadding: '25%',
        slidesToShow: 1,
        focusOnSelect: true,
        responsive: [
            {
                breakpoint: 1960,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: '15%',
                    slidesToShow: 1
                }
            },
            {
                breakpoint: 1680,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: '15%',
                    slidesToShow: 1
                }
            },
            {
                breakpoint: 1440,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: '15%',
                    slidesToShow: 1
                }
            },
            {
                breakpoint: 768,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: '25%',
                    slidesToShow: 1
                }
            },
            {
                breakpoint: 425,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: '15%',
                    slidesToShow: 1
                }
            },
        ]
    });

    $('.nilo-h-aspect-16-9').each(function () {
        $(this).height($(this).width() * (9 / 16))
    })

    $('.nilo-scroll-top-out').mouseout(function () {
        $(this).animate({
            scrollTop: 0
        }, 1000);
    })

    // var humanScrollDiv = null
    // var humanInterval = null
    // function humanSmallScroll() {
    //     let aniTime = 10
    //     if (humanScrollDiv != null) {
    //         let bgPos = parseFloat(humanScrollDiv.css('background-position-y'))
    //         bgPos += 20
    //         if (bgPos < 90) {
    //             humanScrollDiv.animate({
    //                 backgroundPositionY: `${bgPos}%`,
    //             }, aniTime, 'easeOutExpo')
    //         } else {
    //             humanScrollDiv.animate({
    //                 backgroundPositionY: '100%',
    //             }, aniTime, 'easeOutExpo')
    //         }
    //     }
    // }
    // function humanScroll() {
    //     if ($(this).closest('.slick-slide').hasClass('slick-current')) {
    //         console.log('in')
    //         if ($(this).hasClass('nilo-scrolling-background')) {
    //             humanScrollDiv = $(this)
    //         }
    //         humanSmallScroll()
    //         humanInterval = setInterval(humanSmallScroll, 2000)
    //     }
    // }

    // $('.nilo-scrolling-background').mouseover(humanScroll)
    // $('.nilo-scrolling-background').mouseout(function () {
    //     if ($(this).closest('.slick-slide').hasClass('slick-current')) {
    //         clearTimeout(humanInterval)
    //         let bgPos = parseFloat($(this).css('background-position-y'))
    //         let bgInterval = bgPos + 3.6
    //         let aniTime = (200 * bgInterval) / 103.6
    //         $(this).animate({
    //             backgroundPositionY: '-3.6%',
    //         }, aniTime)
    //     }
    // })
});

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

function check_forms(targetForm) {
    let name = targetForm.find('input[name="name"]').val()
    let email = targetForm.find('input[name="email"]').val();
    let website = targetForm.find('input[name="website"]').val();
    let emailRegex = new RegExp(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);
    let websiteRegex = new RegExp(/[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)/);
    let status = true
    if (name.length == '') {
        targetForm.find('.nilo-error-msg.nilo-error-name').css('display', 'contents')
        targetForm.find('input[name="name"]').addClass('error')
        status = false
    } else {
        targetForm.find('.nilo-error-msg.nilo-error-name').css('display', 'none')
        targetForm.find('input[name="name"]').removeClass('error')
    }
    if (!emailRegex.test(email)) {
        targetForm.find('.nilo-error-msg.nilo-error-email').css('display', 'contents')
        targetForm.find('input[name="email"]').addClass('error')
        status = false
    } else {
        targetForm.find('.nilo-error-msg.nilo-error-email').css('display', 'none')
        targetForm.find('input[name="email"]').removeClass('error')
    }
    if (!websiteRegex.test(website) && website.length != '') {
        targetForm.find('.nilo-error-msg.nilo-error-website').css('display', 'contents')
        targetForm.find('input[name="website"]').addClass('error')
        status = false
    } else {
        targetForm.find('.nilo-error-msg.nilo-error-website').css('display', 'none')
        targetForm.find('input[name="website"]').removeClass('error')
    }
    return status
}

function get_form_values(targetForm) {
    let obj = {
        name: targetForm.find('input[name="name"]').val(),
        email: targetForm.find('input[name="email"]').val(),
        website: targetForm.find('input[name="website"]').val(),
        sn_facebook: targetForm.find('div[name="sn_facebook"]').hasClass('active'),
        sn_instagram: targetForm.find('div[name="sn_instagram"]').hasClass('active'),
        sn_twitter: targetForm.find('div[name="sn_twitter"]').hasClass('active'),
        sn_tiktok: targetForm.find('div[name="sn_tiktok"]').hasClass('active'),
        sn_linkedin: targetForm.find('div[name="sn_linkedin"]').hasClass('active'),
        sn_snapchat: targetForm.find('div[name="sn_snapchat"]').hasClass('active'),
        sn_pinterest: targetForm.find('div[name="sn_pinterest"]').hasClass('active'),

        user_agent: navigator.userAgent,
        screen_height: Math.max(document.documentElement.clientHeight, window.innerHeight || 0),
        screen_width: Math.max(document.documentElement.clientWidth, window.innerWidth || 0),
        plan: targetForm.find('input[name="plan"]').val(),
    }
    return obj
}

function create_payment(targetForm) {
    $.post("/consulenze/api/create-payment-intent",
        get_form_values(targetForm),
        function (data, status) {
            console.log(data);
            if (data['payment_intent_id']) {
                PAYMENT_ID = data['payment_intent_id']
            }
            console.log(PAYMENT_ID)
        });
}

$(document).on('click', '.nilo-form-validation', function (e) {
    let targetForm = $(this).closest('.modal-content').find('form.nilo-form')
    if (check_forms(targetForm)) {
        create_payment(targetForm)
    } else {
        if ($(this).data('nilo-stay')) {
            console.log($(this).data('nilo-stay'))
            $($(this).data('nilo-stay')).tab('show')
            $($(this).data('nilo-stay')).removeClass('active show')
        }
    }
});

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

$(document).on('click', '.nilo-autoremove-active-show', function (e) {
    $(this).removeClass("active")
    $(this).removeClass("show")
})
$(document).on('click', '.nilo-reset-tabs', function (e) {
    let btn = $(this)
    setTimeout(function () {
        if (btn.data('target-tabs')) {
            let tabs = $(`#${btn.data('target-tabs')}`).children('.tab-pane')
            tabs.removeClass("active")
            tabs.removeClass("show")
            if (tabs.first()) {
                tabs.first().addClass("active")
                tabs.first().addClass("show")
            }
        }
    }, 500)
})
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
            $('#circuit-logos').find('img').fadeTo(200, 1)
        }
    }
    $(this).parent().children('.nilo-button-pay-method').each(function () {
        if ($(this)[0] !== activeBtn[0]) {
            if ($(this).hasClass("active")) {
                $(this).removeClass("active")
                if ($(this).hasClass("carta")) {
                    $('#circuit-logos').find('img').fadeTo(200, 0)
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

$(document).on('click', '.nilo-fake-link', function (e) {
    if ($(this).data('href')) {
        window.location.href = $(this).data('href');
    }
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
    if ($(window).width() < 1200 && $(window).scrollTop() > 0) {
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
    $('#nilo-popup-container').css('height', `${window.innerHeight}px`)
    $('#nilo-popup-clickable').css('height', `${window.innerHeight * 0.85}px`)
    $('.nilo-test-height').css('height', `${window.innerHeight - 10}px`)
    custom_console(`wi=${window.innerHeight}\two=${window.outerHeight}\tsh=${screen.height}\tch=${document.documentElement.clientHeight}\tvh=${$('.nilo-jumbo-container').first().height()}`)
    window.requestAnimationFrame(constant_log); // update on each frame
}
// constant_log()


