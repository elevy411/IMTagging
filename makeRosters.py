import csv
from time import sleep

rosterDic = {}
masterControl = True

class button:
  def __init__(self,name,(x,y),cellColor,color='Black',func=None):
    self.name = Cell(x,y).name
    self.location = (x,y)
    self.function = func
    temp = Cell(x,y)
    temp.value = name
    temp.copy_format_from(Cell("A1"))  
    temp.font.bold = True
    temp.font.color = color
    if cellColor != 'None':
      temp.color = cellColor

def makeDicsBoth():
  global rosterDic,masterControl
  active_sheet('Both')
  for cell in Cell(4,3).horizontal_range:
    rosterDic[cell.value] = []
    for subCell in cell.vertical_range:
      if subCell.value == 'O':
        row = subCell.row
        rosterDic[cell.value].append(Cell(row,2).value)
    print "Ran A Cell"
  Cell("ControlPage","A3").value = "Rosters Made"
  autofit()
  active_cell("ControlPage","A1")
  autofit()

# def makeDics():
#   global rosterDic,masterControl
#   active_sheet('Guys')
#   for cell in Cell(4,3).horizontal_range:
#     rosterDic[cell.value] = []
#     for subCell in cell.vertical_range:
#       if subCell.value == 'O':
#         row = subCell.row
#         rosterDic[cell.value].append(Cell(row,2).value)
#   for cell in Cell("Girls",4,3).horizontal_range:
#     for subCell in cell.vertical_range:
#       if subCell.value == 'O':
#         row = subCell.row
#         rosterDic[cell.value].append(Cell("Girls",row,2).value)
#   Cell("ControlPage","A3").value = "Rosters Made"
#   autofit()
#   active_cell("ControlPage","A1")

def stop():
  global masterControl
  active_sheet("ControlPage")
  Cell("A1").clear()
  Cell("A3").clear()
  masterControl = False

def export():
  global rosterDic
  Cell('ControlPage',1,1).value = 'Exporting'
  for key in rosterDic:
    file = open('{}.txt'.format(key),'w')
    for x in rosterDic[key]:
      file.write('{}\n'.format(x))
    file.close()
  Cell('ControlPage',1,1).value = 'Finished'
  active_cell('ControlPage',1,1)

def mix():
  global rosterDic
  active_sheet("ControlPage")
  Cell('A1').value = "Mixing"
  lS = 5
  lF = lS + len(Cell("J5").vertical_range)
  sportList = []
  for i in range(lS,lF):
    if Cell("I{}".format(i)).value == 'X':
      sportList.append(Cell("J{}".format(i)).value)
  bigList    = [] 
  dupList    = []
  rosterList = []
  for x in sportList:
    for y in rosterDic[x]:
        bigList.append(y)
  print sportList
  for i in range(len(sportList)):
    rosterList.append(rosterDic[sportList[i]])  # the playoff rosters
  for i in range(len(bigList)-1):
    if i+1 == len(bigList):
      break
    if bigList[i] in bigList[i+1:]:
      dupList.append(bigList[i])
      for roster in rosterList:
        roster.remove(bigList[i])
  rosterList.append(dupList)
  for i in range(len(rosterList)):
    if i == len(rosterList)-1:
      rosterDic['Playoffs Both'] = rosterList[i]
    else:
      rosterDic['Playoffs {}'.format(i+1)] = rosterList[i]
  active_cell("A1")


def mainFunc():
  global masterControl
  active_sheet("ControlPage")
  makeBothCell = button('MakeBoth',(5,3),'Yellow','Black',makeDicsBoth)
  stopCell = button('StopProgram',(5,5),'Red','Black',stop)
  textCell = button('ToTxtFiles',(7,4),'Blue','White',export)
  mixCell = button('Make Playoffs',(7,5),'Yellow','Black',mix)

  active_cell("A1")
  autofit()
  Cell(1,1).value = 'Running'
  while (masterControl):
    if active_cell().name == makeBothCell.name:
      makeBothCell.function()
    if active_cell().name == stopCell.name:
      stopCell.function()
    if active_cell().name == textCell.name:
      textCell.function()
    if active_cell().name == mixCell.name:
      mixCell.function()

  active_sheet("ControlPage")
  Cell(1,1).value = 'Stopped'

mainFunc()