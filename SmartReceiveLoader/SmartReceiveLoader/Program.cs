using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SmartReceiveLoader
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            //Application.Run(new Form1());
            Application.Run(new AppLoader());
        }

        public static void LogIt(String msg)
        {
            System.Diagnostics.Trace.WriteLine($"[SmartReceiveLoader]: {msg}");
        }
    }
}
