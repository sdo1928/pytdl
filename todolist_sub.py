#!/usr/bin/env python

#
# Generated Fri Sep 11 18:37:06 2009 by generateDS.py version 1.18e.
#

import sys
from string import lower as str_lower
from xml.dom import minidom
from xml.sax import handler, make_parser
from xml.dom import Node
import mx.DateTime as DateTime

import todolist as supermod

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#

class TODOLISTSub(supermod.TODOLIST):
    def __init__(self, FILEVERSION=None, PROJECTNAME=None, FILENAME=None, CUSTOMCOMMENTSTYPE=None, LASTMODIFIED=None, EARLIESTDUEDATE=None, NEXTUNIQUEID=None, FILEFORMAT=None, TASK=None, CATEGORY=None, STATUS=None, PERSON=None, ALLOCATEDBY=None, VERSION=None):
        supermod.TODOLIST.__init__(self, FILEVERSION, PROJECTNAME, FILENAME, CUSTOMCOMMENTSTYPE, LASTMODIFIED, EARLIESTDUEDATE, NEXTUNIQUEID, FILEFORMAT, TASK, CATEGORY, STATUS, PERSON, ALLOCATEDBY, VERSION)
    def add_TASK(self, value):
        nextid = self.get_NEXTUNIQUEID()
        if nextid is None:
            nextid = 1
        value.set_ID(nextid)
        nextid = int(nextid) + 1
        self.set_NEXTUNIQUEID(nextid)
        maxpos = 0
        for task in self.get_TASK():
            if int(task.get_POS()) > maxpos:
                maxpos = int(task.get_POS())
        value.set_POS(maxpos + 1)
        self.TASK.append(value)
supermod.TODOLIST.subclass = TODOLISTSub
# end class TODOLISTSub


class TASKSub(supermod.TASK):
    def __init__(self, TASK=None, CATEGORY1=None, STARTDATE=None, CATEGORY3=None, CATEGORY2=None, CATEGORY5=None, CATEGORY4=None, CATEGORY7=None, CATEGORY6=None, CATEGORY9=None, CATEGORY8=None, NUMPERSON=None, PERSON2=None, PERSON3=None, COST=None, EXTERNALID=None, DEPENDS9=None, PERSON4=None, PERSON5=None, DUEDATESTRING=None, ICONINDEX=None, CREATIONDATESTRING=None, PERSON9=None, WEBCOLOR=None, PERSON8=None, LASTMOD=None, TIMEESTUNITS=None, COLOR=None, TITLE=None, LASTMODSTRING=None, PRIORITYWEBCOLOR=None, POS=None, ID=None, PRIORITY=None, CALCTIMESPENT=None, DEPENDS=None, NUMCATEGORY=None, DONEDATESTRING=None, CREATIONDATE=None, PERCENTDONE=None, TIMEESTIMATE=None, STATUS=None, DEPENDS7=None, ALLOCATEDBY=None, DONEDATE=None, RISK=None, STARTDATESTRING=None, TEXTCOLOR=None, NUMDEPENDS=None, CALCPERCENTDONE=None, FLAG=None, VERSION=None, TIMESPENT=None, TEXTWEBCOLOR=None, PRIORITYCOLOR=None, FILEREFPATH=None, DUEDATE=None, CALCTIMEESTIMATE=None, CATEGORY=None, DEPENDS6=None, DEPENDS5=None, DEPENDS4=None, DEPENDS3=None, DEPENDS2=None, DEPENDS1=None, CUSTOMCOMMENTS=None, TIMESPENTUNITS=None, COMMENTS=None, DEPENDS8=None, PERSON=None, PERSON1=None, CALCCOST=None, PERSON6=None, COMMENTSTYPE=None, PERSON7=None, valueOf_=''):
        supermod.TASK.__init__(self, CATEGORY1, STARTDATE, CATEGORY3, CATEGORY2, CATEGORY5, CATEGORY4, CATEGORY7, CATEGORY6, CATEGORY9, CATEGORY8, NUMPERSON, PERSON2, PERSON3, COST, EXTERNALID, DEPENDS9, PERSON4, PERSON5, DUEDATESTRING, ICONINDEX, CREATIONDATESTRING, PERSON9, WEBCOLOR, PERSON8, LASTMOD, TIMEESTUNITS, COLOR, TITLE, LASTMODSTRING, PRIORITYWEBCOLOR, POS, ID, PRIORITY, CALCTIMESPENT, DEPENDS, NUMCATEGORY, DONEDATESTRING, CREATIONDATE, PERCENTDONE, TIMEESTIMATE, STATUS, DEPENDS7, ALLOCATEDBY, DONEDATE, RISK, STARTDATESTRING, TEXTCOLOR, NUMDEPENDS, CALCPERCENTDONE, FLAG, VERSION, TIMESPENT, TEXTWEBCOLOR, PRIORITYCOLOR, FILEREFPATH, DUEDATE, CALCTIMEESTIMATE, CATEGORY, DEPENDS6, DEPENDS5, DEPENDS4, DEPENDS3, DEPENDS2, DEPENDS1, CUSTOMCOMMENTS, TIMESPENTUNITS, COMMENTS, DEPENDS8, PERSON, PERSON1, CALCCOST, PERSON6, COMMENTSTYPE, PERSON7, valueOf_)
        if TASK is None:
            self.TASK = []
        else:
            self.TASK = TASK
        if PRIORITYCOLOR is None or PRIORITYWEBCOLOR is None:
            self.PRIORITYCOLOR = "15732480"
            self.PRIORITYWEBCOLOR = "#000FF0"
        else:
            self.PRIORITYCOLOR = PRIORITYCOLOR
            self.PRIORITYWEBCOLOR = PRIORITYWEBCOLOR
        if COST is None:
            self.COST = '0.00000000'
        else:
            self.COST = COST
        if CREATIONDATE is None or CREATIONDATESTRING is None:
            td = DateTime.today()
            self.CREATIONDATE = td.COMDate()
            self.CREATIONDATESTRING = td.strftime('%m/%d/%Y')
        else:
            self.CREATIONDATE = CREATIONDATE
            self.CREATIONDATESTRING = CREATIONDATESTRING
        if CALCCOST is None:
            self.CALCCOST = '0.00000000'
        else:
            self.CALCCOST = CALCCOST
        if ICONINDEX is None:
            self.ICONINDEX = -1
        else:
            self.ICONINDEX = ICONINDEX
        if PERCENTDONE is None:
            self.PERCENTDONE = 0
        else:
            self.PERCENTDONE = PERCENTDONE
        if PRIORITY is None:
            self.PRIORITY = 5
        else:
            self.PRIORITY = PRIORITY
        if RISK is None:
            self.RISK = 0
        else:
            self.RISK = RISK
        if STARTDATE is None or sTARTDATESTRING is None:
            self.STARTDATE = self.CREATIONDATE
            self.STARTDATESTRING = self.CREATIONDATESTRING
        else:
            self.STARTDATE = STARTDATE
            self.STARTDATESTRING = STARTDATESTRING
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'TASK':
            obj_ = supermod.TASK.factory()
            obj_.build(child_)
            self.TASK.append(obj_)
        elif child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        elif child_.nodeType == Node.CDATA_SECTION_NODE:
            self.valueOf_ += '![CDATA['+child_.nodeValue+']]'
    def get_TASK(self): return self.TASK
    def set_TASK(self, TASK): self.TASK = TASK
    def add_TASK(self, value): self.TASK.append(value)
    def insert_TASK(self, index, value): self.TASK[index] = value
    def exportChildren(self, outfile, level, namespace_='', name_='TASK'):
        for TASK_ in self.TASK:
            TASK_.export(outfile, level, namespace_, name_='TASK')
        if self.valueOf_.find('![CDATA')>-1:
            value=supermod.quote_xml('%s' % self.valueOf_)
            value=value.replace('![CDATA','<![CDATA')
            value=value.replace(']]',']]>')
            outfile.write(value)
        else:
            outfile.write(supermod.quote_xml('%s' % self.valueOf_))
    def hasContent_(self):
        if (
            self.TASK or
            self.valueOf_
            ):
            return True
        else:
            return False
supermod.TASK.subclass = TASKSub
# end class TASKSub



class CATEGORYSub(supermod.CATEGORY):
    def __init__(self, CATEGORY1=None, CATEGORY0=None, CATEGORY3=None, CATEGORY2=None, CATEGORY5=None, CATEGORY4=None, CATEGORY7=None, CATEGORY6=None, CATEGORY9=None, CATEGORY8=None, valueOf_=''):
        supermod.CATEGORY.__init__(self, CATEGORY1, CATEGORY0, CATEGORY3, CATEGORY2, CATEGORY5, CATEGORY4, CATEGORY7, CATEGORY6, CATEGORY9, CATEGORY8, valueOf_)
supermod.CATEGORY.subclass = CATEGORYSub
# end class CATEGORYSub


class STATUSSub(supermod.STATUS):
    def __init__(self, STATUS5=None, STATUS4=None, STATUS7=None, STATUS6=None, STATUS1=None, STATUS0=None, STATUS3=None, STATUS2=None, STATUS9=None, STATUS8=None, valueOf_=''):
        supermod.STATUS.__init__(self, STATUS5, STATUS4, STATUS7, STATUS6, STATUS1, STATUS0, STATUS3, STATUS2, STATUS9, STATUS8, valueOf_)
supermod.STATUS.subclass = STATUSSub
# end class STATUSSub


class PERSONSub(supermod.PERSON):
    def __init__(self, PERSON2=None, PERSON3=None, PERSON0=None, PERSON1=None, PERSON6=None, PERSON7=None, PERSON4=None, PERSON5=None, PERSON8=None, PERSON9=None, valueOf_=''):
        supermod.PERSON.__init__(self, PERSON2, PERSON3, PERSON0, PERSON1, PERSON6, PERSON7, PERSON4, PERSON5, PERSON8, PERSON9, valueOf_)
supermod.PERSON.subclass = PERSONSub
# end class PERSONSub


class ALLOCATEDBYSub(supermod.ALLOCATEDBY):
    def __init__(self, ALLOCATEDBY4=None, ALLOCATEDBY5=None, ALLOCATEDBY6=None, ALLOCATEDBY7=None, ALLOCATEDBY0=None, ALLOCATEDBY1=None, ALLOCATEDBY2=None, ALLOCATEDBY3=None, ALLOCATEDBY8=None, ALLOCATEDBY9=None, valueOf_=''):
        supermod.ALLOCATEDBY.__init__(self, ALLOCATEDBY4, ALLOCATEDBY5, ALLOCATEDBY6, ALLOCATEDBY7, ALLOCATEDBY0, ALLOCATEDBY1, ALLOCATEDBY2, ALLOCATEDBY3, ALLOCATEDBY8, ALLOCATEDBY9, valueOf_)
supermod.ALLOCATEDBY.subclass = ALLOCATEDBYSub
# end class ALLOCATEDBYSub


class VERSIONSub(supermod.VERSION):
    def __init__(self, VERSION4=None, VERSION5=None, VERSION6=None, VERSION7=None, VERSION0=None, VERSION1=None, VERSION2=None, VERSION3=None, VERSION8=None, VERSION9=None, valueOf_=''):
        supermod.VERSION.__init__(self, VERSION4, VERSION5, VERSION6, VERSION7, VERSION0, VERSION1, VERSION2, VERSION3, VERSION8, VERSION9, valueOf_)
supermod.VERSION.subclass = VERSIONSub
# end class VERSIONSub



#
# SAX handler used to determine the top level element.
#
class SaxSelectorHandler(handler.ContentHandler):
    def __init__(self):
        self.topElementName = None
    def getTopElementName(self):
        return self.topElementName
    def startElement(self, name, attrs):
        self.topElementName = name
        raise StopIteration


def parseSelect(inFileName):
    infile = file(inFileName, 'r')
    topElementName = None
    parser = make_parser()
    documentHandler = SaxSelectorHandler()
    parser.setContentHandler(documentHandler)
    try:
        try:
            parser.parse(infile)
        except StopIteration:
            topElementName = documentHandler.getTopElementName()
        if topElementName is None:
            raise RuntimeError, 'no top level element'
        topElementName = topElementName.replace('-', '_').replace(':', '_')
        if topElementName not in supermod.__dict__:
            raise RuntimeError, 'no class for top element: %s' % topElementName
        topElement = supermod.__dict__[topElementName]
        infile.seek(0)
        doc = minidom.parse(infile)
    finally:
        infile.close()
    rootNode = doc.childNodes[0]
    rootObj = topElement.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0)
    return rootObj


def saxParse(inFileName):
    parser = make_parser()
    documentHandler = supermod.Sax_TODOLISTHandler()
    parser.setDocumentHandler(documentHandler)
    parser.parse('file:%s' % inFileName)
    rootObj = documentHandler.getRoot()
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0)
    return rootObj


def saxParseString(inString):
    parser = make_parser()
    documentHandler = supermod.SaxContentHandler()
    parser.setDocumentHandler(documentHandler)
    parser.feed(inString)
    parser.close()
    rootObj = documentHandler.getRoot()
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0)
    return rootObj


def parse(inFilename):
    doc = minidom.parse(inFilename)
    rootNode = doc.documentElement
    rootObj = supermod.TODOLIST.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="TODOLIST",
        namespacedef_='')
    doc = None
    return rootObj


def parseString(inString):
    doc = minidom.parseString(inString)
    rootNode = doc.documentElement
    rootObj = supermod.TODOLIST.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="TODOLIST",
        namespacedef_='')
    return rootObj


def parseLiteral(inFilename):
    doc = minidom.parse(inFilename)
    rootNode = doc.documentElement
    rootObj = supermod.TODOLIST.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('from todolist import *\n\n')
    sys.stdout.write('rootObj = TODOLIST(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="TODOLIST")
    sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    root = parse(infilename)


if __name__ == '__main__':
    main()
    #import pdb
    #pdb.run('main()')


