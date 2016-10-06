SELECT B.BookId, B.Title, BC.BranchId, BC.No_of_Copies, LB.BranchName
FROM Book1 AS B INNER JOIN Book_Copies AS BC
ON B.BookId=BC.BookId
INNER JOIN Library_Branch AS LB
ON LB.BranchId=BC.BranchId
WHERE LB.BranchName='Sharptown Central' AND B.Title= ' EatsShootsLeaves'

