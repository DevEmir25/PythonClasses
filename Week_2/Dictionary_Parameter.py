
def unit_process(**unit):
  print("Unit Type :", type(unit))
  print("Unit Name : " + unit["name"])
  print("Unit Type :", unit["type"])
  print("Unit Year :", unit["year"])


unit_process(name = "Balikesir" , type = "Üniversite",  year = 1992)