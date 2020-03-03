setInterval(ajaxCall, 3000);
/*var geral = 0;*/
function ajaxCall() {
    $.ajax({
        dataType: "json",
        url: '/api/',
        data: 'json',
        success: function(data){
        	console.log(data['temp']);
        	$('#temp').text(data['temp']);
            // temperature = data.temperature.value;
        }
    });
}

// window.feed = function(callback) {
//   var tick = {};
//   tick.plot0 = temperature;
//   callback(JSON.stringify(tick));
// };
//
// var myConfig = {
//  	type: "gauge",
//  	globals: {
//  	  fontSize: 22
//  	},
//  	plotarea:{
//  	  marginTop:80
//  	},
//  	plot:{
//  	  size:'100%',
//  	  valueBox: {
//  	    placement: 'center',
//  	    text:'%v', //default
//  	    fontSize:35,
//  	    rules:[
//  	      {
//  	        rule:'%v <= -10',
//  	        text: '%v °C<br>Gongelando'
//  	      },
//  	      {
//  	        rule:'%v >= -10 && %v < 0',
//  	        text: '%v °C<br>Muito Frio'
//  	      },
//  	      {
//  	        rule:'%v >= 0 && %v < 10',
//  	        text: '%v °C<br>Frio'
//  	      },
//  	      {
//  	        rule:'%v >= 10 && %v < 20',
//  	        text: '%v °C<br>Ambiente'
//  	      },
//           {
//  	        rule:'%v >= 20 && %v < 30',
//  	        text: '%v °C<br>Calor'
//  	      },
//           {
//  	        rule:'%v >= 30 && %v < 40',
//  	        text: '%v °C<br>Quente'
//  	      },
//           {
//  	        rule:'%v >= 40 && %v <= 50',
//  	        text: '%v °C<br>Muito Quente'
//  	      },
//
//  	    ]
//  	  }
//  	},
//   tooltip:{
//     borderRadius:5
//   },
//  	scaleR:{
// 	  aperture:180,
// 	  minValue:-10,
// 	  maxValue:50,
// 	  step:5,
// 	  center:{
// 	    visible:false
// 	  },
// 	  tick:{
// 	    visible:true
// 	  },
// 	  item:{
// 	    offsetR:0,
// 	    rules:[
// 	      {
// 	        rule:'%i == 9',
// 	        offsetX:15
// 	      }
// 	    ]
// 	  },
// 	  labels:[],
// 	  ring:{
// 	    size:50,
// 	    rules:[
//
//           {
// 	        rule:'%v <= -5',
// 	        backgroundColor:'#0000FF'
// 	      },
//           {
// 	        rule:'%v >= -5 && %v < 0',
// 	        backgroundColor:'#87CEEB'
// 	      },
// 	      {
// 	        rule:'%v >= 0 && %v < 10',
// 	        backgroundColor:'#00FF7F'
// 	      },
// 	      {
// 	        rule:'%v >= 10 && %v < 20',
// 	        backgroundColor:'#7FFF00'
// 	      },
// 	      {
// 	        rule:'%v >= 20 && %v < 30',
// 	        backgroundColor:'#FFFF00'
// 	      },
//           {
// 	        rule:'%v >= 30 && %v < 40',
// 	        backgroundColor:'#FFA500'
// 	      },
//           {
// 	        rule:'%v >= 40 && %v <= 50',
// 	        backgroundColor:'#E53935'
// 	      }
// 	    ]
// 	  }
//  	},
//   refresh:{
//       type:"feed",
//       transport:"js",
//       url:"feed()",
//       interval:1000,
//       resetTimeout:1000
//   },
// 	series : [
// 		{
// 			values : [0], // starting value
// 			backgroundColor:'black',
// 	    indicator:[10,5,5,5,0.75],
// 	    animation:{
//         effect:2,
//         method:1,
//         sequence:4,
//         speed: 900
//      },
// 		}
// 	]
// };
// zingchart.render({
// 	id : 'myChart',
// 	data : myConfig,
// 	height: 500,
// 	width: '100%'
// });