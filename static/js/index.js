"use strict";
$(document).ready(function(){
    console.log('him');
}); 

$('#form').submit(function(e) {
    e.preventDefault();
    console.log($('#form-url').val());
    console.log($('#form-type').val());

    var url = $('#form-url').val();
    var type = $('#form-type').val();
    download(url, type);
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
            alert("Error! Please make sure the Youtube URL is correct");
        }
    });
}

function downloadSuccessCallback(url) {
    window.open(url);
}