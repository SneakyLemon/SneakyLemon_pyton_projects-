import random
trafic_light1 = ""
trafic_light2 = ""
trafic_light3 = ""
trafic_light1_cars = random.randint(0,20)
trafic_light2_cars = random.randint(0,20)
trafic_light3_cars = random.randint(0,20)
random_choose = 0
answer = ""
while answer != "no":
    most_cars = max(trafic_light1_cars,trafic_light2_cars,trafic_light3_cars)
    if (trafic_light1_cars == most_cars) and (trafic_light2_cars == most_cars):
        random_choose = random.randint (0,3)
    elif (trafic_light1_cars == most_cars) and (trafic_light3_cars == most_cars):
        random_choose = random.randint (0,3)
    else:
        choose = random.randint (0,3)
    if ((trafic_light1_cars == most_cars) and (trafic_light2_cars < most_cars) and (trafic_light3_cars < most_cars) or (random_choose == 1)):
        trafic_light1 = "Green"
        leaving_cars = random.randint (0,5)
        trafic_light1_cars -= leaving_cars
        coming_cars1 = random.randint (0,5)
        coming_cars2 = random.randint (0,5)
        trafic_light2_cars += coming_cars1
        trafic_light3_cars += coming_cars2
        print ("Το φαναρι εχει" , trafic_light1_cars , "αυτοκινητα")
    elif ((trafic_light2_cars == most_cars) and (trafic_light1_cars < most_cars) and (trafic_light3_cars < most_cars) or (random_choose == 2)):
          trafic_light2 = "Green"
          leaving_cars = random.randint (0,5)
          trafic_light2_cars -= leaving_cars
          coming_cars1 = random.randint (0,5)
          coming_cars2 = random.randint (0,5)
          trafic_light1_cars += coming_cars1
          trafic_light3_cars += coming_cars2
          print ("Το φαναρι εχει" , trafic_light2_cars , "αυτοκινητα")
    else:
        trafic_light3 = "Green"
        leaving_cars = random.randint (0,5)
        trafic_light3_cars -= leaving_cars
        coming_cars1 = random.randint (0,5)
        coming_cars2 = random.randint (0,5)
        trafic_light1_cars += coming_cars1
        trafic_light2_cars += coming_cars2
        print ("Το φαναρι εχει" , trafic_light3_cars ,"αυτοκινητα")
    print ("Φευγουν" , leaving_cars , "αυτοκινητα")
    print ("Ερχοστα στα αλλα δυο φαναρια" , coming_cars1 + coming_cars2 , "αυτοκινητα")
    answer = input ("you want to continue?")
    
    
