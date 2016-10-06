CREATE PROC GetPayRate1 @JobTitle nvarchar(50), @Rate float 
AS


SELECT 
HRE.BusinessEntityID, HRE.JobTitle,
HEH.Rate,
PP.FirstName,PP.LastName

FROM HumanResources.Employee AS HRE 
INNER JOIN HumanResources.EmployeePayHistory AS HEH
ON HRE.BusinessEntityID = HEH.BusinessEntityID

INNER JOIN Person.Person AS PP
ON HRE.BusinessEntityID = PP.BusinessEntityID
WHERE JobTitle= @JobTitle AND Rate= @Rate
GO