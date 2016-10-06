SELECT Bo.Title, B.Name, B.Address, LB.BranchName, BL.DueDate
FROM Book_Loans AS BL INNER JOIN Borrower AS B
ON B.CardNo=BL.CardNo
INNER JOIN Book1 AS Bo
ON BL.BookId=Bo.BookID
INNER JOIN Library_Branch AS LB
ON BL.BranchId=LB.BranchId   
WHERE BranchName='Sharptown Central' AND DueDate=' 01-25-2016'