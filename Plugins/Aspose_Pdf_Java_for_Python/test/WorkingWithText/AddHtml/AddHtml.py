__author__ = 'fahadadeel'
import jpype
import os.path
from WorkingWithText import AddHtml

asposeapispath = os.path.join(os.path.abspath("../../../"), "lib")

print "You need to put your Aspose.Words for Java APIs .jars in this folder:\n"+asposeapispath

jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.ext.dirs=%s" % asposeapispath)

testObject = AddHtml('data/')
testObject.main()