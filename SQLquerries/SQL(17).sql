SELECT B.Name, B.Address, BL.CardNo, BL.BookId, BL.DueDate
FROM Borrower AS B INNER JOIN Book_Loans AS BL
ON B.CardNo=BL.CardNo
SELECT CardNo FROM Book_Loans
GROUP BY Book_Loans.CardNo
HAVING COUNT(Book_Loans.CardNo)>5