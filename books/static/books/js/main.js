/**
 * Created by olechka on 24.10.17.
 */

jQuery(document).ready(function ($) {
    //'use strict';
    /**таблица - группы пользователей**/
    $("button.like").click(function () {
        id = $(this).val()
        console.log(id)
        $.ajax({
            url: '/books/set_like/',
            data: {
                'id': id
            },
            type: 'GET',

            dataType: 'json',
            beforeSend: function () {

            },
            complete: function () {

            },
            success: function (data) {
                //alert(data)
                console.log(data)
                new_like = data
                $(".l").text(new_like)
            }
        });
    });

     $(".dislike").click(function () {
        id = $(this).val()
        console.log(id)
        $.ajax({
            url: '/books/set_dislike/',
            data: {
                'id': id
            },
            type: 'GET',

            dataType: 'json',
            beforeSend: function () {

            },
            complete: function () {

            },
            success: function (data) {
                //alert(data)
                console.log(data)
                new_dislike = data
                $(".dl").text(new_dislike)
            }
        });
    });
});