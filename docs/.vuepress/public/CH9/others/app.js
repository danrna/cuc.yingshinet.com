$(document).ready(function () {
	  var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
	  var audioElement = document.getElementById('audioElement');
	  var audioSrc = audioCtx.createMediaElementSource(audioElement);
	  var analyser = audioCtx.createAnalyser();

	  //绑定分析器到音频媒体元素
	  audioSrc.connect(analyser);
	  audioSrc.connect(audioCtx.destination);

	  var frequencyData = new Uint8Array(100);

	  var svgHeight = '500';
	  var svgWidth = '1200';
	  var barPadding = '1';

	  function createSvg(parent, height, width) {
		  return d3.select(parent).append('svg').attr('height', height).attr('width', width);
	  }
	  var svg = createSvg('body', svgHeight, svgWidth);

	  //创建图形
	  svg.selectAll('rect')
		 .data(frequencyData)
		 .enter()
		 .append('rect')
		 .attr('x', function (d, i) {
			return i * (svgWidth / frequencyData.length);
		 })
		 .attr('width', svgWidth / frequencyData.length - barPadding);

		  // 连续循环更新
	  function renderChart() {
	     requestAnimationFrame(renderChart);
		 analyser.getByteFrequencyData(frequencyData);
	     svg.selectAll('rect')
		    .data(frequencyData)
			.attr('y', function(d) {
				   return svgHeight - d;
				})
			.attr('height', function(d) {
				   return d;
				})
			.attr('fill', function(d) {
				   return 'rgb(0, 0, ' + d + ')';
				});
      }
	  renderChart();
});
