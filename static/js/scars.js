'use strict'

$(function(){
  var id = window.location.pathname.replace("/", "");

  var scars_canvas = document.getElementById('scars');
  var scars_context = scars_canvas.getContext("2d");

  var scarsFabric = new fabric.Canvas('scars', {
    backgroundColor: '#000000'
  });

  //scars_canvas.style.border = "2px solid black";
  var width = window.innerWidth - 10;
  var height = window.innerHeight;

  scarsFabric.setHeight(height);
  scarsFabric.setWidth(width);

  //scars_canvas.style.border = '2px solid white';

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
        columns = 25,
        colWidth = width / columns + 1;

    //construct scars and push to fabricScars;
    for(var i = 0; i < visits.length; i++){
      //console.log(visits[i].device);
      var fill;

      if(visits[i].is_mobile){
        fill = 'blue';
      }else if(visits[i].is_pc){
        fill = 'red';
      }else if(visits[i].is_bot){
        fill = 'green';
      }else{
        fill = 'white';
      }

      var thisScar = new fabric.Rect({
        left: colWidth * (((visits[i].id - 1) % columns ) + 1),
        //top: Math.ceil(visits[i].id / 10) * 25,
        top: height,
        fill: fill,
        width: 10,
        angle: 45,
        height: 10,
      })
      fabricScars.push(thisScar);
    }

    //draw scars
    var index = 0;
    function nextScar(){
      scarsFabric.add(fabricScars[index]);
      fabricScars[index].animate('top',Math.ceil(visits[index].id / columns) * 25, { 
        duration: 2400,
        easing: fabric.util.ease.easeOutCirc,
        onChange: scarsFabric.renderAll.bind(scarsFabric)
      })
      index = (index + 1) % fabricScars.length;
    }
    setInterval(nextScar, 20);
  }

  getScars(id, drawScars);
})


