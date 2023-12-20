


import asyncio

data = {
    "object":{
                "da":{
                        "ps":[
                            "https://i.ibb.co/mG7cxFD/display-audit-168-16988305241892453492482315125.jpg",
                            "https://i.ibb.co/rpt2JFq/C01-6225-jpg-rf-2652d509af5b98497e63b6d13eae1dde.jpg"
                        ],
                        "ds":[
                            "https://i.ibb.co/BcGbJZw/ubl-ds-english-version-1-24.jpg",
                            "https://i.ibb.co/Cpj5GfL/display-audit-178-16988979482964936100751368791.jpg"
                        ],
                        "ns":[
                            "https://i.ibb.co/pfJvfs4/ns-version-1-pic-20.jpg"
                        ]
                    },
                "qpds":["https://i.ibb.co/pfJvfs4/ns-version-1-pic-20.jpg"],
                "sos":["https://i.ibb.co/pfJvfs4/ns-version-1-pic-20.jpg"]
    }
}


task = [
    asyncio.create_task(detect("ps","https://i.ibb.co/mG7cxFD/display-audit-168-16988305241892453492482315125.jpg")),
    asyncio.create_task(detect('ps', 'https://i.ibb.co/rpt2JFq/C01-6225-jpg-rf-2652d509af5b98497e63b6d13eae1dde.jpg')),
    asyncio.create_task(detect('ds', 'https://i.ibb.co/BcGbJZw/ubl-ds-english-version-1-24.jpg')),
    asyncio.create_task(detect('ds', 'https://i.ibb.co/Cpj5GfL/display-audit-178-16988979482964936100751368791.jpg')),
    asyncio.create_task(detect('ns', 'https://i.ibb.co/pfJvfs4/ns-version-1-pic-20.jpg')),
    asyncio.create_task(detect('qpds', 'https://i.ibb.co/pfJvfs4/ns-version-1-pic-20.jpg')),
    asyncio.create_task(detect('sos', 'https://i.ibb.co/pfJvfs4/ns-version-1-pic-20.jpg'))
]