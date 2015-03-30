'use strict'

window.onload = function(){
  var scars_canvas = document.getElementById("scars");
  console.log(scars_canvas);
  var scars_context = scars_canvas.getContext("2d");
  scars_context.fillRect(50, 25, 10, 10);

  $.get('/5', {}, function(data){
    console.log('data', data);
  })

};


