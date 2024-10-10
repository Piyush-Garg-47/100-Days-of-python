ep1 = {23:122 , 24:234 , 25:456 ,26:466 ,27 :678 ,28 :789}

ep2 ={29:455 ,30:876 ,31 :987}

ep1.update(ep2)

print("epdated value of dictionary" , ep1)

ep2.clear()

print("after clearing the value of ep2" , ep2) 

ep1.pop(23)

print(ep1)

print(ep1.popitem())