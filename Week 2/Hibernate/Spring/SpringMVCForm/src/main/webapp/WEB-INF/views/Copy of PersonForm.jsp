<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
    
 <%@taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
<form:form modelAttribute="person" action="${pageContext.request.contextPath}/personDetails" method="POST">
<table>
	<tr>
	    <td>First Name: </td>
	    <td><form:input path="firstName"/></td>
	</tr>
	<tr>
	    <td>Last Name: </td>
	    <td><form:input path="lastName"/></td>
	</tr>
	<tr>
	    <td><input type="submit" value="Save Changes"/>
	</tr>
</table>
</form:form>

</body>
</html>