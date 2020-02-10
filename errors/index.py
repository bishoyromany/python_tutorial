try:
    print(5/0)
except Exception as e:
    print("error" , e) 
finally:
    print("Done")