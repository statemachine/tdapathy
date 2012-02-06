class PathWalker(object):
  def walkpath(self, origin, step_iterator, false_path_listener, action):
    current = origin
    for index, (mode, direction) in enumerate(step_iterator):
      stepper = self.stepper_map[mode]
      try:
        current = stepper.step(current, direction)
      except Exception, e:
        false_path_listener.notify(
          step_iterator, current, index, mode, direction, e)
    action.do(current)
