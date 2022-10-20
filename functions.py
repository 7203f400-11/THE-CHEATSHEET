class MathFunctions(self):
  def __init__(self):
    return 'OPERATING'
  def percentval(self):
    def inputs():
        startval = input("Enter original value\n")
        endval = input("Enter new value\n")
        return float(startval), float(endval)
    def change(s, e):
        change = e-s
        fraction = change/s
        return fraction*100
    s, e = inputs()
    out = change(s, e)
    approximate = round(change(s, e))
    if out == approximate:
        return f'Exact: {out}%'
    else:
        return (f'Exact(almost): {out}', f'Approximate: {approximate}%')
    
   
