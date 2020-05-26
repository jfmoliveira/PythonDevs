####################################################################################
# Nome: createUsers.py
#
# Autor: Flavio Oliveira - Midlleware
#
# Data: 16 de Marco 2020
#
#
# Descricao: Este python tem como objectivo automatizar a criacao de utilizadores associando ao grupo
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

# Obtem informacao pelo ficheiro de propriedades
propInputStream = FileInputStream("/home/oracle/scripts/python/users.properties")
configProps = Properties()
configProps.load(propInputStream)

totalGroups_to_Create=configProps.get("total.groups")
totalUsers_to_Create=configProps.get("total.username")

#### Dados que alteram entre ambientes
domainName = 'transsec_domain'
realmName = 'myrealm'
admSvr = "ptmtstrnmchpp01"
admPort = "7001"

##### Dados que nao mudam
adminUserName="/home/oracle/scripts/securefiles/userconfig.secure"
adminPassword="/home/oracle/scripts/securefiles/userkey.secure"
adminURL="t3://"+admSvr+":"+admPort

#Ligar ao ambiente
connect(userConfigFile=adminUserName, userKeyFile=adminPassword, url=adminURL)

#Localizaçao no MBean Correto
authenticatorPath= '/SecurityConfiguration/' + domainName + '/Realms/' + realmName + '/AuthenticationProviders/DefaultAuthenticator'
cd(authenticatorPath)
print ' '
print ' '
print 'Creating Users . . .'
x=1
while (x <= int(totalUsers_to_Create)):
	userName = configProps.get("create.user.name."+ str(x))
	userPassword = configProps.get("create.user.password."+ str(x))
	userDescription = configProps.get("create.user.description."+ str(x))
	try:
		cmo.createUser(userName , userPassword , userDescription)
		print '-----------User Created With Name : ' , userName
	except:
		print '*************** Check If the User With the Name : ' , userName ,' already Exists...'
	x = x + 1
print ' '
print ' '
print 'Adding Groups to users:'
z=1
while (z <= int(totalUsers_to_Create)):
	userName = configProps.get("create.user.name."+ str(z))
	grpName = configProps.get("create.user.group."+ str(z))
	try:
		cmo.addMemberToGroup(grpName,userName)
		print 'USER:' , userName , 'Added to GROUP: ' , grpName
		userName=''
		grpName=''
	except:
		print'********** Check if the group :' , grpName ,' exists...'
	z = z + 1
print ' '
print ' '
