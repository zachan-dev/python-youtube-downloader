"use strict";
$(document).ready(function(){
    console.log('him');

    $('#form').submit(function(e) {
        e.preventDefault();
        console.log($('#form-url').val());
        console.log($('#form-type').val());
    
        var url = $('#form-url').val();
        var type = $('#form-type').val();
        download(url, type);
    });
    
    $('#facebook').click(function() {
        window.open('https://www.facebook.com/zachchan.11');
    });

    $('#twitter').click(function() {
        window.open('https://twitter.com/ZachChan10');
    });

    $('#instagram').click(function() {
        window.open('https://www.instagram.com/zach_csh/');
    });

    $('#patreon').click(function() {
        window.open('https://www.patreon.com/zachchan');
    });

    $('#linkedin').click(function() {
        window.open('https://www.linkedin.com/in/zach-chan-hk/');
    });
}); 

function download(url, type) {
    var data = {
        url: url,
        type: type
    };

    $.ajax({
        type: "POST",
        url: "/api/v1/download",
        contentType: "application/json",
        data: JSON.stringify(data),
        success: downloadSuccessCallback,
        error: function(error){
            alert("Error! Please make sure the Youtube URL is correct.\n\nSometimes this can be solved by downloading again.\n\nIf you experience difficulty after retrying, please don't hesitate to contact Zach Chan.");
        }
    });
}

function downloadSuccessCallback(url) {
    window.open(url);
}