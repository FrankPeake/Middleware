import csv, re
from MyClasses import Manufacturer, User, TestLab, TestRestults, Product

def isEmail(email):
    m = re.match('\w+@\w+\.com', email)
    while m is None:
        email = input('Input invalid, please enter a valid email:')
        m = re.match('\w+@\w+\.com', email)
    return email

def isPhoneNumb(phone):
    m = re.match('\d{3}-\d{3}-\d{4}', phone)
    while m is None:
        phone = input('Input invalid, please enter a valid Phone Number:')
        m = re.match('\d{3}-\d{3}-\d{4}', phone)
    return phone

def isDate(date):
    m = re.match('[01][1-9]-[0-3][1-9]-[12][0-9]{3}', date)
    while m is None:
        date = input('Input invalid, please enter a valid Date:')
        m = re.match('[01][1-9]-[0-3][1-9]-[12][0-9]{3}', date)
    return date

def isNumber(number):
    m = re.match('\d+(\.\d*)?', number)
    while m is None:
        number = input('Input invalid, please enter a numberical value:')
        m = re.match('\d+(\.\d*)?', number)
    return number

def getTestResults(fileName):
    fileText = open(fileName,'r')
    getTestResults.fileText = fileText

def userMDS():
    mds = {}

    manufacturer = input("Manufacturer: ")
    location = input('Location: ')
    contact = input('Contact: ')
    address = input('Address: ')
    email = input('Email Address: ')
    email = isEmail(email)
    phone = input('Phone Number: ')
    phone = isPhoneNumb(phone)
    modelNumber = input('Model Number:')
    moduleTotalLenxWid = input('Module Total Length x Width (cm x cm): ')
    moduleWeight = input('Module Weight (kg): ')
    moduleWeight = isNumber(moduleWeight)
    indCellArea = input('Individual Cell Area (cm^2): ')
    indCellArea = isNumber(indCellArea)
    cellTech = input('Cell Technology: ')
    cellManufacturer = input('Cell Manufacturer and part #: ')
    cellManuLocation = input('Cell Manufacturing Location : ')
    totalCells = input('Total Number of Cells: ')
    totalCells = isNumber(totalCells)
    cellSeries = input('Number of cells in series: ')
    cellSeries = isNumber(cellSeries)
    seriesStrings = input('Number of series strings: ')
    seriesStrings = isNumber(seriesStrings)
    bypassDiodes = input('Number of bypass diodes: ')
    bypassDiodes = isNumber(bypassDiodes)
    bypassDiodeRating = input('Bypass Diode Rating(A): ')
    bypassDiodeMaxTemp = input('Bypass Diode Max Junction Temperature(C): ')
    bypassDiodeMaxTemp = isNumber(bypassDiodeMaxTemp)
    seriesFuseRating = input('Series Fuse Rating(A): ')
    seriesFuseRating = isNumber(seriesFuseRating)
    interconnectMatSupModNo = input('Interconnect Material and Supplier Model No.: ')
    interconnectDims = input('Interconnect Dimensions (mm x mm): ')
    superstrateType = input('Superstrate Type: ')
    superstrateMan = input('Superstrate Manufacturer and Part #: ')
    substrateType = input('Substrate Type: ')
    substrateMan = input('Substrate Manufacturer and Part #: ')
    frameType = input('Frame Type/Material: ')
    frameAdhesive = input('Frame Adhesive: ')
    encapsulantType = input('Encapsulant Type: ')
    encapsulantMan = input('Encapsulant Manufacturer and Part #: ')
    juncBoxType = input('Junction Box Type: ')
    juncBoxMan = input('Junction Box Manufacturer and Part #: ')
    juncBoxPottingMat = input('Junction Box Potting Material, if any: ')
    juncBoxAdhesive = input('Junction Box Adhesive: ')
    juncBoxUse = input('Is Junction Box intended for use with Conduit: ')
    cableConnectorType = input('Cable and Connector Type: ')
    maxSysVoltage = input('Max System Voltage: ')
    voc = input('Vmp (V): ')
    voc = isNumber(voc)
    isc = input('Isc (A): ')
    isc = isNumber(isc)
    vmp = input('Vmp (V): ')
    vmp = isNumber(vmp)
    imp = input('Imp (A): ')
    imp = isNumber(imp)
    pmp = input('Pmp (W): ')
    pmp = isNumber(pmp)
    ff = input('FF (%): ')
    ff = isNumber(ff)

    mds['Manufacturer'] = manufacturer
    mds['Location'] = location
    mds['Contact'] = contact
    mds['Address'] = address
    mds['Email'] = email
    mds['Phone'] = phone
    mds['Model Number'] = modelNumber
    mds['Module total length x width (cm x cm)'] = moduleTotalLenxWid
    mds['Module weight(kg)'] = moduleWeight
    mds['Individual Cell Area(cm^2)'] = indCellArea
    mds['Cell Technology'] = cellTech
    mds['Cell Manufacturer and part #'] = cellManufacturer
    mds['Cell Manufacturing Location'] = cellManuLocation
    mds['Total Number of Cells'] = totalCells
    mds['Number of cells in series'] = cellSeries
    mds['Number of series strings'] = seriesStrings
    mds['Number of bypass diodes'] = bypassDiodes
    mds['Bypass Diode Rating(A)'] = bypassDiodeRating
    mds['Bypass Diode Max Junction Temperature(C)'] = bypassDiodeMaxTemp
    mds['Series Fuse Rating(A)'] = seriesFuseRating
    mds['Interconnect Material and Supplier Model No.'] = interconnectMatSupModNo
    mds['Interconnect Dimensions (mm x mm)'] = interconnectDims
    mds['Superstrate Type'] = superstrateType
    mds['Substrate Manufacturer and Part #'] = superstrateMan
    mds['Substrate Type'] = substrateType
    mds['Substrate Manufacturer and Part #'] = substrateMan
    mds['Frame Type/Material'] = frameType
    mds['Frame Adhesive'] = frameAdhesive
    mds['Encapsulant Type'] = encapsulantType
    mds['Encapsulant Manufacturer and Part #'] = encapsulantMan
    mds['Junction Box Type'] = juncBoxType
    mds['Junction Box Manufacturer and Part #'] = juncBoxMan
    mds['Junction Box Potting Material, if any'] = juncBoxPottingMat
    mds['Junction Box Adhesive'] = juncBoxAdhesive
    mds['Is Junction Box intended for use with Conduit'] = juncBoxUse
    mds['Cable and Connector Type'] = cableConnectorType
    mds['Max System Voltage'] = maxSysVoltage
    mds['Voc (V)'] = voc
    mds['Isc (A)'] = isc
    mds['Vmp (V)'] = vmp
    mds['Imp (A)'] = imp
    mds['Pmp (W)'] = pmp
    mds['FF (%)'] = ff

    return mds

def userRegister():
    user = {}

    username = input('Username: ')
    password = input('Password: ')
    firstName = input('First Name: ')
    middleName = input('Middle Name (optional): ')
    lastName = input('Last Name: ')
    compName = input('Company Name: ')
    compType = input('Company Type (Test Lab or Manufacturer): ')
    address = input('Address: ')
    officePhoneNo = input('Office Number: ')
    cellPhoneNo = input('Cell Phone:')
    email = input('Email: ')
    email = isEmail(email)

    user['Username'] = username
    user['Password'] = password
    user['First Name'] = firstName
    user['Middle Name (optional)'] = middleName
    user['Last Name'] = lastName
    user['Company Name'] = compName
    user['Company Type (Test Lab or Manufacturer)'] = compType
    user['Address'] = address
    user['Office Phone Number'] = officePhoneNo
    user['Cell Phone Number'] = cellPhoneNo
    user['Email'] = email 

    return user

def main():
    
    mds = userMDS()
    user = userRegister()
    
    manufacturer = mds['Manufacturer']
    firstName = user['First Name']
    lastName = user['Last Name']
    email = user['Email']
    modelNumber = mds['Model Number']
    cellTechnology = mds['Cell Technology']
    maxSysVoltage = mds['Max System Voltage']
    pmp = mds['Pmp (W)']

    p = Product(mds)
    u = User(user)
    m = Manufacturer(user)
    t = TestLab(user)

    p.setManufacturer(manufacturer)
    m.setName(manufacturer)
    u.setFirstName(firstName)
    u.setLastName(lastName)
    t.setContactPerson(firstName, lastName)
    u.setEmail(email)
    p.setModelNumber(modelNumber)
    p.setCellTech(cellTechnology)
    p.setMaxSysVoltage(maxSysVoltage)
    p.setRatedPMP(pmp)

    print ('Manufacturer: ', m.getName(), '\nContact Name: ', u.getFirstName() + u.getLastName(), '\nContact Email: ', u.getEmail(), '\nModel Number: ', p.getModelNumber(), '\nCell Technology: ', p.getCellTech(), '\nSystem Voltage: ', p.getMaxSysVoltage(), '\nRated Power (Pmp): ', p.getRatedPMP())


    manufacturer = mds['Manufacturer']
    location = mds['Location'] 
    contact = mds['Contact'] 
    address = mds['Address'] 
    email = mds['Email']  
    phone = mds['Phone'] 
    modelNumber = mds['Model Number'] 
    moduleTotalLenxWid = mds['Module total length x width (cm x cm)']  
    moduleWeight = mds['Module weight(kg)'] 
    indCellArea = mds['Individual Cell Area(cm^2)'] 
    cellTech = mds['Cell Technology'] 
    cellManufacturer = mds['Cell Manufacturer and part #']
    cellManuLocation = mds['Cell Manufacturing Location'] 
    totalCells = mds['Total Number of Cells']
    cellSeries = mds['Number of cells in series'] 
    seriesStrings = mds['Number of series strings'] 
    bypassDiodes = mds['Number of bypass diodes'] 
    bypassDiodeRating = mds['Bypass Diode Rating(A)'] 
    bypassDiodeMaxTemp = mds['Bypass Diode Max Junction Temperature(C)'] 
    seriesFuseRating = mds['Series Fuse Rating(A)'] 
    interconnectMatSupModNo = mds['Interconnect Material and Supplier Model No.'] 
    interconnectDims = mds['Interconnect Dimensions (mm x mm)'] 
    superstrateType = mds['Superstrate Type'] 
    superstrateMan = mds['Substrate Manufacturer and Part #'] 
    substrateType = mds['Substrate Type'] 
    substrateMan = mds['Substrate Manufacturer and Part #'] 
    frameType = mds['Frame Type/Material'] 
    frameAdhesive = mds['Frame Adhesive'] 
    encapsulantType = mds['Encapsulant Type'] 
    encapsulantMan = mds['Encapsulant Manufacturer and Part #'] 
    juncBoxType = mds['Junction Box Type'] 
    juncBoxMan = mds['Junction Box Manufacturer and Part #'] 
    juncBoxPottingMat = mds['Junction Box Potting Material, if any'] 
    juncBoxAdhesive = mds['Junction Box Adhesive'] 
    juncBoxUse = mds['Is Junction Box intended for use with Conduit'] 
    cableConnectorType = mds['Cable and Connector Type'] 
    maxSysVoltage = mds['Max System Voltage'] 
    voc = mds['Voc (V)'] 
    isc = mds['Isc (A)'] 
    vmp = mds['Vmp (V)'] 
    imp = mds['Imp (A)'] 
    pmp = mds['Pmp (W)'] 
    ff = mds['FF (%)']
        
    import mysql.connector
    db = mysql.connector.connect(user ='root', host = 'localhost', password ='Fiddlere2012!', db='py')
    cursor = db.cursor() 
    input1 = (manufacturer, location, contact, address, email, phone, modelNumber, moduleTotalLenxWid, moduleWeight, indCellArea, cellTech, cellManufacturer, cellManuLocation, totalCells, cellSeries, seriesStrings, bypassDiodes, bypassDiodeRating, bypassDiodeMaxTemp, seriesFuseRating, interconnectMatSupModNo, interconnectDims, superstrateType, superstrateMan, substrateType, substrateMan, frameType, frameAdhesive, encapsulantType, encapsulantMan, juncBoxType, juncBoxMan, juncBoxPottingMat, juncBoxAdhesive, juncBoxUse, cableConnectorType, maxSysVoltage, voc, isc, vmp, imp, pmp, ff)  
    sql = ('INSERT INTO MDS (manufacturer, location, contact, address, email, phone, modelNumber, moduleTotalLenxWid, moduleWeight, indCellArea, cellTech, cellManufacturer, cellManuLocation, totalCells, cellSeries, seriesStrings, bypassDiodes, bypassDiodeRating, bypassDiodeMaxTemp, seriesFuseRating, interconnectMatSupModNo, interconnectDims, superstrateType, superstrateMan, substrateType, substrateMan, frameType, frameAdhesive, encapsulantType, encapsulantMan, juncBoxType, juncBoxMan, juncBoxPottingMat, juncBoxAdhesive, juncBoxUse, cableConnectorType, maxSysVoltage, voc, isc, vmp, imp, pmp, ff) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)') 
    cursor.execute(sql, input1)
    db.commit()
 
    fileName = input('Enter name of Test Result File: ')

    getTestResults(fileName)

    count = 0
    count2 = 0
    avgISC = 0
    avgVOC = 0
    avgPmax = 0
    avgPmaxDrop = 0 

    for line in getTestResults.fileText:
        if count >= 1:
            line = line.rstrip('\n')
            values = line.split(',')
            input2 = (values[0],  values[1],  values[2],  values[3],  values[4],  values[5],  values[6],  values[7],  values[8],  values[9])
            sql2 = ('INSERT INTO TestResults (model, testSequence, conditions, date, isc, voc, imp, vmp, ff, pmp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)')
            cursor.execute(sql2, input2)
            db.commit()

            count += 1
        elif count == 0:
            count += 1

    select = ('SELECT manufacturer, contact, email, cellTech, seriesFuseRating FROM mds')
    cursor.execute(select)
    
    for data in cursor.fetchall():
        print ( ('-'*71 + '\n|Manufacturer      | %s\n' + '-'*71 + '\n|Contact Name      | %s\n' + '-'*71 + '\n|Contact Email     | %s\n' + '-'*71 + '\n|Cell Technology   | %s\n' + '-'*71 + '\n|Rated Power       | %s') % data )

    select2 = ('SELECT isc, voc, pmp FROM testresults WHERE testSequence = "Baseline"')
    cursor.execute(select2)
    
    for data in cursor.fetchall():
        avgISC = avgISC + data[0]
        avgISC = round(avgISC, 2) 
        avgVOC = avgVOC + data[1]
        avgVOC = round(avgVOC, 2)
        avgPmax = avgPmax + data[2]
        avgPmax = round(avgPmax, 2)
        avgPmaxDrop = 0
        count2 += 1

    avgISC = avgISC/count2
    avgISC= round(avgISC, 2)
    avgVOC = avgVOC/count2
    avgVOC = round(avgVOC, 2)
    avgPmax = avgPmax/count2
    avgPmax = round(avgPmax, 2)

    baseline = (avgISC, avgVOC, avgPmax, avgPmaxDrop)

    count2 = 0
    avgISC = 0
    avgVOC = 0
    avgPmax = 0

    select3 = ('SELECT isc, voc, pmp FROM testresults WHERE testSequence = "TC200"')
    cursor.execute(select3)
    
    for data in cursor.fetchall():
        avgISC = avgISC + data[0]
        avgISC = round(avgISC, 2) 
        avgVOC = avgVOC + data[1]
        avgVOC = round(avgVOC, 2)
        avgPmax = avgPmax + data[2]
        avgPmax = round(avgPmax, 2)
        avgPmaxDrop = 0
        count2 += 1

    avgISC = avgISC/count2
    avgISC= round(avgISC, 2)
    avgVOC = avgVOC/count2
    avgVOC = round(avgVOC, 2)
    avgPmax = avgPmax/count2
    avgPmax = round(avgPmax, 2)
    avgPmaxDrop = ((baseline[2] - avgPmax)/baseline[2])*100
    avgPmaxDrop = round(avgPmaxDrop, 2)

    tc200 = (avgISC, avgVOC, avgPmax, avgPmaxDrop)

    count2 = 0
    avgISC = 0
    avgVOC = 0
    avgPmax = 0
    avgPmaxDrop = 0

    select4 = ('SELECT isc, voc, pmp FROM testresults WHERE testSequence = "Damp Heat"')
    cursor.execute(select4)
    
    for data in cursor.fetchall():
        avgISC = avgISC + data[0]
        avgISC = round(avgISC, 2) 
        avgVOC = avgVOC + data[1]
        avgVOC = round(avgVOC, 2)
        avgPmax = avgPmax + data[2]
        avgPmax = round(avgPmax, 2)
        count2 += 1

    avgISC = avgISC/count2
    avgISC= round(avgISC, 2)
    avgVOC = avgVOC/count2
    avgVOC = round(avgVOC, 2)
    avgPmax = avgPmax/count2
    avgPmax = round(avgPmax, 2)
    avgPmaxDrop = ((baseline[2] - avgPmax)/baseline[2])*100
    avgPmaxDrop = round(avgPmaxDrop, 2)

    dampHeat = (avgISC, avgVOC, avgPmax, avgPmaxDrop)

    count2 = 0
    avgISC = 0
    avgVOC = 0
    avgPmax = 0
    avgPmaxDrop = 0

    select5 = ('SELECT isc, voc, pmp FROM testresults WHERE testSequence = "HF10"')
    cursor.execute(select5)
    
    for data in cursor.fetchall():
        avgISC = avgISC + data[0]
        avgISC = round(avgISC, 2) 
        avgVOC = avgVOC + data[1]
        avgVOC = round(avgVOC, 2)
        avgPmax = avgPmax + data[2]
        avgPmax = round(avgPmax, 2)
        count2 += 1

    avgISC = avgISC/count2
    avgISC= round(avgISC, 2)
    avgVOC = avgVOC/count2
    avgVOC = round(avgVOC, 2)
    avgPmax = avgPmax/count2
    avgPmax = round(avgPmax, 2)
    avgPmaxDrop = ((baseline[2] - avgPmax)/baseline[2])*100
    avgPmaxDrop = round(avgPmaxDrop, 2)

    hf10 = (avgISC, avgVOC, avgPmax, avgPmaxDrop)

    avgISC = (baseline[0], tc200[0], dampHeat[0], hf10[0])
    avgVOC = (baseline[1], tc200[1], dampHeat[1], hf10[1])
    avgPmax = (baseline[2], tc200[2], dampHeat[2], hf10[2])
    avgPmaxDrop = (baseline[3], tc200[3], dampHeat[3], hf10[3])

    print("-"*71)
    print("|                  |Baseline\t|TC300    \t|Damp Heat\t|HF10 |") 
    print("-"*71)
    print("|Average Isc       | %s     \t|%s     \t|%s     \t|%s " % avgISC)
    print("-"*71) 
    print("|Average Voc       | %s     \t|%s     \t|%s     \t|%s" % avgVOC)
    print("-"*71)
    print("|Average Pmax      | %s\t|%s         \t|%s \t|%s" % avgPmax)
    print("-"*71)
    print("|Average Pax Drop  | %s     \t|%s     \t|%s     \t|%s " % avgPmaxDrop)
    print("-"*71)  
if __name__ == '__main__':
    main()


