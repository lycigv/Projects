
SELECT B.Name, B.CardNo, BL.DueDate
FROM Borrower AS B INNER JOIN Book_Loans AS BL
ON B.CardNo=BL.CardNo

WHERE DueDate IS NULL