# 第三节 树状词云

## 1. 二叉树到文字树

<svg id="mySvg" width=100% height=500 ></svg>

## 2. 文字旋转比较

<br/>
<svg id="mySvg" width=100% height=600 >
  <line x1=0 y1=200 x2=400 y2=200 stroke=blue />
  <line x1=200 y1=0 x2=200 y2=400 stroke=blue />
  <text x=200 y=200 font-size=40 fill=blue>春江花月夜</text>
<text x=200 y=200 rotate=90 font-size=40 fill=green>春江花月夜</text>
  <text x=200 y=200 transform='rotate(90,200,200)' font-size=40 fill=red>春江花月夜</text>
<text x=200 y=200 transform='rotate(45,200,200)' font-size=40 fill=orange>春江花月夜</text>
  <text x=200 y=200 transform='rotate(45,0,0)' font-size=40 fill=purple>春江花月夜</text>  
</svg>

## 3. 文字树

<svg id="mySvg2" width="100%" height=600></svg>

## 4. 苹果树

<svg id="mySvg3" width="100%" height=600 ></svg>

<script>
export default {
  mounted () {
    // 1.
    var w = 600;
    var h = 600;
    var mysvg = document.getElementById("mySvg");
    var length=150;
    var rate=0.7;
    var x0=w/2;
    var y0=h;
    var count=7;
    var str="2018新年快乐";
    function show(x0,y0,length,rate,a,count){
      var x1=x0;
      var y1=y0;
      var x2=x1+length*Math.cos(a);
      var y2=y1+length*Math.sin(a);
      var myText=document.createElement("text");
      mysvg.appendChild(myText);
      myText.outerHTML="<text x="+(x1)+" y="+y1+" style='fill:green;font-size:"+(count*2)+"'>"+str+"</text>";
      var aL=a-Math.PI/4*(0.5+0.5*Math.random());
      var aR=a+Math.PI/4*(0.5+0.5*Math.random());
      if(count>0){
          show(x2,y2,length*rate,rate,aL,count-1);
          show(x2,y2,length*rate,rate,aR,count-1);
      }
    }
    show(x0,y0,length,rate,-Math.PI/2,count);
    // 3.
    var treeSvg=document.getElementById("mySvg2");

    var length=200;
    var rate=0.75;
    var count=7;
    var a=Math.PI/4;
    var x0=w/2;
    var y0=h;

    function show2(x0,y0,length,rate,a,count){
      length=length*rate;
      var x1=x0;
      var y1=y0;
      var x2=x1+length*Math.cos(a);
      var y2=y1+length*Math.sin(a);
      var myText=document.createElement("text");
      treeSvg.appendChild(myText);
      myText.outerHTML="<text x="+(x1)+" y="+y1+" textLength="+(length)+" style='fill:rgb(131,175,155);font-family:微软雅黑;font-size:"+(count*3)+"' transform='rotate("+(a*180/Math.PI)+","+x1+","+y1+")' >春风十里不如你</text>";
      var aL=a-Math.PI/(Math.random()*20+3);
      var aR=a+Math.PI/(Math.random()*20+3);
      if(count>0){
        show2(x2,y2,length,rate,aL,count-1);
        show2(x2,y2,length,rate,aR,count-1);
      }
    }
    show2(x0,y0,length,rate,-Math.PI/3,count);
    show2(x0,y0,length,rate,-Math.PI/2,count);
    show2(x0,y0,length,rate,-Math.PI/2,count);
    // 4.
    var mysvg3 = document.getElementById("mySvg3");
    mysvg3.setAttribute("width",w*0.96);
    mysvg3.setAttribute("height",h*0.99);

    var rate=0.7;
    var x0=w/2;
    var y0=h;
    var count=7;
          var str="依依袅袅复青青";
    var fontsize=40;
    var length=str.length*fontsize;
    var iter=0
    function show3(x0,y0,length,rate,a,count){
        iter++;
      var x1=x0;
      var y1=y0;
      fontsize=count*3;
      length=str.length*fontsize;
      var x2=x1+length*Math.cos(a);
      var y2=y1+length*Math.sin(a);
      var myText=document.createElement("text");
      mysvg3.appendChild(myText);
      //myText.outerHTML="<text x="+(x1)+" y="+y1+" style='fill:green;font-size:"+(count*2)+"' rotate=90 >"+str+"</text>";
      //myText.outerHTML="<text x="+(x1)+" y="+y1+" style='fill:green;font-size:"+(count*2)+"' transform='rotate(90,"+x1+","+y1+")' >"+str+"</text>";
      myText.outerHTML="<text id="+iter+" x="+(x1)+" y="+y1+
                " style='fill:rgb(0,"+Math.floor(255*Math.random())+",0);font-size:"+(fontsize)+
                "' transform='rotate("+(a*180/Math.PI)+","+x1+","+y1+")' >"+str+"</text>";
      var aL=a-Math.PI/4*(0.5+0.5*Math.random());
      var aR=a+Math.PI/4*(0.5+0.5*Math.random());
      if (count<=1){
        var myCircle=document.createElement("circle");
        mysvg3.appendChild(myCircle);
        myCircle.outerHTML="<circle cx="+x1+" cy="+y1+" r="+(6*Math.random())+" fill='red'/>"
      }
      if(count>0){
        show3(x2,y2,length*rate,rate,aL,count-1);
        show3(x2,y2,length*rate,rate,aR,count-1);
      }
    }
    show3(x0,y0,length,rate,-Math.PI/2,count);
    show3(x0,y0,length,rate,-Math.PI*7/16,count);
    show3(x0,y0,length,rate,-Math.PI*9/16,count);
  }
}
</script>