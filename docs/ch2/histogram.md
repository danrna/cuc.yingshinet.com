# 第一节 直方图

## 1. 屏幕分辨率

<p id="demo"></p>

## 2. 随机数直方图

<svg id="mySVG" width="800" height="300" version="1.1" xmlns="http://www.w3.org/2000/svg"></svg>

<video controls width="100%">
  <source src="\MOOC\CH2\histogram.mp4"  type="video/mp4">
</video>

## 3. 随机色直方图

<svg id="mySVG2" width="800" height="400" version="1.1" xmlns="http://www.w3.org/2000/svg"></svg>

## 4. 直方图添加文本

<svg id="mySVG3" width="800" height="400" version="1.1"></svg>

<script>
export default {
  mounted () {
    // 1.
    var w=window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

    var h=window.innerHeight
    || document.documentElement.clientHeight
    || document.body.clientHeight;

    x=document.getElementById("demo");
    x.innerHTML="浏览器的内部窗口宽度：" + w + "，高度：" + h + "。"
    // 2.
    var x=100,y=300;
    var mysvg = document.getElementById("mySVG");
    var svgrec= new Array();
    for(var i=0;i<6;i++){
      svgrec[i] = document.createElement("rect");
      mysvg.appendChild(svgrec[i]);
      var h=Math.random()*300;
      svgrec[i].outerHTML="<rect x="+(i*x)+" y="+(y-h)+" width=70 height="+(h)+" style='fill:red'>";
    }
    // 3. 随机色直方图
    var mysvg = document.getElementById("mySVG2");
    var rec= new Array();
    for(var i=0;i<6;i++){
      rec[i] = document.createElement("rect");
      mysvg.appendChild(rec[i]);
      var h=Math.random()*300;
      //rec[i].outerHTML="<rect x="+(20+80*i)+" y="+(400-h)+" width=70 height="+h+" style='fill:red'/>";
      //rec[i].outerHTML="<rect x="+(60*i)+" y="+(400-h)+" width=55 height="+h+" style='fill:rgb(0,0,255)'/>";
      //rec[i].outerHTML="<rect x="+(60*i)+" y="+(400-h)+" width=55 height="+h+" style='fill:rgb(0,0,"+Math.floor(h)+")'/>";
      var r=Math.floor(Math.random()*255);
            var g=Math.floor(Math.random()*255);
            var b=Math.floor(Math.random()*255);
      rec[i].outerHTML="<rect x="+(45*i)+" y="+(400-h)+" width=42 height="+h+" style='fill:rgb("+r+","+g+","+b+")'/>";

    }
    // 4. 直方图添加文本
    var mysvg = document.getElementById("mySVG3");
    var rec= new Array();
    var txt=new Array();
    for(var i=0;i<6;i++){
      rec[i] = document.createElement("rect");
      txt[i] = document.createElement("text");
      mysvg.appendChild(rec[i]);
      mysvg.appendChild(txt[i]);
      var h=Math.random()*300;
      var r=Math.floor(Math.random()*255);
      var g=Math.floor(Math.random()*255);
      var b=Math.floor(Math.random()*255);
      rec[i].outerHTML="<rect x="+(45*i)+" y="+(400-h)+" width=42 height="+h+" style='fill:rgb("+r+","+g+","+b+")'/>";
      txt[i].outerHTML="<text x="+(10+45*i)+" y="+(400-h)+">"+Math.floor(h)+"</text>";
    }
  }
}
</script>
