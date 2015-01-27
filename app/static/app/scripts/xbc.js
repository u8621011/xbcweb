/*
$(document).ready(function () {
    $(".no_img_alterable").error(function () {
        $(this).attr('src', 'static/app/img/no_image_yet.jpg');
    });
});
*/

$(function () {
    $(".no_img_alterable").error(function () {
        $(this).attr('src', 'static/app/img/no_image_yet.jpg');
    });
});

function get_product_count_in_row() {
    wndWidth = $(window).width();
    console.log("Width of windows is " + wndWidth);

    portfolioWidth = $(".portfolio-item").width();
    console.log("Width of portfolio-item is " + portfolioWidth);

    item_count_in_one_row = Math.floor(wndWidth / portfolioWidth);
    console.log("Portfolio Item Count in one row is " + item_count_in_one_row);

    return item_count_in_one_row;
}

function get_item_count_in_one_page() {
    items_on_row = get_product_count_in_row()
    items_on_page = Math.floor(12 / items_on_row) * items_on_row
    console.log(items_on_page + " items in one page");

    return items_on_page;
}

function get_total_pages(ipp, total) {
    return Math.ceil(ipp / total);
}

function on_cancel_search_click(c) {
    window.location.href = 'products?c=' + c;
}

function on_product_search_click(c) {
    var search_box = $("#product_search_box")
    var product_search = search_box.val();

    window.location.href = 'products?c=' + c + "&s=" + product_search;
}

function on_product_search_pressed(e, c) {
    if (e.keyCode == 13) {
        on_product_search_click (c)
    }
}

function on_page_num_pressed (e, c, s, ipp, t, pt) {
    if (e.keyCode == 13) {
        var page_number = $("#page_number")
        var new_p = page_number.val ();
        console.log("page_number enter key press, val = " + new_p);

        if (isNaN (new_p)) {
            // not a Number
            alert ("Page Number is not a number");
        } else {
            // is a number, jump to page if valid
            window.location.href = 'products?c=' + c + "&s=" + s + "&ipp=" + ipp + "&t=" + t + "&pt=" + pt + "&p=" + new_p;
        }
    }
}