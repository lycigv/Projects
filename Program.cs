using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FileCheck
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Begin File Transfer...\n");

            // Set up default values
            string originPath = "C:\\FolderA\\";
            string destPath = "C:\\FolderB\\";
            string fileType = "*.txt";

            Console.WriteLine("From: {0}", originPath);
            Console.WriteLine("To: {0}\n", destPath);

            // Get all text files
            string[] txtFilesArray = Directory.GetFiles(originPath, fileType);

            // Loop through files
            foreach (string file in txtFilesArray)
            {
                // If file was modified withi 24 hours, then copy to FolderB
                if (FileCheck(file))
                {
                    string fileName = Path.GetFileName(file);

                    Console.WriteLine("Copying ... {0}", fileName);

                    File.Copy(file, destPath + fileName, true);
                }
            }

            Console.WriteLine("\nFile Transfer Complete ... Press ENTER");
            Console.ReadLine();
        }

        public static bool FileCheck(string FileName)
        {
                        //  file check to see if it was modified within 
                           /* the last 24 hours*/


            // Get the attributes of the file
            FileInfo fileNameInfo = new FileInfo(FileName);

            // Check the last modify date
            if (fileNameInfo.LastWriteTime.AddDays(1) >= DateTime.Now)
                return true;
            else
                return false;
        }
    }
    }

