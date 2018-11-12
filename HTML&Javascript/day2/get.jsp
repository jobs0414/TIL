<!-- get.jsp-->
<%@page language= "java" contentType= "text/html; charset=utf-8"
        pageEncoding = "utf-8" %>

<html> 
<body>

<%

String name = request.getParameter("name");
String major = request.getParameter("major");
String phone = request.getParameter("phone");
out.println("이름:"+ name + "<br/>");
out.println("전공:" + major + "<br/>");
out.println("전화번호" + phone + "<br/>");

%>



</body>
</html>

<!-- post 방식 http request 헤더에 파라미터를 붙여서 데이터를 전송하는 방식 
