#Here is a description of what each script does….
- **0-current_working_directory:** This script prints the current working directory
- **1-listit**: This lists the contents of the current working directory
- **2-bring_me_home:** Changes the current working directory to the home directory
- **3-listfiles:** Lists the contents of the current working directory in long format
- **4-listmorefiles:** Lists all the contents of the working directory including hidden files
- **5-listfilesdigitonly:** Lists contents  working directory including hidden files in
long format with user and group IDs displayed numerically
- **6-firstdirectory:** Creates a directory named my_first_directory in tmp/ directory
- **7-movethatfile:** Moves file Betty from the tmp/ directory to tmp/my_first_directory 
- **8-firstdelete:** This deletes the file betty from tmp/my_first_directory
- **9-firstdirdeletion:** This deletes my_first_directory from the tmp/ directory
- **10-back:** Changes directory from current working directory to previous directory
- **11-lists:** Long format list of all files even hidden files in the current directory, 
parent of current directory and /boot directory in that order
- **12-file_type:** prints the type of file iamafile which is present inside tmp/ is
- **13-symbolic_link:** This creates a symbolic link to /bin/ls with the name _ls_ in the working directory
- **14-copy_html:** Copies all html files from the current directory to the parent directory but only 
copy files that do not exist in or are newer in version than the parent directory
