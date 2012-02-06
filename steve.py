class MapStepper(object):
  def step(self, start, direction):
    return start[direction]

class ObjectStepper(object):
  def step(self, start, direction):
    return getattr(start, direction)
