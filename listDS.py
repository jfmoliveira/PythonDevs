###########################################################################################################################################################
#
#Nome.......:listParDS.py
#Autor......:Flávio Oliveira
#Data.......:25 Janeiro 2019
#Descrição: Obtem informação sobre as configurações das datasources
#
#
#
#Modifacções:
#
# 19-05-2020 Acrescentado para escrever para ficheiro para ser executado via ansible
#
#
#
#############################################################################################################################################################
import sys,os,re

#Inicialização do contador de datasources
dsCounter = 0

#### Dados que alteram entre ambientes
admSvr = "ptmtseaicrtprd01"
admPort = "7001"

#ficheiro de log das DS
f=open("/home/oracle/scripts/logs/datasources.log","w+")


##### Dados que nao mudam
adminUserName="/home/oracle/scripts/securefiles/userconfig.secure"
adminPassword="/home/oracle/scripts/securefiles/userkey.secure"
adminURL="t3://"+admSvr+":"+admPort

#Ligar ao ambiente
connect(userConfigFile=adminUserName, userKeyFile=adminPassword, url=adminURL)

# Obtem todas as datasources e colocas num contentor
allJDBCResources = cmo.getJDBCSystemResources()


# para o caso de correr vi ansible
f.write("\n datasource.url." + str(admSvr))

# Para cada datasource obtem as suas caracteristicas e gurda no respectivo vector
for jdbcResource in allJDBCResources:

        dsCounter +=1 # incrimenta o contados
        dsname = jdbcResource.getName()  # nome da datasource
        dsResource = jdbcResource.getJDBCResource() # resource
        dsJNDIname = dsResource.getJDBCDataSourceParams().getJNDINames() #JNDI
        dsInitialCap = dsResource.getJDBCConnectionPoolParams().getInitialCapacity() #Initial Capacity
        dsMaxCap = dsResource.getJDBCConnectionPoolParams().getMaxCapacity() #Pool params
        dsParams = dsResource.getJDBCDataSourceParams() #Parametros
        dsDriver = dsResource.getJDBCDriverParams().getDriverName() #driver
        conn =  dsResource.getJDBCDriverParams().getUrl() # ligação
        #test = dsResource.getJDBCDriverParams().getProperties()
        #test1 = dsResource.getJDBCConnectionPoolParams()
        user = ''
        readTimeOut = ''
        conTimeOut = ''
        streamAsBlob = ''

        redirect('file','false')
        try :
                user = get("/JDBCSystemResources/"+ dsname +"/Resource/" + dsname + "/JDBCDriverParams/" + dsname + "/Properties/" + dsname + "/Properties/user/Value")
                readTimeOut = get("/JDBCSystemResources/"+ dsname +"/Resource/" + dsname + "/JDBCDriverParams/" + dsname + "/Properties/" + dsname + "/Properties/oracle.jdbc.ReadTimeout/Value")
                conTimeOut = get("/JDBCSystemResources/"+ dsname +"/Resource/" + dsname + "/JDBCDriverParams/" + dsname + "/Properties/" + dsname + "/Properties/oracle.net.CONNECT_TIMEOUT/Value")
                streamAsBlob = get("/JDBCSystemResources/"+ dsname +"/Resource/" + dsname + "/JDBCDriverParams/" + dsname + "/Properties/" + dsname + "/Properties/SendStreamAsBlob/Value")
        except WLSTException:
                # erros omitidos
                pass
        stopRedirect()

        #Impressão dos dados obtidos
        print  str(dsname)
        #print 'datasource.name.' + str(dsCounter) +'=' + str(dsname)
        #print 'datasource.jndiname.' + str(dsCounter) + '=' + str(dsJNDIname)
        #print 'datasource.driver.class.' + str(dsCounter) + '=' + str(dsDriver)
        print 'datasource.url.' + str(dsCounter) + '=' + str(conn)
        f.write("\n" + str(dsname) + ';' + str(conn) + ';' + str(dsInitialCap))
        #print 'datasource.readTimeout.' + str(dsCounter) + '=' + str(readTimeOut)
        #print 'datasource.connectionTimeout.' + str(dsCounter) + '=' + str(conTimeOut)
        #print 'datasource.username.' + str(dsCounter) + '=' + str(user)
        #print 'datasource.initialCapacity.' + str(dsCounter) + '=' + str(dsInitialCap)
        #print 'datasource.maxCapacity.' + str(dsCounter) + '=' + str(dsMaxCap)
        ##print 'datasource.target.' + str(dsCounter) + '=' + str(target)
        if not streamAsBlob :
                getStreamAsBlob = 'false'
        else :
                print '#datasource.sendStreamAsBlob.' + str(dsCounter) + '=' + str(streamAsBlob)

        print '\n'
f.close()
disconnect();
exit()
