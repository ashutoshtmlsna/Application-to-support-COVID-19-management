import pyorient
import time

#--------------------------------------------------#
#                  process t3                      #
#--------------------------------------------------#
def timequery():
    # database name
    dbname = "covid19-ky"
    # database login is root by default
    login = "root"
    # database password, set by docker param
    password = "rootpwd"

    # create client to connect to local orientdb docker container
    client = pyorient.OrientDB("localhost", 2424)
    session_id = client.connect(login, password)

    while True:
        if client.db_exists(dbname):
            #open the database
            client.db_open(dbname,login,password)
            zips = client.query("SELECT zipcode FROM zipcodes WHERE positive_count >= 2 * last_count AND last_count !=0")
            ziplists = str(len(zips))
            client.command("UPDATE zipcodes SET zipcodealert = '" + ziplists + "'")
            if int(ziplists) >=5:
                client.command("UPDATE zipcodes SET statealert = 1")
            client.command("UPDATE zipcodes SET last_count = positive_count")
            time.sleep(15)
    client.close()

#--------------------------------------------------#
#                     RTR3                         #
#--------------------------------------------------#
def testcounter():
    # database name
    dbname = "covid19-ky"
    # database login is root by default
    login = "root"
    # database password, set by docker param
    password = "rootpwd"

    # create client to connect to local orientdb docker container
    client = pyorient.OrientDB("localhost", 2424)
    session_id = client.connect(login, password)

    # open the database we are interested in
    client.db_open(dbname, login, password)
    positiveCount = client.query("SELECT count(*) FROM patient WHERE patient_status_code = 2 or patient_status_code = 5"
                                 "or patient_status_code = 6")
    negativeCount = client.query("SELECT count(*) FROM patient WHERE patient_status_code = 1 or patient_status_code = 4")
    untested = client.query("SELECT count(*) FROM patient WHERE patient_status_code = 0 or patient_status_code = 3")

    return positiveCount[0].oRecordData['count'], negativeCount[0].oRecordData['count'], untested[0].oRecordData['count']

#--------------------------------------------------#
#                     RTR1                         #
#--------------------------------------------------#
def zipcounter():
    """
        check the zipcodes with growth of 2X over a 15 second time interval
        :return: ziplists in alert state
    """
    # database name
    dbname = "covid19-ky"
    # database login is root by default
    login = "root"
    # database password, set by docker param
    password = "rootpwd"

    # create client to connect to local orientdb docker container
    client = pyorient.OrientDB("localhost", 2424)
    session_id = client.connect(login, password)

    # open the database we are interested in
    client.db_open(dbname, login, password)
    lists = []

    ziplists = client.query("SELECT zipcode FROM zipcodes WHERE positive_count >= 2 * last_count AND last_count !=0")
    for i in range(len(ziplists)):
        lists.append(ziplists[i].oRecordData['zipcode'])
    return lists

#--------------------------------------------------#
#                     RTR2                         #
#--------------------------------------------------#
def statewide():
    """
    Return (1) if at least five zipcodes are in alert state (based on RT1) within the same 15 second window
    :return: state_stat_code = 0 or 1
    """
    # database name
    dbname = "covid19-ky"
    # database login is root by default
    login = "root"
    # database password, set by docker param
    password = "rootpwd"

    # create client to connect to local orientdb docker container
    client = pyorient.OrientDB("localhost", 2424)
    session_id = client.connect(login, password)

    # open the database we are interested in
    client.db_open(dbname, login, password)
    state_status = client.query("SELECT statealert FROM zipcodes")
    state_stat_code = state_status[0].oRecordData['statealert']

    return state_stat_code
