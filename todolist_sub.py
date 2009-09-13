#!/usr/bin/env python

#
# Generated Fri Sep 11 18:37:06 2009 by generateDS.py version 1.18e.
#

import sys
from string import lower as str_lower
from xml.dom import minidom
from xml.sax import handler, make_parser

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
supermod.TODOLIST.subclass = TODOLISTSub
# end class TODOLISTSub


class TASKSub(supermod.TASK):
    def __init__(self, CATEGORY1=None, STARTDATE=None, CATEGORY3=None, CATEGORY2=None, CATEGORY5=None, CATEGORY4=None, CATEGORY7=None, CATEGORY6=None, CATEGORY9=None, CATEGORY8=None, NUMPERSON=None, PERSON2=None, PERSON3=None, COST=None, EXTERNALID=None, DEPENDS9=None, PERSON4=None, PERSON5=None, DUEDATESTRING=None, ICONINDEX=None, CREATIONDATESTRING=None, PERSON9=None, WEBCOLOR=None, PERSON8=None, LASTMOD=None, TIMEESTUNITS=None, COLOR=None, TITLE=None, LASTMODSTRING=None, PRIORITYWEBCOLOR=None, POS=None, ID=None, PRIORITY=None, CALCTIMESPENT=None, DEPENDS=None, NUMCATEGORY=None, DONEDATESTRING=None, CREATIONDATE=None, PERCENTDONE=None, TIMEESTIMATE=None, STATUS=None, DEPENDS7=None, ALLOCATEDBY=None, DONEDATE=None, RISK=None, STARTDATESTRING=None, TEXTCOLOR=None, NUMDEPENDS=None, CALCPERCENTDONE=None, FLAG=None, VERSION=None, TIMESPENT=None, TEXTWEBCOLOR=None, PRIORITYCOLOR=None, FILEREFPATH=None, DUEDATE=None, CALCTIMEESTIMATE=None, CATEGORY=None, DEPENDS6=None, DEPENDS5=None, DEPENDS4=None, DEPENDS3=None, DEPENDS2=None, DEPENDS1=None, CUSTOMCOMMENTS=None, TIMESPENTUNITS=None, COMMENTS=None, DEPENDS8=None, PERSON=None, PERSON1=None, CALCCOST=None, PERSON6=None, COMMENTSTYPE=None, PERSON7=None, valueOf_=''):
        supermod.TASK.__init__(self, CATEGORY1, STARTDATE, CATEGORY3, CATEGORY2, CATEGORY5, CATEGORY4, CATEGORY7, CATEGORY6, CATEGORY9, CATEGORY8, NUMPERSON, PERSON2, PERSON3, COST, EXTERNALID, DEPENDS9, PERSON4, PERSON5, DUEDATESTRING, ICONINDEX, CREATIONDATESTRING, PERSON9, WEBCOLOR, PERSON8, LASTMOD, TIMEESTUNITS, COLOR, TITLE, LASTMODSTRING, PRIORITYWEBCOLOR, POS, ID, PRIORITY, CALCTIMESPENT, DEPENDS, NUMCATEGORY, DONEDATESTRING, CREATIONDATE, PERCENTDONE, TIMEESTIMATE, STATUS, DEPENDS7, ALLOCATEDBY, DONEDATE, RISK, STARTDATESTRING, TEXTCOLOR, NUMDEPENDS, CALCPERCENTDONE, FLAG, VERSION, TIMESPENT, TEXTWEBCOLOR, PRIORITYCOLOR, FILEREFPATH, DUEDATE, CALCTIMEESTIMATE, CATEGORY, DEPENDS6, DEPENDS5, DEPENDS4, DEPENDS3, DEPENDS2, DEPENDS1, CUSTOMCOMMENTS, TIMESPENTUNITS, COMMENTS, DEPENDS8, PERSON, PERSON1, CALCCOST, PERSON6, COMMENTSTYPE, PERSON7, valueOf_)
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


