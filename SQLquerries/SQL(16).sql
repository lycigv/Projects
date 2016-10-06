

SELECT LB.BranchId,LB.BranchName, BL.BookId, BL.DueDate
FROM Book_Loans AS BL INNER JOIN Library_Branch AS LB
ON BL.BranchId=LB.BranchId 
SELECT COUNT(*) FROM Book_Loans