using System;
using System.IO;
using System.Data;
using System.Data.OleDb;
using System.Data.SqlClient;
using System.Threading;

namespace ConsoleApplication2

    /* What I did in this was to create a Console application in VS then use C# code to load data to a database in SQL Server.
     I created database manualy in SQL Server, then table with matching Columns as in Excel Sheet */
{
    class Transfer
    {
        static void Main(string[] args)
        {
            string datetime = DateTime.Now.ToString("yyyyMMddHHmmss");
            string LogFolder = @"c:\Log";
            try
            {
                string DatabaseName = "booklistSQL";               
                //string SQLServerName = "(LocalDB)\\MSSQLLocalDB";
                string SQLServerName = ".\\SQLEXPRESS";
                //string TableName = @"Book";
                string TableName = @"Book2";
                string SchemaName = @"dbo";
                //string fullFilePath = @"C:\Users\Student\Documents\GitHub\Projects\ConsoleAppSQLloadExcellCS\ExcelData.xls";
                //string fileName = "ExcelData.xls";
                //string fullFilePath = @"Data\" + fileName; //Data is a folder in projectfolder and .xls is saved there
                //string fullFilePath = Path.Combine(Environment.CurrentDirectory, @"Data\", fileName);
                string fullFilePath = @"ExcelData.xls"; //file path  is ConsoleApplication2\bin\Debug
                //string sheetName = "Sheet1";
                string sheetName = "USDA table";

                SqlConnection SQLConnection = new SqlConnection();
                SQLConnection.ConnectionString = "Data Source = "
                    + SQLServerName + "; Initial Catalog = "
                    + DatabaseName + "; "
                    + "Integrated Security = true";

                string ConStr;
                string HDR;
                HDR = "YES";
                ConStr = "Provider = Microsoft.ACE.OLEDB.12.0; Data Source = "
                    + fullFilePath + "; Extended Properties =\"Excel 12.0; HDR = "
                    + HDR + ";IMEX = 0\"";
                OleDbConnection Conn = new OleDbConnection(ConStr);
                Conn.Open();
                OleDbCommand oconn = new OleDbCommand("select * from [" + sheetName + "$]", Conn);
              
                OleDbDataAdapter adp = new OleDbDataAdapter(oconn);
                DataTable dt = new DataTable();
                adp.Fill(dt);
                Conn.Close();

                SQLConnection.Open();
                //If not exists (select name from sysobjects where name = 'Book2')
                using (SqlCommand command = new SqlCommand("CREATE TABLE Book2 (ID int, Name char(50), Email char(50),Password char(50));", SQLConnection))
                command.ExecuteNonQuery();  // this create new table to database

                using (SqlBulkCopy BC = new SqlBulkCopy(SQLConnection))
                {
                    
                    BC.DestinationTableName = SchemaName + "." + TableName;
                    foreach (var column in dt.Columns)
                    BC.WriteToServer(dt);
                    Console.WriteLine("Database {0} table {1} is Loaded with data from .xls file", DatabaseName, BC.DestinationTableName);
                    Thread.Sleep(3000);
                }
                SQLConnection.Close();
            }
            catch (Exception exception)
            {
                using (StreamWriter sw = File.CreateText(LogFolder
                    + "\\" + "ErrorLog_" + datetime + ".log"))
               {
                   sw.WriteLine(exception.ToString());
               }
            }

            
        }
    }
}
