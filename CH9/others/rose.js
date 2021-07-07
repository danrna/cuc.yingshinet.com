$(document).ready(function () {
	  var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
	  var audioElement = document.getElementById('audioElement');
	  var audioSrc = audioCtx.createMediaElementSource(audioElement);
	  var analyser = audioCtx.createAnalyser();

	  //绑定分析器到音频媒体元素
	  audioSrc.connect(analyser);
	  audioSrc.connect(audioCtx.destination);

	  var frequencyData = new Uint8Array(100);

	  var height = '500';
	  var width = '1200';

	  var dataset=new Array(100);
	  for(var i=0;i<100;i++){
				dataset[i]=Math.floor(Math.random()*255);
	  }
		//转化数据为适合生成饼图的对象数组		
		var pie = d3.layout.pie()
					.value(function(d){return d});
		
		innerRadius = 50;//内半径
		
		var arc=d3.svg.arc()//内外半径
			.innerRadius(innerRadius)
			.outerRadius(function (d) {
				return d.value+ innerRadius;
			});		

		var svg=d3.select("body")
				.append("svg")
				.attr("width",width)
				.attr("height",height);
		
		var arcs=svg.selectAll("g")
					.data(pie(dataset))
					.enter()
					.append("g")
					.attr("transform", "translate(" + width/2 + "," + height/2 + ")");

		arcs.append("path")
			.attr("fill",function(d,i){//填充颜色
				return 'rgb(0,0,'+dataset[i]+')';
			})
			.attr("d",arc);
				
		  // 连续循环更新
	  function renderChart() {
	     requestAnimationFrame(renderChart);
		 analyser.getByteFrequencyData(frequencyData);		 
		 arc.outerRadius(function (i) {
				return frequencyData[i]+ innerRadius;
		 });
		 
	     arcs.selectAll('path')
		     .data(pie(dataset))
		     .attr("fill",function(d,i){//填充颜色
				return 'rgb(0,0,'+dataset[i]+')';
			 })
			 .attr("d",arc);
      }
	  renderChart();
});
