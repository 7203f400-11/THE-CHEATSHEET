import functions.py as functions #import functions
import csv #command base handling
#from colorama import Fore, Back, init #cosmetics
commandpath = "7203f400-11/THE-CHEATSHEET/commands.csv"
def loadfiles():
  '''
  Loads command base
  '''
  with open(commandpath) as commands:
    commandbase = [row["COMMAND"] for row in commands]
  return (commandbase,)
def dash(n):
  '''
  Takes command input
  '''
  while True:
    try:
      command = input("Enter your command\n")
      return cbase[command]
      break
    except ValueError:
      print("\nInvalid Command")
      continue
def container():
  '''
  Initializes an instance of the functions file
  '''
  c = functions.MathFunctions()
  return (c,)
def main():
  '''
  The main script
  '''
  cbase = loadfiles()
  daman = container()
  command = dash(cbase)
  c.command()
if __name__ == "__main__":
  main()
