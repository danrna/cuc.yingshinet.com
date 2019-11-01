# 第二节 递归二叉树

## 分形二叉树

<svg id="mySvg" width="100%" height=600 ></svg>

## 风格化分形二叉树

<svg id="wcSvg" width="100%" height=600 ></svg>

<script>
export default {
  mounted () {
    var w = 600;
    var h = 600;
    // 1.
    var mysvg = document.getElementById("mySvg");
    var length=200;
    var rate=0.6;
    var x0=300;
    var y0=600;
    var count=7;
    function show(x0,y0,length,rate,a,count){
      var x1=x0;
      var y1=y0;
      var x2=x1+length*Math.cos(a);
      var y2=y1+length*Math.sin(a);
      var svgline= document.createElement("line");
      mysvg.appendChild(svgline);
      svgline.outerHTML="<line x1="+x1+" y1="+y1+" x2="+x2+" y2="+y2+" style='stroke:rgb(99,99,99);stroke-width:2'/>";
      var aL=a-Math.PI/4;
      var aR=a+Math.PI/4;
      if(count>0){
        show(x2,y2,length*rate,rate,aL,count-1);
        show(x2,y2,length*rate,rate,aR,count-1);
      }
    }
    show(x0,y0,length,rate,-Math.PI/2,count);
    // 2.
    var mysvg2 = document.getElementById("wcSvg");
    var length=300;
    rate=0.6;
    var x0=w/2;
    var y0=h;
    var count=7;
    var iter=0;
    function show2(x0,y0,length,rate,a,count){
        var x1=x0;
        var y1=y0;
        var x2=x1+length*(0.5+0.5*Math.random())*Math.cos(a);
        var y2=y1+length*(0.5+0.5*Math.random())*Math.sin(a);
        var svgline2= document.createElement("line");
        mysvg2.appendChild(svgline2);
        iter++;
        var rand=Math.random();
        svgline2.outerHTML="<line x1="+x1+" y1="+y1+" x2="+x2+" y2="+y2+" style='stroke:rgb(0,"+(iter)+",0);stroke-width:"+(count)+"' />";
        var aL=a-Math.PI/4*(0.5+0.5*Math.random());
        var aR=a+Math.PI/4*(0.5+0.5*Math.random());
        if(count>0){
        show2(x2,y2,length*rate,rate,aL,count-1);
        show2(x2,y2,length*rate,rate,aR,count-1);
        }
    }
    show2(x0,y0,length,rate,-Math.PI/2,count);
  }
}
</script>