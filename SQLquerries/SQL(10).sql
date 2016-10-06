CREATE PROC GetBookDetails @BranchName nvarchar(50), @Title nvarchar(50)
AS

SELECT B.BookId, B.Title, BA.AuthorName, BC.BranchId, BC.No_of_Copies, LB.BranchName
FROM Book1 AS B INNER JOIN Book_Copies AS BC
ON B.BookId=BC.BookId
INNER JOIN Library_Branch AS LB
ON LB.BranchId=BC.BranchId
INNER JOIN Book_Authors AS BA
ON B.BookId=BA.BookId

WHERE BranchName=@BranchName AND Title=@Title
GO

EXEC GetBookDetails @BranchName= 'Sharptown Central', @Title= ' Do Androids Dream of Electric Sheep?'
EXEC GetBookDetails @BranchName= '	Downtown', @Title= ' EatsShootsLeaves'
EXEC GetBookDetails @BranchName= '	South East', @Title= ' The Earth My Butt and Other Big Round Things'