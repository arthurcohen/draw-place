function setup(){
    createCanvas(windowWidth,windowHeight);
    strokeWeight(5);
    stroke(127);
}

var lastPointX = null;
var lastPointY = null;
var currentWeight = 3;

function draw(){

    if (mouseIsPressed){
        if (lastPointX && lastPointY){
            strokeWeight(this.currentWeight);
            line(this.lastPointX, this.lastPointY, mouseX, mouseY);
        }
        /*
        stroke(0);
        strokeWeight(5);
        point(mouseX, mouseY);
        */
        this.lastPointX = mouseX;
        this.lastPointY = mouseY;
    }
    //ellipse(mouseX,mouseY,80,80);
}

function mouseReleased() {
    this.lastPointX = null;
    this.lastPointY = null;
    $("#image").val(canvas.toDataURL('image/png').replace(/data:image\/png;base64,/, ''));
}

function changeColorStroke(red, green, blue){
    stroke(red, green, blue);
}

function saveToServer(){
    var request;
    request = $.ajax({
        url: "/canvas/save/",
        method: "POST",
        data:
        {
            image: canvas.toDataURL('image/png')
        },
        datatype: "json"
    });

    request.done(function(msg) {
        alert('done')
    });

    request.fail(function(jqXHR, textStatus) {
        alert(textStatus)
    });
}

$(document).ready(function(){
    if($('#urlimage')){
        let cvs = canvas.getContext('2d');
        let img = new Image();
        img.onload = function(){
            cvs.drawImage(img,0,0); // Or at whatever offset you like
        };
        img.src = 'data:image/png;base64,'+$('#urlimage').val();
        
    }

    $.ajaxSetup({
        headers:
        { 'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content') }
    });
});
