SELECT B.BookId, B.Title, BC.BranchId, BC.No_of_Copies
FROM Book1 AS B INNER JOIN Book_Copies AS BC
ON B.BookId=BC.BookId
WHERE Title=' The Lost Tribe'