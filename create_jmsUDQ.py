####################################################################################
# Nome: create_jmsUDQ.py
#
# Autor: Flavio Oliveira - Midlleware
#
# Data: 16 de Marco 2020
#
#
# Descricao: Este python tem como objectivo automatizar a criacao de JMS
#
#
#
# Modificacoes:
#
#
#        Nome          Data               Descricao
#
# Flavio Oliveira    16-03-2020     Criado o ficheiro python
#
#
#
####################################################################################

from java.io import FileInputStream
import java.lang
import os
import string

propInputStream = FileInputStream("/home/oracle/scripts/python/jmsConfig.properties")
configProps = Properties()
configProps.load(propInputStream)

# 1 – Connecting details
serverUrl = configProps.get("server.url")
Username = configProps.get("username")
Password = configProps.get("password")


# 2 – JMSServer details
jmsServerName = configProps.get("jms.server.name")

# 3 – SystemModule Details
systemModuleName = configProps.get("system.module.name")

# 6 – SubDeployment & Queue Details
queueSubDeploymentName = configProps.get("queue.sub.deployment.name")
queueName = configProps.get("queue.name")
queueJNDIName = configProps.get("queue.jndi.name")


# 1 – Connecting to the Destination 
connect(userConfigFile=Username,userKeyFile=Password,url=serverUrl)

# 6 – SubDeployment & Queue Details

edit()
startEdit()
#cd('/JMSSystemResources/'+systemModuleName+'/JMSResource/'+systemModuleName)
#cmo.createQueue(queueName)
#cd('/JMSSystemResources/'+systemModuleName+'/JMSResource/'+systemModuleName+'/Queues/'+queueName)
#cmo.setJNDIName(queueJNDIName)
#cmo.setSubDeploymentName(queueSubDeploymentName)
#cd('/SystemResources/'+systemModuleName+'/SubDeployments/'+queueSubDeploymentName)
##set(‘Targets’,jarray.array([ObjectName(‘com.bea:Name=’+jmsServerName+’,Type=JMSServer’)], ObjectName))
##print “Targeted the Queue to the created subdeployment !!”
#cmo.addTarget(getMBean('/JMSServers/'+jmsServerName))
#activate()


cd('/JMSSystemResources/'+systemModuleName+'/JMSResource/'+systemModuleName)
cmo.createUniformDistributedQueue(queueName)
cd('/JMSSystemResources/'+systemModuleName+'/JMSResource/'+systemModuleName+'/UniformDistributedQueues/'+queueName)
cmo.setJNDIName(queueJNDIName)
#cmo.setDefaultTargetingEnabled(bool("true"))
cmo.setSubDeploymentName(queueSubDeploymentName)
cd('/SystemResources/'+systemModuleName+'/SubDeployments/'+queueSubDeploymentName)
cmo.addTarget(getMBean('/JMSServers/'+jmsServerName))
activate()
