<!-- get.jsp-->
<%@page language= "java" contentType= "text/html; charset=utf-8"
        pageEncoding = "utf-8" %>

<html> 
<body>

<%


String[] subjects = request.getParameterValues("subjects");

out.println("관심과목" + subjects +"<br/>" );



%>



</body>
</html>

<!-- post 방식 http request 헤더에 파라미터를 붙여서 데이터를 전송하는 방식 
