import subprocess


def run_testcase():
    #checked_testcases = request.POST.getlist('testcases')
    #return HttpResponse("Inside Run : " + checked_testcases[0] + ' --- ' + checked_testcases[1])
    #file_path = ''
    #file_name = ''
    #file = file_path + file_name
    #subprocess.call(test.py, shell=True)
    command = 'python test.py'
    for line in run_command(command):
        print 'Each Line: ' + line
	
def run_command(command): 
    print 'here'
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')
	
	
run_testcase()