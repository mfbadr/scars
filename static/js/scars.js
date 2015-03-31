'use strict'



window.onload = function(){
  var id = window.location.pathname.replace("/", "");
  console.log('id', id);
  var scars_canvas = document.getElementById("scars");
  console.log(scars_canvas);
  var scars_context = scars_canvas.getContext("2d");
  scars_context.fillRect(50, 25, 10, 10);

  $.get('/' , {"id":id}, function(data){
    console.log('data', data);
    for(var visit in data){
      var visit = data[visit];

      scars_context.fillRect(50 * visit.id, 25 * visit.id, 10, 10);
    }
  })

};


