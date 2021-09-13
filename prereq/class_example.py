
class IceCream:
  # constructor
  # dunder init method
  def __init__(self):
    self.scoops = 0
  
  def add(self, scoops):
    # this->scoops += scoops
    # this.scoops += scoops
    self.scoops += scoops

  def eat(self, scoops):
    if self.scoops < scoops:
      print("Inside base icecream")
      print("Not enough bites left!")
    else:
      self.scoops -= scoops

# C++: class ButterScotch : public IceCream {...}
# Java: public class ButterScotch extends IceCream { ... }
# Ruby: class ButterScotch < IceCream

# extends from the IceCream
class ButterScotch(IceCream):
  def eat(self, scoops):
    if self.scoops < 2*scoops:
      print("Inside butterscotch")
      print("Not enough bites left!")
    else:
      self.scoops -= 2*scoops


# IceCream ice_cream;
# IceCream ice_cream = new IceCream();

"""
ice_cream = IceCream()
print(ice_cream.scoops)

ice_cream.eat(1)
print(ice_cream.scoops)

ice_cream.add(2)
print(ice_cream.scoops)

ice_cream.eat(1)
print(ice_cream.scoops)
"""

ice_cream = ButterScotch()

print(ice_cream.scoops)

ice_cream.eat(1)
print(ice_cream.scoops)

ice_cream.add(2)
print(ice_cream.scoops)

ice_cream.eat(1)
print(ice_cream.scoops)