<html>
	<head>
		<title>基于D3调用数据库中数据的词云图</title>
	</head>
	<body>
	<div id="wc"></div>
	<%@ page contentType="text/html; charset=gb2312" %> 
	<%@ page language="java" %> 
	<%@ page import="com.mysql.jdbc.Driver.*" %> 
	<%@ page import="java.sql.*" %> 
	<% 		
			String driverName="com.mysql.jdbc.Driver"; //驱动程序名 			 
			String userName="root"; //数据库用户名			
			String userPasswd="123456"; //密码 		
			String dbName="engword"; //数据库名 			 
			//String tableName="dictionary"; //表名
			String tableName="map_enword";
			//联结字符串 
			String url="jdbc:mysql://localhost/"+dbName+"?user="+userName+"&password="+userPasswd; 
			Class.forName("com.mysql.jdbc.Driver").newInstance(); 
			Connection connection=DriverManager.getConnection(url); 
			Statement statement = connection.createStatement(); 
			String sql="SELECT * FROM "+tableName+" order by english"; 
			ResultSet rs = statement.executeQuery(sql); 
			//获得数据结果集合 
			ResultSetMetaData rmeta = rs.getMetaData(); 
			//确定数据集的列数，亦字段数 
			int numColumns=rmeta.getColumnCount(); 
			// 输出每一个数据值 
			out.print("<center><font color=blue>Matrix Word Cloud English Learning</center>"); 
			String str1="";
			String str2="";
			int count[]=new int[27];
			int j=0;
			while(rs.next()) { 
				str2=str1;
				str1=(rs.getString(2)).substring(0,1);			
				if((!str2.equals(str1))&&(!str2.equals(str1.toLowerCase()))&&(!str2.equals(str1.toUpperCase())))
				{	
				  if(j>0)
					out.print(" "+j+" "+count[j]+"<br><font color=blue>"); 
					j++;
				}
				count[j]++;
				out.print(str1+" "); 
			}
			out.print(" "+j+" "+count[j]+"<br><font color=blue>");  
			out.print("<br>"); 
%>
	<script src="../d3.v3.min.js"></script>
	<script src="../d3.layout.cloud.js"></script>
	<script>
	    var w=window.innerWidth|| document.documentElement.clientWidth|| document.body.clientWidth;
		var h=window.innerHeight|| document.documentElement.clientHeight|| document.body.clientHeight;
		var width = w*0.98;
		var height =h*0.3;		
		function wc_click(e){
			var evt=e||window.event;
			var evtSrc=evt.target||evt.srcElement;
			location.href="word.jsp?w="+evtSrc.textContent;
		}		
	  var fill = d3.scale.category20();
	  d3.layout.cloud().size([width, height])
		  .words([
			"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
		   .map(function(d) {
			var tmp={
				<%
				for(int i=0;i<26;i++){
					out.print("\""+(char)('A'+i)+"\" : "+count[i+1]);
					if(i!=25){
						out.print(", ");
					}
				}
				%>
			};
			return {text: d, size: Math.sqrt(tmp[d])*5.5};
		  }))
		  .padding(-3)
		  .rotate(function() { return ~~(Math.random() * 2) * 90; })
		  .font("Impact")
		  .fontSize(function(d) { return d.size; })
		  .on("end", draw)
		  .start();

	  function draw(words) {
		d3.select("#wc").append("svg")
			.attr("width", width)
			.attr("height", height)
		  .append("g")
			.attr("transform", "translate("+(width/2)+","+(height/2)+")")
		  .selectAll("text")
			.data(words)
		  .enter().append("text")
			.style("font-size", function(d) { return d.size + "px"; })
			.style("font-family", "Impact")
			.style("fill", function(d, i) { return fill(i); })
			.style("cursor", "pointer")
			.attr("text-anchor", "middle")
			.attr("class", "wc")
			.attr("transform", function(d) {
			  return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
			})
			.text(function(d) { return d.text; });
		var ele=document.getElementsByClassName("wc");
		for(var e in ele){
			ele[e].onclick=wc_click;
		}
	  }
	</script>
	<%
			rs.close(); 
			statement.close(); 
			connection.close(); 
	%>
	</body>
</html>
