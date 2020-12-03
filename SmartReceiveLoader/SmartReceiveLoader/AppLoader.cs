using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SmartReceiveLoader
{
    class AppLoader : ApplicationContext
    {
        NotifyIcon _notifyIcon;
        ToolStripItem _start_service_item;
        ToolStripItem _stop_service_item;
        public AppLoader()
        {
            _notifyIcon = new NotifyIcon
            {
                ContextMenuStrip = new ContextMenuStrip(),
                Text = Application.ProductName,
                Visible = true,
                Icon = SmartReceiveLoader.Properties.Resources.Icon1
            };
            _start_service_item = _notifyIcon.ContextMenuStrip.Items.Add("Start Service");
            _start_service_item.Click += new EventHandler(delegate(object sender, EventArgs e) 
            {
                _start_service_item.Enabled = false;
                _stop_service_item.Enabled = true;
            });
            _stop_service_item = _notifyIcon.ContextMenuStrip.Items.Add("Stop Service");
            _stop_service_item.Click += new EventHandler(delegate (object sender, EventArgs e)
            {
                _start_service_item.Enabled = true;
                _stop_service_item.Enabled = false;
            });

            _notifyIcon.ContextMenuStrip.Items.Add("-");
            _notifyIcon.ContextMenuStrip.Items.Add("&About", null, new EventHandler(delegate (object sender, EventArgs e)
            {
                MessageBox.Show("OK");
            }));
            _notifyIcon.ContextMenuStrip.Items.Add("-");
            _notifyIcon.ContextMenuStrip.Items.Add("E&xit", null, new EventHandler(delegate (object sender, EventArgs e)
            {
                _notifyIcon.Visible = false;
                this.ExitThread();
            }));
        }

    }
}
