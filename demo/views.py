from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
import random


# SEARCH
# SEARCHING FOR PRODUCT THAT CONTAIN THE SEARCH CONTENT
@api_view(['GET'])
def SearchProduct(request):
    data = [
    {
        "code": "DOL1213",
        "company": {
            "name": "Micro Labs Ltd",
            "id": 1
        },
        "molicule": {
            "name": "Paracetamol (650mg)"
        },
        "category": {
            "name": "Tablet"
        },
        "name": "Dolo 650 Tablet",
        "type": 1
    },
    {
        "code": "WEL5548",
        "company": {
            "name": "Sun Pharmaceutical",
            "id": 2
        },
        "molicule": {
            "name": "Paracetamol (650mg)"
        },
        "category": {
            "name": "Tablet"
        },
        "name": "Welset 650 Tablet",
        "type": 1
    },
    {
        "code": "XTP5656",
        "company": {
            "name": "Torrent Pharmaceuticals",
            "id": 3
        },
        "molicule": {
            "name": "Paracetamol (650mg)"
        },
        "category": {
            "name": "Tablet"
        },
        "name": "XTPara 650mg Tablet",
        "type": 1
    },
    {
        "code": "PAC0001",
        "company": {
            "name": "Ipca Laboratories Ltd",
            "id": 4
        },
        "molicule": {
            "name": "Paracetamol (650mg)"
        },
        "category": {
            "name": "Tablet"
        },
        "name": "Pacimol 650 Tablet",
        "type": 1
    },
    {
        "code": "AST0001",
        "company": {
            "name": "Torrent Pharmaceuticals",
            "id": 3
        },
        "molicule": {
            "name": "Prilocaine (2.5% w/w) + Lidocaine (2.5% w/w)"
        },
        "category": {
            "name": "Cream"
        },
        "name": "Asthesia Cream",
        "type": 1
    },
    {
        "code": "ALP0001",
        "company": {
            "name": "Torrent Pharmaceuticals",
            "id": 3
        },
        "molicule": {
            "name": "Alprazolam (0.25mg)"
        },
        "category": {
            "name": "Tablet"
        },
        "name": "Alprax 0.25 Tablet",
        "type": 1
    }
]
    return Response(data)


# INDIVIDUAL PRODUCT PROFILE
# GETING MEDICINE DATA USING CODE
@api_view(['GET'])
def ProductData(request):
    return Response({
    "code": "XTP5656",
    "company": {
        "name": "Torrent Pharmaceuticals",
        "id": 3
    },
    "molicule": {
        "name": "Paracetamol (650mg)"
    },
    "category": {
        "name": "Tablet"
    },
    "name": "XTPara 650mg Tablet",
    "type": 1
})


#IS THE PRODUCT IS LIKED
@api_view(['GET'])
def isLiked(request):

    return Response(random.choice([True, False]))


 #INDIVIDUAL PRODUCT PROFILE
@api_view([ 'POST'])
def LikeFunction(request):
    return Response(random.choice(['liked', 'unliked']))

@api_view(['GET'])
def Substitute(request):
    
    return Response([
    [
        {
            "product": {
                "code": "DOL1213",
                "company": {
                    "name": "Micro Labs Ltd",
                    "id": 1
                },
                "molicule": {
                    "name": "Paracetamol (650mg)"
                },
                "category": {
                    "name": "Tablet"
                },
                "name": "Dolo 650 Tablet",
                "type": 1
            }
        },
        {
            "product": {
                "code": "WEL5548",
                "company": {
                    "name": "Sun Pharmaceutical",
                    "id": 2
                },
                "molicule": {
                    "name": "Paracetamol (650mg)"
                },
                "category": {
                    "name": "Tablet"
                },
                "name": "Welset 650 Tablet",
                "type": 1
            }
        }
    ],
    [
        {
            "product": {
                "code": "XTP5656",
                "company": {
                    "name": "Torrent Pharmaceuticals",
                    "id": 3
                },
                "molicule": {
                    "name": "Paracetamol (650mg)"
                },
                "category": {
                    "name": "Tablet"
                },
                "name": "XTPara 650mg Tablet",
                "type": 1
            },
            "like": 4
        },
        {
            "product": {
                "code": "WEL5548",
                "company": {
                    "name": "Sun Pharmaceutical",
                    "id": 2
                },
                "molicule": {
                    "name": "Paracetamol (650mg)"
                },
                "category": {
                    "name": "Tablet"
                },
                "name": "Welset 650 Tablet",
                "type": 1
            },
            "like": 1
        },
        {
            "product": {
                "code": "PAC0001",
                "company": {
                    "name": "Ipca Laboratories Ltd",
                    "id": 4
                },
                "molicule": {
                    "name": "Paracetamol (650mg)"
                },
                "category": {
                    "name": "Tablet"
                },
                "name": "Pacimol 650 Tablet",
                "type": 1
            },
            "like": 1
        }
    ],
    [
        {
            "code": "DOL1213",
            "company": {
                "name": "Micro Labs Ltd",
                "id": 1
            },
            "molicule": {
                "name": "Paracetamol (650mg)"
            },
            "category": {
                "name": "Tablet"
            },
            "name": "Dolo 650 Tablet",
            "type": 1
        }
    ]
])
    
@api_view(['GET'])
def SearchMolicule(request):
    return Response([
    {
        "name": "Paracetamol (650mg)"
    },
    {
        "name": "Prilocaine (2.5% w/w) + Lidocaine (2.5% w/w)"
    },
    {
        "name": "Alprazolam (0.25mg)"
    }
])

# GETTINF ALL MEDICINES THAT CONTAINS THE MOLICULE
# THE RELATED MEDICINE TO THE MOLICULE
def myFunc2(e):
    return e['like']

@api_view(['GET'])
def Generic(request):
    return Response([
    [
        {
            "product": {
                "code": "DOL1213",
                "company": {
                    "name": "Micro Labs Ltd",
                    "id": 1
                },
                "molicule": {
                    "name": "Paracetamol (650mg)"
                },
                "category": {
                    "name": "Tablet"
                },
                "name": "Dolo 650 Tablet",
                "type": 1
            }
        },
        {
            "product": {
                "code": "WEL5548",
                "company": {
                    "name": "Sun Pharmaceutical",
                    "id": 2
                },
                "molicule": {
                    "name": "Paracetamol (650mg)"
                },
                "category": {
                    "name": "Tablet"
                },
                "name": "Welset 650 Tablet",
                "type": 1
            }
        }
    ],
    [
        {
            "product": {
                "code": "XTP5656",
                "company": {
                    "name": "Torrent Pharmaceuticals",
                    "id": 3
                },
                "molicule": {
                    "name": "Paracetamol (650mg)"
                },
                "category": {
                    "name": "Tablet"
                },
                "name": "XTPara 650mg Tablet",
                "type": 1
            },
            "like": 4
        },
        {
            "product": {
                "code": "WEL5548",
                "company": {
                    "name": "Sun Pharmaceutical",
                    "id": 2
                },
                "molicule": {
                    "name": "Paracetamol (650mg)"
                },
                "category": {
                    "name": "Tablet"
                },
                "name": "Welset 650 Tablet",
                "type": 1
            },
            "like": 1
        },
        {
            "product": {
                "code": "PAC0001",
                "company": {
                    "name": "Ipca Laboratories Ltd",
                    "id": 4
                },
                "molicule": {
                    "name": "Paracetamol (650mg)"
                },
                "category": {
                    "name": "Tablet"
                },
                "name": "Pacimol 650 Tablet",
                "type": 1
            },
            "like": 1
        }
    ],
    [
        {
            "code": "DOL1213",
            "company": {
                "name": "Micro Labs Ltd",
                "id": 1
            },
            "molicule": {
                "name": "Paracetamol (650mg)"
            },
            "category": {
                "name": "Tablet"
            },
            "name": "Dolo 650 Tablet",
            "type": 1
        }
    ]
])

# MOLICULE LIST
@api_view(['GET'])
def DoctorMolicules(request):
    data = [
    {
        "name": "Paracetamol (650mg)"
    },
    {
        "name": "Paracetamol (150mg)"
    },
    {
        "name": "Paracetamol (250mg)"
    }
]
    return Response (data)

# OPENIG INDIVIDUAL MOLICULE
@api_view(['GET'])
def DoctorItems(request):
    return Response([
    {
        "product": {
            "code": "XTP5656",
            "company": {
                "name": "Torrent Pharmaceuticals",
                "id": 3
            },
            "molicule": {
                "name": "Paracetamol (650mg)"
            },
            "category": {
                "name": "Tablet"
            },
            "name": "XTPara 650mg Tablet",
            "type": 1
        },
        "like": 4
    },
    {
        "product": {
            "code": "PAC0001",
            "company": {
                "name": "Ipca Laboratories Ltd",
                "id": 4
            },
            "molicule": {
                "name": "Paracetamol (650mg)"
            },
            "category": {
                "name": "Tablet"
            },
            "name": "Pacimol 650 Tablet",
            "type": 1
        },
        "like": 1
    }
])

# DOCTOR PROFILE
@api_view(['GET'])
def doctorProfile(request):
    return Response({
    "id": 2,
    "name": "pushpan",
    "registrationNumber": "dfasdf454",
    "district": "Wayanad",
    "state": 'null',
    "working": "sdasd",
    "specialization": "hsidfhijasdfjnasd",
    "description": "kjhdskjfhasdh",
    "lat": "11.7932652",
    "lon": "76.1643871",
    "user": 6
})
