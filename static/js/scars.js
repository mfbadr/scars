'use strict'

$(function(){
  var id = window.location.pathname.replace("/", "");

  var scars_canvas = document.getElementById('scars');
  var scars_context = scars_canvas.getContext("2d");

  var scarsFabric = new fabric.Canvas('scars', {
    backgroundColor: '#000000'
  });

  //scars_canvas.style.border = "2px solid black";
  var width = window.innerWidth;
  var height = window.innerHeight;
  console.log('width', width);
  console.log('height', height);
  scars_canvas.style.width = width + 'px';
  scars_canvas.style.height = height + 'px';
  scars_context.canvas.width = width;
  scars_context.canvas.height = height;
  scars_canvas.style.border = '2px solid white';



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
    //set up counters, analyze canvas
    var fabricScars = [],
        colWidth = width / 11;

    console.log('colwidth', colWidth);


    //construct a fabric object based on visit attr
    var row = 1;
    for(var i = 0; i < visits.length; i++){
      //swithc on tablet/pc/mobile

      var thisScar = new fabric.Rect({
        left: colWidth * ((visits[i].id % 10) + 1),
        top: Math.ceil(visits[i].id / 10) * 25,
        fill: 'red',
        width: 10,
        angle: 45,
        height: 10,
      })
      fabricScars.push(thisScar);
    }

    //draw scars
    for(var i = 0; i < fabricScars.length; i++){
      scarsFabric.add(fabricScars[i]);
    }
  }

  getScars(id, drawScars);
})


