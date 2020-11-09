class Manufacturer:

    def __init__ (self, name='Adam', registered_country='America', contact_person='Eve'):
        self.name = name
        self.registered_country = registered_country
        self.contact_person = contact_person

    def setName (self, name):
        self.name = name
    def setRegisteredCountry (self, registered_country):
        self.registered_country = registered_country
    def setContactPerson (self, contact_person):
        self.contact_person = contact_person

    def getName (self):
        return self.name
    def getRegisteredCountry (self):
        return self.registered_country
    def getContactPerson (self):
        return self.contact_person

class User:

    def __init__(self, username='username', password='password', first_name='Jane', middle_name='A', last_name='Doe', company_name='company', company_type='company type',
    address='123 address', officePhone='(111) 111-1111', cellphone='(111) 111-1111', email='email@email.com'):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.company_name = company_name
        self.company_type = company_type
        self.address = address
        self.officePhone = officePhone
        self.cellphone = cellphone
        self.email = email

    def setUsername (self, username):
        self.username = username
    def setPassword (self, password):
        self.password = password
    def setFirstName (self, first_name):
        self.first_name = first_name
    def setMiddleName (self, middle_name):
        self.middle_name = middle_name
    def setLastName (self, last_name):
        self.last_name = last_name
    def setCompanyName (self, company_name):
        self.company_name = company_name
    def setCompanyType (self, company_type):
        self.company_type = company_type
    def setAddress (self, address):
        self.address = address
    def setOfficePhone (self, officePhone):
        self.officePhone = officePhone
    def setCellPhone (self, cellphone):
        self.cellphone = cellphone
    def setEmail (self, email):
        self.email = email

    def getUsername (self):
        return self.username
    def getPassword (self):
        return self.password
    def getFirstName (self):
        return self.first_name
    def getMiddleName (self):
        return self.middle_name
    def getLastName (self):
        return self.last_name
    def getCompanyName (self):
        return self.company_name
    def getCompanyType (self):
        return self.company_type
    def getAddress (self):
        return self.address
    def getOfficePhone (self):
        return self.officePhone
    def getCellPhone (self):
        return self.cellphone
    def getEmail (self):
        return self.email

class TestRestults:
    def __init__(self, dataSource='TestLab', product='Product', reportingCondition='N/A', testSequence='N/A', testDate='N/A',
    isc='N/A', voc='N/A', imp='N/A', vmp='N/A', pmp='N/A', ff='N/A', noct='N/A'):
        self.dataSource = dataSource
        self.product = product
        self.reportingCondition = reportingCondition
        self.testSequence = testSequence
        self.testDate = testDate
        self.isc = isc
        self.voc = voc
        self.imp = imp
        self.vmp = vmp
        self.pmp = pmp
        self.ff = ff
        self.noct = noct

    def setDataSource (self, dataSource):
        self.dataSource = dataSource
    def setProduct (self, product):
        self.product = product
    def setReportCondition (self, reportingCondition):
        self.reportingCondition = reportingCondition
    def setTestSequence (self, testSequence):
        self.testSequence = testSequence
    def setTestDate (self, testDate):
        self.testDate = testDate
    def setISC (self, isc):
        self.isc = isc
    def setVOC (self, voc):
        self.voc = voc
    def setIMP (self, imp):
        self.imp = imp
    def setVMP (self, vmp):
        self.vmp = vmp
    def setPMP (self, pmp):
        self.pmp = pmp
    def setFF (self, ff):
        self.ff = ff
    def setNOCT (self, noct):
        self.noct = noct

    def getDataSource (self):
        return self.dataSource
    def getProduct (self):
        return self. product
    def getReportCondition (self):
        return self.reportingCondition
    def getTestSequence (self):
        return self.testSequence
    def getTestDate (self):
        return self.testDate
    def getISC (self):
        return self.isc
    def getVOC (self):
        return self.voc
    def getIMP (self):
        return self.imp
    def getVMP (self):
        return self.vmp
    def getPMP (self):
        return self.pmp
    def getFF (self):
        return self.ff
    def getNOCT (self):
        return self.noct

class TestLab:
    def __init__(self, name='Adam', address='123 address', contact_person='Eve'):
        self.name = name
        self.address = address
        self.contact_person = contact_person

    def setName (self, name):
        self.name = name
    def setAddress (self, address):
        self.address = address
    def setContactPerson (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def getName (self):
        return self.name
    def getAddress (self):
        return self.address
    def getContactPerson (self):
        return self.contact_person

class Product:
    
    def __init__(self, modelNumber='1234', manufacturer='N/A', manufacturingDate='00/00/0000', length='1.00', width='1.00', weight='1.00',
    cellArea='1.00', cellTechnology='N/A', totalCells='1', cellsSeries='1', stringsSeries='1', bypassDiodes='1', seriesFuseRating='1.00',
    interconnectMaterial='N/A', interconnectSupplier='N/A', superstrateType='N/A', superstrateManufacturer='N/A', substrateType='N/A',
    substrateManufacturer='N/A', frameMaterial='N/A', frameAdhesive='N/A', encapsulantTyoe='N/A', encapuslantManufactuer='N/A', 
    junctionBoxType='N/A', junctionBoxManufacturer='N/A', junctionBoxAdhesive='N/A', cableType='N/A', connectorType='N/A',
    maxSystemVoltage='1.00', ratedVOC='1.00', ratedISC='1.00', ratedVMP='1.00', ratedIMP='1.00', ratedPMP='1.00', ratedFF='1.00'):
        self.modelNumber = modelNumber
        self.manufacturer = manufacturer
        self.manufacturingDate = manufacturingDate
        self.length = length
        self.width = width
        self.weight = weight
        self.cellArea = cellArea
        self.cellTechnology = cellTechnology
        self.totalCells = totalCells
        self.cellsSeries = cellsSeries
        self.stringsSeries = stringsSeries
        self.bypassDiodes = bypassDiodes
        self.seriesFuseRating = seriesFuseRating
        self.interconnectMaterial = interconnectMaterial
        self.interconnectSupplier = interconnectSupplier
        self.superstrateType = superstrateType
        self.superstrateManufacturer = superstrateManufacturer
        self.substrateType = substrateType
        self.substrateManufacturer = substrateManufacturer
        self.frameMaterial = frameMaterial
        self.frameAdhesive = frameAdhesive
        self.encapsulantTyoe = encapsulantTyoe
        self.encapuslantManufactuer = encapuslantManufactuer
        self.junctionBoxType = junctionBoxType
        self.junctionBoxManufacturer = junctionBoxManufacturer
        self.junctionBoxAdhesive = junctionBoxAdhesive
        self.cableType = cableType
        self.connectorType = connectorType
        self.maxSystemVoltage = maxSystemVoltage
        self.ratedVOC = ratedVOC
        self.ratedISC = ratedISC
        self.ratedVMP = ratedVMP
        self.ratedIMP = ratedIMP
        self.ratedPMP = ratedPMP
        self.ratedFF = ratedFF

    def setModelNumber (self, modelNumber):
        self.modelNumber = modelNumber
    def setManufacturer (self, manufacturer):
        self.manufacturer = manufacturer
    def setManufacturingDate (self, manufacturingDate):
        self.manufacturingDate = manufacturingDate
    def setLength (self, length):
        self.length = length
    def setWidth (self, width):
        self.width = width
    def setWeight (self, weight):
        self.weight = weight
    def setCellArea (self, cellArea):
        self.cellArea = cellArea
    def setCellTech (self, cellTechnology):
        self.cellTechnology = cellTechnology
    def setTotalCells (self, totalCells):
        self.totalCells = totalCells
    def setCellsSeries (self, cellsSeries):
        self.cellsSeries = cellsSeries
    def setStringsSeries (self, stringsSeries):
        self.stringsSeries = stringsSeries
    def setBypassDiodes (self, bypassDiodes):
        self.bypassDiodes = bypassDiodes
    def setFuseRating (self, seriesFuseRating):
        self.seriesFuseRating = seriesFuseRating
    def setInterconnectMaterial (self, interconnectMaterial):
        self.interconnectMaterial = interconnectMaterial
    def setInterconnectSupplier (self, interconnectSupplier):
        self.interconnectSupplier = interconnectSupplier
    def setSuperstrateType (self, superstrateType):
        self.superstrateType = superstrateType
    def setSuperstrateManufacturer (self, superstrateManufacturer):
        self.superstrateManufacturer = superstrateManufacturer
    def setSubstrateType (self, substrateType):
        self.substrateType = substrateType
    def setSubstrateManufacturer (self, substrateManufacturer):
        self.substrateManufacturer = substrateManufacturer
    def setFrameMaterial (self, frameMaterial):
        self.frameMaterial = frameMaterial
    def setFrameAdhesive (self, frameAdhesive):
        self.frameAdhesive = frameAdhesive
    def setEncapsulantType (self, encapsulantTyoe):
        self.encapsulantTyoe = encapsulantTyoe
    def setEncapsulantManufacturer (self, encapuslantManufactuer):
        self.encapuslantManufactuer = encapuslantManufactuer
    def setJunctionBoxType (self, junctionBoxType):
        self.junctionBoxType = junctionBoxType
    def setJunctionBoxManufacturer (self, junctionBoxManufacturer):
        self.junctionBoxManufacturer = junctionBoxManufacturer
    def setJunctionBoxAdhesive (self, junctionBoxAdhesive):
        self.junctionBoxAdhesive = junctionBoxAdhesive
    def setCableType (self, cableType):
        self.cableType = cableType
    def setConnectorType (self, connectorType):
        self.connectorType = connectorType
    def setMaxSysVoltage (self, maxSystemVoltage):
        self.maxSystemVoltage = maxSystemVoltage
    def setRatedVOC (self, ratedVOC):
        self.ratedVOC = ratedVOC
    def setRatedISC (self, ratedISC):
        self.ratedISC = ratedISC
    def setRatedVMP (self, ratedVMP):
        self.ratedVMP = ratedVMP
    def setRatedIMP (self, ratedIMP):
        self.ratedIMP = ratedIMP
    def setRatedPMP (self, ratedPMP):
        self.ratedPMP = ratedPMP
    def setRatedFF (self, ratedFF):
        self.ratedFF = ratedFF

    def getModelNumber (self):
        return self.modelNumber
    def getManufacturer (self):
        return self.manufacturer
    def getManufacturingDate (self):
        return self.manufacturingDate
    def getLength (self):
        return self.length
    def getWidth (self):
        return self.width
    def getWeight (self):
        return self.weight
    def getCellArea (self):
        return self.cellArea
    def getCellTech (self):
        return self.cellTechnology
    def getTotalCells (self):
        return self.totalCells
    def getCellsSeries (self):
        return self.cellsSeries
    def getStringsSeries (self):
        return self.stringsSeries
    def getBypassDiodes (self):
        return self.bypassDiodes
    def getFuseRating (self):
        return self.seriesFuseRating
    def getInterconnectMaterial (self):
        return self.interconnectMaterial
    def getInterconnectSupplier (self):
        return self.interconnectSupplier
    def getSuperstrateType (self):
        return self.superstrateType
    def getSuperstrateManufacturer (self):
        return self.superstrateManufacturer
    def getSubstrateType (self):
        return self.substrateType
    def getSubstrateManufacturer (self):
        return self.substrateManufacturer
    def getFrameMaterial (self):
        return self.frameMaterial
    def getFrameAdhesive (self):
        return self.frameAdhesive
    def getEncapsulantType (self):
        return self.encapsulantTyoe
    def getEncapsulantManufacturer (self):
        return self.encapuslantManufactuer
    def getJunctionBoxType (self):
        return self.junctionBoxType
    def getJunctionBoxManufacturer (self):
        return self.junctionBoxManufacturer
    def getJunctionBoxAdhesive (self):
        return self.junctionBoxAdhesive
    def getCableType (self):
        return self.cableType
    def getConnectorType (self):
        return self.connectorType
    def getMaxSysVoltage (self):
        return self.maxSystemVoltage
    def getRatedVOC (self):
        return self.ratedVOC
    def getRatedISC (self):
        return self.ratedISC
    def getRatedVMP (self):
        return self.ratedVMP
    def getRatedIMP (self):
        return self.ratedIMP
    def getRatedPMP (self):
        return self.ratedPMP
    def getRatedFF (self):
        return self.ratedFF
