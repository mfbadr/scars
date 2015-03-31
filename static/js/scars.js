'use strict'

$(function(){
  var id = window.location.pathname.replace("/", "");
  var scars_canvas = document.getElementById("scars");
  scars_canvas.style.width = window.innerWidth + 'px';
  scars_canvas.style.border = "2px solid black";
  scars_canvas.style.height = window.innerHeight + 'px';

  var scars_context = scars_canvas.getContext("2d");

  function getScars(id, cb){
    var scars = [];
    $.get('/' , {"id":id}, function(data){
      //console.log('data', data);
      for(var visit in data){
        var visit = data[visit];
        scars.push(visit);
      }
      cb(scars);
    })
  }


  function drawScars(visits){
    for(var i = 0; i < visits.length; i++){
      scars_context.fillRect( 15 , 25 * visits[i].id , 10, 10);
    }
  }

  getScars(id, drawScars);
})


