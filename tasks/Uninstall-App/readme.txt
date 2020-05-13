Uninstall3Program("FileZilla Server");

//...

public static bool Uninstall3Program(string ProgramName)
{
    try
    {
        ManagementObjectSearcher mos = new ManagementObjectSearcher(
          "SELECT * FROM Win32_Service WHERE Name = '" + ProgramName + "'");
        foreach (ManagementObject mo in mos.Get())
        {
            try
            {
                if (mo["Name"].ToString() == ProgramName)
                {
                    object hr = mo.InvokeMethod("Uninstall", null);
                    return (bool)hr;
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Failed to uninstall " + ProgramName + " - " + ex.Message);
                //this program may not have a name property, so an exception will be thrown
            }
        }

        //was not found...
        return false;

    }
    catch (Exception ex)
    {
        return false;
    }
}