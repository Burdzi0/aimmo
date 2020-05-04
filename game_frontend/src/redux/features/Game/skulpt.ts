/* eslint-disable no-console */

let skulptInitialized = false
let avatarCode = `
from base import *

def next_turn(world_state, avatar_state):
    return MoveAction(direction.NORTH)
`

function builtinRead (x: string) {
  // console.log(`I am here for ${x}`)
  if (x === './avatar.py') {
    return avatarCode
  } else if (x === './base.py') {
    return `
class Direction(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Direction(x={}, y={})".format(self.x, self.y)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def serialise(self):
        return {"x": self.x, "y": self.y}


NORTH = Direction(0, 1)
EAST = Direction(1, 0)
SOUTH = Direction(0, -1)
WEST = Direction(-1, 0)

ALL_DIRECTIONS = (NORTH, EAST, SOUTH, WEST)
class Directions(object):
    def __init__(self):
        self.NORTH = NORTH
        self.EAST = EAST
        self.WEST = WEST
        self.SOUTH = SOUTH

direction = Directions()

class Action:
    def serialise(self):
        pass


class WaitAction(Action):
    def serialise(self):
        return {"action_type": "wait"}


class PickupAction(Action):
    def serialise(self):
        return {"action_type": "pickup"}


class MoveAction(Action):
    def __init__(self, direction):
        self.direction = direction

    def serialise(self):
        return {
            "action_type": "move",
            "options": {"direction": self.direction.serialise()},
        }
  
  
class AttackAction(Action):
    def __init__(self, direction):
        self.direction = direction

    def serialise(self):
        return {
            "action_type": "attack",
            "options": {"direction": self.direction.serialise()},
        }
  


class Location(object):
  def __init__(self, x, y):
      self.x = x
      self.y = y

  def __add__(self, direction):
      return Location(self.x + direction.x, self.y + direction.y)

  def __sub__(self, direction):
      return Location(self.x - direction.x, self.y - direction.y)

  def __repr__(self):
      return "Location({}, {})".format(self.x, self.y)

  def __eq__(self, other):
      return self.x == other.x and self.y == other.y

  def __ne__(self, other):
      return not self == other

  def __hash__(self):
      return hash((self.x, self.y))
  `
  }
  if (Sk.builtinFiles === undefined || Sk.builtinFiles.files[x] === undefined) {
    // console.error(`File not found: ${x}`)
    throw new Error(`File not found: ${x}`)
  }
  return Sk.builtinFiles['files'][x]
}

let logCollector: object

function addToLogCollector (log: string) {
  console.log(log)
  const jsonString = log.replace(/'/g, '"')
  logCollector = JSON.parse(jsonString)
}

export function runSkulpt (userCode) {
  if (!skulptInitialized) {
    return
  }
  avatarCode = `from base import *

${userCode}
`
  const runTurn = `
import avatar

next_action = avatar.next_turn(None, None)

print(next_action.serialise())
`

  try {
    Sk.importMainWithBody('runTurn', false, `${runTurn}`, false)
  } catch (error) {
    console.log(error)
  }
  console.log('finished runTurn')

  // Sk.importMainWithBody('location', true, code, false)
  //   console.log(logCollector)
  return logCollector
}

export function initializeSkulpt () {
  console.log('I am being initialized')
  Sk.execLimit = 1000
  Sk.retainGlobals = true
  Sk.builtins.MEMORY = Sk.builtin.int_(0)
  console.log(Sk.globals)
  Sk.configure({
    read: builtinRead,
    __future__: Sk.python3,
    output: addToLogCollector,
    execLimit: 1000,
    retainGlobals: true
  })
  Sk.doOneTimeInitialization()

  Sk.importModule('base')
  // Sk.importModule('location', false, false)
  skulptInitialized = true
}