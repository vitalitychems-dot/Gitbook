from quakes import summarize
fc={"features":[{"properties":{"mag":2.0,"place":"A","time":1},"geometry":{"coordinates":[1,2,3]}},
 {"properties":{"mag":5.1,"place":"B","time":2},"geometry":{"coordinates":[4,5,6]}},
 {"properties":{"mag":None,"place":"C","time":3},"geometry":{"coordinates":[0,0,0]}}]}
s=summarize(fc); assert s["count"]==2 and s["max_mag"]==5.1 and s["top5"][0]["place"]=="B"; print("PASS")
