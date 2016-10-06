SELECT B.BookId, B.Title, BA.AuthorName, BC.BranchId, BC.No_of_Copies, LB.BranchName
FROM Book1 AS B INNER JOIN Book_Copies AS BC
ON B.BookId=BC.BookId
INNER JOIN Library_Branch AS LB
ON LB.BranchId=BC.BranchId
INNER JOIN Book_Authors AS BA
ON B.BookId=BA.BookId
WHERE BranchName= 'Sharptown Central' AND AuthorName='Philip K Dick'