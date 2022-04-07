
menu = {

 "breakfast": {
                "hours": "7-11",
                 "items": {
                            "breakfast burritos": "$6.00",
                            "pancakes": "$4.00"
                          }
              },
 "lunch" : {
                "hours": "11-3",
                 "items": {
                            "hamburger": "$5.00"
                          }
          },
 "dinner": {
                "hours": "3-10",
                "items": {
                           "spaghetti": "$8.00"
                         }
          }
 }


import json
menu_json = json.dumps(menu)
print(menu_json)

print('\n\n')
menu2 = json.loads(menu_json)
print(menu2)