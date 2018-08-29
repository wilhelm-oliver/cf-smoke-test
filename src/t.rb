# should not report Layout/AccessModifierIndentation, Layout/EmptyLinesAroundAccessModifier, Layout/EndOfLine
# should report Lint/DuplicateMethods

# bad
class Plumbus
private
  def smooth; end
end

# good
class Plumbus
  private
  def smooth; end
end
