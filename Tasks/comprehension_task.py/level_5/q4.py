"""
Add 18% GST Input:[100,250,500,800] Output:[118.0,295.0,590.0,944.0]
"""

numbers = [100,250,500,800]
# percentage/100*that number

gst = [num+((18/100)*num) for num in numbers]
print(gst)