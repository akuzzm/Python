def bread(function_to_decorate):
  def put_bread():
    print "Hello, I am a bread!"
  
    function_to_decorate()
  
    print "Hello, I am a bread!"
  return put_bread
  
  def salad(function_to_decorate):
  def put_salad():
    print "Hello, I am a salad!"
  
    function_to_decorate()
  
    print "Hello, I am a salad!"
  return put_salad

@bread
@salad
def meat():
  print "Hello, I am a meet!"
  
meat()  

