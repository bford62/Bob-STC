import os
from behave import given, when, then
import sys
# context: where behave runs
sys.path.insert(1, 'lib/')
import wcommon as wc
wc.jenkins_header(); # load inputs from Jenkinsfile
wc.wcheader['packages']['wc'] = wc.__file__
wc.jd(wc.wcheader)
ARC = '10.88.240.60'; # CHASSIS2
WP = '10.44.0.21'; # CHASSIS1
os.environ['STC_PRIVATE_INSTALL_DIR'] = STC_PRIVATE_INSTALL_DIR = '/opt/STC_5.16/Spirent_TestCenter_5.16/Spirent_TestCenter_Application_Linux'
import Stc

@given(u'Spirent config built')
def step_impl(context):
	system1,project = Stc.init('traffictest.py')
	Stc.connectChassis(ARC)
	assert True

@when(u'I try to ping "{ip}"')
def step_impl(context, ip):
	context.ip = ip
	context.pingable = bool(wc.is_pingable(ip))
	print('\t'.join(['','PID',str(os.getpid())]))
	pass

@then(u'I expect response "{expectationBoolean}"')
def step_impl(context, expectationBoolean):
	expectationBoolean = wc.bdd_bool_inp(expectationBoolean)
	print('\t'.join(['',context.ip,'actual:' + str(context.pingable),'','expected:' + str(expectationBoolean)]))
	assert context.pingable == expectationBoolean

Stc.disconnectChassis()
