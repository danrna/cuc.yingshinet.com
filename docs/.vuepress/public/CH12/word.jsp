<body>
<%@ page contentType="text/html; charset=gb2312" %> 
<%@ page language="java" %> 
<%@ page import="com.mysql.jdbc.Driver" %> 
<%@ page import="java.sql.*" %> 
<% 

						String word=request.getParameter("w").toLowerCase();
						//驱动程序名 
						String driverName="com.mysql.jdbc.Driver"; 
						//数据库用户名 
						String userName="root"; 
						//密码 
						String userPasswd="123456"; 
						//数据库名 
						String dbName="engword"; 
						//表名 
						//String tableName="dictionary"; 
						String tableName="map_enword";
						//联结字符串 
						String url="jdbc:mysql://localhost/"+dbName+"?user="+userName+"&password="+userPasswd; 
						Class.forName("com.mysql.jdbc.Driver").newInstance(); 
						Connection connection=DriverManager.getConnection(url); 
						Statement statement = connection.createStatement(); 
						String sql="SELECT * FROM "+tableName+" where english like '"+word+"%' order by english"; 
						ResultSet rs = statement.executeQuery(sql); 
						//获得数据结果集合 
						ResultSetMetaData rmeta = rs.getMetaData(); 
						//确定数据集的列数，亦字段数 
						int numColumns=rmeta.getColumnCount(); 
						// 输出每一个数据值 
						out.print("<center><font color=blue>Matrix Word Cloud English Learning</center>"); 
						//out.print("|"); 
						//out.print("num"); 
						//out.print("<br>"); 
						String str1="";
						String str2="";
						int count[]=new int[300];
						int j=0;
						out.print("<br><font color=blue size=5>"); 
						while(rs.next()&&(j<211)) { 
						str2=str1;
						//str1=(rs.getString(2)).substring(0,1);
						str1=rs.getString(2);
						
						
								if((!str2.equals(str1))&&(!str2.equals(str1.toLowerCase()))&&(!str2.equals(str1.toUpperCase())))
								{	
								  if(j>0)
								  	//out.print(" "+j+" "+count[j]+"<br><font color=blue>"); 
								  	out.print("<br><font color=blue size=5>"); 
									j++;
								}
								count[j]++;
						  	out.print(str1+" "); 
						  	//out.print(UTF2GBK.utf82gbk(rs.getString(3))); 
						  	out.print("      "); 
								out.print(rs.getString(4)); 
								out.print("      "); 
						}
						out.print(" "+j+" "+count[j]+"<br><font color=blue>");  
						out.print("<br>"); 
						//out.print("ok"); 
						rs.close(); 
						statement.close(); 
						connection.close(); 
%>
</body>